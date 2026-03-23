import cv2
import face_recognition ## สำหรับตรวจจับและรู้จำใบหน้า
import numpy as np
import os
import requests
import time
import serial ##ใช้เชื่อมต่อกับ Arduino ผ่านพอร์ตอนุกรม

# ====== ตั้งค่า Serial กับ Arduino ======
try:
    arduino = serial.Serial("/dev/cu.usbserial-110", 9600, timeout=1)  # ✅ เปลี่ยนเป็น COM7 แล้ว
    time.sleep(2)  # รอ Arduino พร้อม
    print("✅ เชื่อมต่อ Arduino สำเร็จ")
except:
    arduino = None
    print("❌ ไม่สามารถเชื่อม Arduino ได้")

# ====== ฟังก์ชันสั่งเปิดประตู ======
def open_door():
    if arduino:
        try:
            arduino.write(b"open\n")
            print("🔓 สั่งเปิดประตูแล้ว")
        except Exception as e:
            print("❌ ไม่สามารถส่งข้อมูลไป Arduino:", e)
    else:
        print("⚠️ Arduino ไม่พร้อม")

# ====== ตั้งค่า Telegram Bot ======
BOT_TOKEN = "7965699816:AAF_U-5JGwiePPxOZDu6vqiS8MIcd4Omn-8"
CHAT_ID = "7980876024"

def send_telegram_message(message, image_path=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})
    
    if image_path and os.path.exists(image_path):
        with open(image_path, "rb") as photo:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
                data={"chat_id": CHAT_ID},
                files={"photo": photo}
            )

# ====== โหลดใบหน้าที่รู้จักทั้งหมด ======
known_face_encodings = []
known_face_names = []

KNOWN_FOLDER = "known_faces"
for filename in os.listdir(KNOWN_FOLDER):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        path = os.path.join(KNOWN_FOLDER, filename)
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_face_encodings.append(encodings[0])
            name = os.path.splitext(filename)[0]
            known_face_names.append(name)
            print(f"✅ โหลด: {name}")
        else:
            print(f"⚠️ ไม่พบใบหน้าใน: {filename}")

# ====== เปิดกล้อง ======
video_capture = cv2.VideoCapture(0)
last_alert_time = 0
alert_delay = 10  # วินาที

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        image_path = f"detected_{name}.jpg"
        cv2.imwrite(image_path, frame)

        if time.time() - last_alert_time > alert_delay:
            if name == "Unknown":
                print("🚨 พบคนที่ไม่รู้จัก!")
                send_telegram_message("🚨 พบคนที่ไม่รู้จัก!", image_path)
            else:
                print(f"✅ พบ: {name}")
                send_telegram_message(f"✅ ตรวจพบ: {name}", image_path)
                open_door()  # สั่งเปิดประตูเมื่อรู้จัก
            last_alert_time = time.time()

        # วาดกรอบและชื่อ
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()

#source venv/bin/activate

try:
    arduino = serial.Serial("/dev/cu.usbserial-110", 9600, timeout=1)  
    time.sleep(2) 
    print("เชื่อมต่อ Arduino สำเร็จ")
except:
    arduino = None
    print("ไม่สามารถเชื่อม Arduino ได้")