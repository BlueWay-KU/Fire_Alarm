#include <SoftwareSerial.h>
 
SoftwareSerial bluetooth(3,2); //TX, RX 연결

//analog input
int gasPin = A0 ;
int flamePin = A1;

//sensor vaue
int gas_val;
int flame_val;

void setup() {
  Serial.begin(9600);
  bluetooth.begin(9600);
}

void loop() {
  gas_val = analogRead(gasPin);
  flame_val = analogRead(flamePin);

  if(gas_val>100 | flame_val < 200){
    bluetooth.println("1");
  }

  else{
    bluetooth.println("0");
  }

  Serial.println(gas_val);
  Serial.println(flame_val);
  
  delay(1000);
}
