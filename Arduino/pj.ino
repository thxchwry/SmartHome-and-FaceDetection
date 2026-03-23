#include <Servo.h> //เรียกใช้ไลบารี Servo

Servo myservo; //ประกาศตัวแปร Servo เอาไว้ใช้ควบคุม Servo
String input; 

void setup() {
  Serial.begin(9600);  // ตั้งค่า Serial communication ที่อัตราความเร็ว 9600 บิตต่อวินาที
  myservo.attach(4);    //เชื่อมต่อ Servo กับขาดิจิทัลขาที่ 4 บนบอร์ด
  myservo.write(0);     // ประตูปิด 0 องศา
  Serial.println("พร้อมรับคำสั่งจาก Serial Monitor");//แจ้งว่า Arduino พร้อมใช้งานแล้ว
}

void loop() {
  if (Serial.available() > 0) {
    input = Serial.readStringUntil('\n');  // อ่านข้อมูลจาก Serial จนถึง newline
    Serial.println("ได้รับคำสั่ง: " + input);  // แสดงคำสั่งที่ได้รับ

    if (input == "open") {  //ตรวจสอบว่า open ไหม
      Serial.println("กำลังเปิดประตู...");  // ก็จะแจ้งว่ากำลังเปิดประตู
      myservo.write(180);    // สั่งเปิดประตู โดย Servo หมุนไปที่ 180 องศา
      delay(5000);           // เปิดค้างไว้ 5 วินาที
      myservo.write(0);      // ปิดประตู Servo ก็จะกลับไปที่ 0 องศา
      delay(1000);           // หน่วงเวลา 1 วินาที ก่อนจะรับคำสั่งใหม่
    } else {
      Serial.println("คำสั่งไม่ถูกต้อง!");  // จะแสดงขึ้นมาว่าคำสั่งไม่ถูกต้อง
    }
  }
}
