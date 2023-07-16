#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <Adafruit_MMA8451.h>
#include <Adafruit_Sensor.h>
#include <ArduinoLowPower.h>
int millithen = 0;
int millinow= 0;
Adafruit_MMA8451 mma = Adafruit_MMA8451();
File myFile;
int led = 7;
int csvno = 1;
void setup() {

  Serial.print("Starting Datalog");

  if (!SD.begin(SDCARD_SS_PIN)) {
    Serial.println("SD card failed");
    while (1);
  };
  Serial.println("SD done.");
  if (! mma.begin()) {
    Serial.println("Accelerometer failed");
    while (1);
  }

  myFile = SD.open(CSV , FILE_WRITE);
  if (myFile) {
    Serial.print("csv works");

  myFile.close();
  mma.setRange(MMA8451_RANGE_2_G);
}
  pinMode(led, OUTPUT);
}
void loop() {
  millinow = millis();
  if (millinow > millithen + 1000){
    digitalWrite(led ,HIGH);
    millithen = millis();
  }
  else{
    digitalWrite(led, LOW);
  }
  mma.read();
  myFile = SD.open(CSV , FILE_WRITE);
  sensors_event_t event; 
  mma.getEvent(&event);
  if (myFile) {    
    myFile.println(millis());
    myFile.print(",");
    myFile.print(event.acceleration.x);
    myFile.print(",");    
    myFile.print(event.acceleration.y);
    myFile.print(",");    
    myFile.print(event.acceleration.z);
    myFile.print(",");
    myFile.close();
  }
    Serial.println();
  delay(200);
}
