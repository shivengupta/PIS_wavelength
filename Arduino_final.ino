/*
* Ultrasonic Sensor HC-SR04 and Arduino Tutorial
*
* by Dejan Nedelkovski,
* www.HowToMechatronics.com
*
*/
// defines pins numbers
const int trigPin1 = A0;
const int echoPin1 = A1;

const int trigPin2 = A2;
const int echoPin2 = A3;

const int trigPin3 = 3;
const int echoPin3 = 11;

const int trigPin4 = 9;
const int echoPin4 = 10;


// defines variables
long duration;
long distance;
long s1,s2,s3,s4;

void setup() {
Serial.begin(9600);
pinMode(trigPin1, OUTPUT);
pinMode(echoPin1, INPUT);

pinMode(trigPin2, OUTPUT);
pinMode(echoPin2, INPUT);

pinMode(trigPin3, OUTPUT);
pinMode(echoPin3, INPUT);

pinMode(trigPin4, OUTPUT);
pinMode(echoPin4, INPUT);

}
// increase baud rate or use 2 arduinos
void loop() {
SonarSensor(trigPin1, echoPin1);
s1 = distance;
SonarSensor(trigPin2, echoPin2);
s2 = distance;
SonarSensor(trigPin3, echoPin3);
s3 = distance;
SonarSensor(trigPin4, echoPin4);
s4 = distance;

Serial.print(s1);
Serial.print(" ");
Serial.print(s2);
Serial.print(" ");
Serial.print(s3);
Serial.print(" ");
Serial.println(s4);
delay(100);
}

void SonarSensor(int trigPin,int echoPin)
{
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH);
distance = (duration/2)*0.0343;

}
