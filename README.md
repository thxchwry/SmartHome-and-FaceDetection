# SmartHome & Face Detection System 🏠🔍

โปรเจกต์ระบบ Smart Home ที่ผสานการทำงานของ **การจดจำใบหน้า (Face Recognition)** เข้ากับ **การควบคุมฮาร์ดแวร์ผ่าน Arduino** เพื่อเปิด-ปิดประตูอัตโนมัติ และแจ้งเตือนผ่าน **Telegram Bot** เมื่อตรวจพบบุคคล และมีการตรวจจับการเคลื่อนไหวของสิ่งมีชีวิตเพื่อทำการปิด-เปิดไฟ

---

## 🔍 ภาพรวมของโปรเจกต์

ระบบถูกออกแบบมาเพื่อทำหน้าที่เป็น **ประตูอัจฉริยะ (Smart Door)** โดยใช้กล้องเว็บแคมสแกนและวิเคราะห์ใบหน้าแบบ Real-time หากตรวจพบบุคคลที่ระบบรู้จัก จะส่งสัญญาณไปยัง Arduino เพื่อสั่งเปิดประตูทันที และส่งการแจ้งเตือนพร้อมภาพไปยัง Telegram หากตรวจพบบุคคลที่ไม่รู้จัก ระบบจะแจ้งเตือนเจ้าของบ้านให้ทราบทันที และมีการตรวจจับการเคลื่อนไหวของสิ่งมีชีวิตเพื่อทำการปิด-เปิดไฟ

---

## ✨ ฟีเจอร์หลัก

- 🎥 **Real-time Face Detection** — ตรวจจับใบหน้าจากกล้องแบบ Real-time
- 🧠 **Face Recognition** — เปรียบเทียบและจดจำใบหน้าจากฐานข้อมูลที่กำหนดไว้
- 🔓 **Auto Door Unlock** — ส่งสัญญาณเปิดประตูผ่าน Arduino เมื่อจดจำใบหน้าได้
- 📲 **Telegram Notification** — แจ้งเตือนพร้อมรูปภาพเมื่อตรวจพบบุคคล (ทั้งที่รู้จักและไม่รู้จัก)
- 🚨 **Unknown Person Alert** — แจ้งเตือนทันทีเมื่อพบบุคคลแปลกหน้า

---

## 🛠️ เทคโนโลยีที่ใช้

**ฝั่ง Software (Python)**

- **Language**: Python 3.x
- **Face Recognition**: `face-recognition` + `dlib`
- **Computer Vision**: `opencv-python`
- **Serial Communication**: `pyserial`
- **Notification**: `requests` (Telegram Bot API)

**ฝั่ง Hardware (Arduino)**

- **Board**: Arduino (เชื่อมต่อผ่าน Serial Port)
- **Language**: C/C++ (Arduino IDE)
- **Function**: รับคำสั่งจาก Python เพื่อควบคุมการเปิด-ปิดประตู
