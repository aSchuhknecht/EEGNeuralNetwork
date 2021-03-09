

#include <SPI.h>

// Including the required Arduino libraries
#include <MD_Parola.h>
#include <MD_MAX72xx.h>
#include <SPI.h>


#define HARDWARE_TYPE MD_MAX72XX::GENERIC_HW
#define MAX_DEVICES 1
#define CS_PIN 5

// Create a new instance of the MD_MAX72XX class:
//MD_Parola myDisplay = MD_Parola(HARDWARE_TYPE, CS_PIN, MAX_DEVICES);

// For software SPI you also need to specify the DATA_PIN and the CLK_PIN connections:
 #define DATA_PIN 23
 #define CLK_PIN 18

// Create a new instance of the MD_MAX72XX class:
MD_Parola myDisplay = MD_Parola(HARDWARE_TYPE, DATA_PIN, CLK_PIN, CS_PIN, MAX_DEVICES);


//int incomingByte = 0 ;
String incomingByte ;        

void setup() {
  // Intialize the object
  myDisplay.begin();

  // Set the intensity (brightness) of the display (0-15)
  myDisplay.setIntensity(3);

  // Clear the display
  myDisplay.displayClear();

  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps

  Serial.println("Ready"); // print "Ready" once

}


void loop() {

  if (Serial.available() > 0) {

    incomingByte = Serial.readStringUntil('\n');

    if (incomingByte == "on") {

      myDisplay.setInvert(false);
      myDisplay.print(1);
     // Serial.write("Led on");

    }

    else if (incomingByte == "off") {

      myDisplay.setInvert(false);
      myDisplay.print(0);

     // Serial.write("Led off");

    }

    else{
     myDisplay.setInvert(false);
     myDisplay.print(0);
     //Serial.write("invald input");

    }

  }

 
  
}












  
//  if (Serial.available() > 0) {
//      Serial.print(Serial.read());
//      myDisplay.setInvert(false);
//      myDisplay.print(1);
//      
//    }
//
//    else {
//      myDisplay.setInvert(false);
//      myDisplay.print(0);
//    }
     
//      myDisplay.print(1);
//      delay(1000);
//      myDisplay.print(1);
//      delay(1000);
//      myDisplay.print(2);
//      delay(1000);
//      myDisplay.print(3);
//      delay(1000);
//      myDisplay.print(4);
//      delay(1000);
//      myDisplay.print(5);
//      delay(1000);
//      myDisplay.print(6);
//      delay(1000);
//      myDisplay.print(7);
//      delay(1000);
//      myDisplay.print(8);
//      delay(1000);
//      myDisplay.print(9);
//      delay(1000);

//    incomingByte = Serial.read();
//    
//  if (Serial.available() > 0) {
//  if (incomingByte == 1) {
//
//      digitalWrite(LED_BUILTIN, HIGH);
//
//      Serial.write("Led on");
//      myDisplay.setInvert(false);
//      myDisplay.print(1);
//      
//    }
//
//    else if (incomingByte == 0) {
//
//      digitalWrite(LED_BUILTIN, LOW);
//
//      Serial.write("Led off");
//      
//      myDisplay.setInvert(false);
//      myDisplay.print(0);
//
//    }
//
//    else{
//
//     Serial.write("invald input");
//     myDisplay.setInvert(false);
//     myDisplay.print("n");
//
//    }
//}
//
//
//else{
//
//     Serial.write("invald input");
//     myDisplay.setInvert(false);
//     myDisplay.print(" L ");
//
//    }
