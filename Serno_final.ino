#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <Servo.h>
Servo myservo;// crea el objeto servo
Servo myservos;
int pos = 0, con = 0, c=0, d=0, gra,grad;    // posicion del servo
const int IZQ=D1;
const int DER=D2;
int val, vel, a=0,b=0,seri=0, sera=0, cont=0;
String interruptora="", interruptorb="", est="";
//////////////////////////////////////////////
String server = "";

const char *ssid = "Mon";
const char *password = "12345678i";
//////////////////////////////////////////////

void setup() {
  pinMode(IZQ,INPUT);
  pinMode(DER,INPUT);
  myservo.attach(D3);  // vincula el servo al pin digital 9
  myservos.attach(D4);  // vincula el servo al pin digital 9
Serial.begin(9600);
/////////////////////////////////////////////////////////////////////
Serial.println("WiFi connected");
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
////////////////////////////////////////////////////////////////////////////////
}

void loop()
{
val=digitalRead(IZQ);
vel=digitalRead(DER);
seri = myservo.read();
sera = myservos.read();
cont = cont + 1;

if (cont == 1){
c = 0;
myservo.write(c);
interruptora = "Servo1:";
gra = seri;
myservos.write(180 - c);
interruptorb = "Servo2:";
grad = sera;
delay(50); 
}
else if (cont > 1 and cont <=180){
c = c + 1;
myservo.write(c);
interruptora = "Servo1:";
gra = seri;
myservos.write(180 - c);
interruptorb = "Servo2:";
grad = sera;
delay(50); 
}else if (cont >= 181 and cont <= 360){
c = c - 1;
myservo.write(c);
interruptora = "Servo1:";
gra = seri;
myservos.write(180-c);
interruptorb = "Servo2:";
grad = sera;
delay(50); 
if(cont==360){
  cont = cont *0;
}
}

  if (WiFi.status() == WL_CONNECTED)
  { //Check WiFi connection status

    HTTPClient http;                                                                                  
    http.begin("http://144.202.34.148:3340/interruptores");

if (val==HIGH){
  a=a+1;
  b=0;
  con = 0;
  if(a==1){
    Serial.println(interruptora);
    Serial.println(gra);
    Serial.println(interruptorb);    
    Serial.println(grad);
    post(interruptora, gra, interruptorb, grad);
  }
}
else if (vel==HIGH){
  b=b+1;
  a=0;
  con = 180;
  if(b==1){
    Serial.println(interruptora);
    Serial.println(gra);
    Serial.println(interruptorb);    
    Serial.println(grad);
    post(interruptora, gra, interruptorb, grad);
  }
}
/////////////////////////////////////////////////////////////////////////
  }
}

//////////////////////////////////////////////////////////////////////
void post(String interruptora, int gra, String interruptorb, int grad) {
  Serial.println("Inicio post");
  HTTPClient http;
  String json;
  server = ("http://144.202.34.148:3340/interruptores");


  StaticJsonDocument<256> doc;
  doc["interruptora"] = String(interruptora);
  doc["gra"] = int(gra);
  doc["interruptorb"] = String(interruptorb);
  doc["grad"] = int(grad);
  serializeJson(doc, json);


  
  http.begin(server);
  http.addHeader("Content-Type", "application/json");
  http.POST(json);
  http.writeToStream(&Serial);
  http.end();
  Serial.println("Termino post");
}
