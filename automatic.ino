
int Rpi = 1;
int control = 1;
int trigPin = 12;                  //Trig Pin
int echoPin = 11;                  //Echo Pin
int carspeed = 150;
long duration, cm, inches;

void setup() { 

Serial.begin(9600);

pinMode(4, OUTPUT); //左輪
pinMode(5, OUTPUT);

pinMode(6, OUTPUT); //右輪
pinMode(7, OUTPUT);

pinMode(trigPin, OUTPUT);        //Define inputs and outputs 
pinMode(echoPin, INPUT);

}

void loop() { 
//Rpi傳值
if (Serial.available() > 0){
  Rpi = Serial.read();
}
/*
//超聲波感測
digitalWrite(trigPin, LOW);
delayMicroseconds(5);
digitalWrite(trigPin, HIGH);     // 給 Trig 高電位，持續 10微秒
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

duration = pulseIn(echoPin, HIGH);   // 收到高電位時的時間
 
cm = (duration/2) / 29.1;         // 將時間換算成距離 cm

Serial.print("Distance : ");  
Serial.print(cm);
Serial.print("cm");
Serial.println();

if (cm < 10){  //如果靠近障礙物，車體控制進入避障動作(case 20)
  control = 20;
}
else{
  control = Rpi; 
}
*/
control = Rpi;

switch (control){  //控制車體方向
case 1: //前進
analogWrite(4, LOW); //左輪前進
analogWrite(5, carspeed);

analogWrite(6, LOW); //右輪前進
analogWrite(7, carspeed);
break;

case 2: //後退
analogWrite(4, carspeed); //左輪後退
analogWrite(5, LOW);

analogWrite(6, carspeed); //右輪後退
analogWrite(7, LOW);
break;

case 3: //左轉
analogWrite(4, carspeed); //左輪後退
analogWrite(5, LOW);

analogWrite(6, LOW); //右輪前進
analogWrite(7, carspeed);
break;

case 4: //右轉
analogWrite(4, LOW); //左輪前進
analogWrite(5, carspeed);

analogWrite(6, carspeed); //右輪後退
analogWrite(7, LOW);
break;


case 10: //找球   //加判斷式，當找到球體位置時要往球的方向前進
//原地旋轉找球
analogWrite(4, carspeed); //左輪後退
analogWrite(5, LOW);

analogWrite(6, LOW); //右輪前進
analogWrite(7, carspeed);
delay(1000);

analogWrite(4, LOW); //左輪前進
analogWrite(5, carspeed);

analogWrite(6, 250); //右輪後退
analogWrite(7, carspeed);
delay(1000);


case 20: //避障
//暫停2秒
analogWrite(4, LOW); //左輪停止
analogWrite(5, LOW);

analogWrite(6, LOW); //右輪停止
analogWrite(7, LOW);
delay(2000);

//左轉
analogWrite(4, LOW); //左輪停止
analogWrite(5, LOW);

analogWrite(6, LOW); //右輪前進
analogWrite(7, carspeed);
delay(2000);

//右轉
analogWrite(4, LOW); //左輪前進
analogWrite(5, carspeed);

analogWrite(6, LOW); //右輪停止
analogWrite(7, LOW);
delay(2000);
break;
}

delay(200);

}

