/* 
 *  This sketch run on arduino and is doing data batch through serial port
 */
int outputs[4] = {6,7,8}; // pins for selecting LED
int inputs[4] = {5,4,3}; // pins for selecting diode
int io_pin_diode = A0;
int inhib_diode = 2;
int io_pin = 11; // pin used for sending power to LEDs
int inhibit_pin = 10; // pin for turning off all LEDs
float diodes_values[9];
int capture_time = 1000; // capture time in milliseconds Warning: might overflow if capture time is too much 1000 seems just fine
int response_array[9][50]; 
int line_to_write = 0;
unsigned long start_time;
unsigned long loop_timer;
void setup() {
  Serial.begin(9600);
  for(int ii;ii<3;ii++){
    pinMode(outputs[ii],OUTPUT); // output selection for LED control
  }


  for(int jj;jj<3;jj++){
    pinMode(inputs[jj],OUTPUT); // input selection for diode control
  }

  pinMode(inhibit_pin,OUTPUT); 
  digitalWrite(inhibit_pin,LOW); // raise high to disable all
  pinMode(inhib_diode,OUTPUT); 
  digitalWrite(inhib_diode,LOW); // raise high to disable all
  pinMode(io_pin,OUTPUT); // this controls the power sent to each LED
  digitalWrite(io_pin,HIGH); // send high to all LEDs when powered on
  pinMode(io_pin_diode,INPUT); // input of selected diode
  start_time = millis();
  line_to_write = 0;

}

void loop() {
  loop_timer = millis();
  if (loop_timer<start_time+capture_time){
    digitalWrite(inhibit_pin,LOW); // turn on led
    // looping through all 8 LEDs
    for (int jj=0;jj<8;jj++){
      // turn on LEDs based on bit conversion
      for(int ii=0;ii<3;ii++){
        digitalWrite(outputs[ii],bitRead(jj,ii));
      }
      delay(10);
      // looping through all 8 diodes
      for (int kk=0;kk<8;kk++){
        // turn on diodes based on bit conversion
        for(int ll=0;ll<3;ll++){
          digitalWrite(inputs[ll],bitRead(kk,ll));
        }
        response_array[kk][line_to_write] = analogRead(A0);
      }
        line_to_write++;
    }
    digitalWrite(inhibit_pin,HIGH); // turn off led
    //delay(10);
  }
  else{
    Serial.print("IR_startflag");
    for(int i=0;i<line_to_write;i++){
      Serial.print("A: "); Serial.print(response_array[0][i]); Serial.print("  ");
      Serial.print("B: "); Serial.print(response_array[1][i]); Serial.print("  ");
      Serial.print("C: "); Serial.print(response_array[2][i]); Serial.print("  ");
      Serial.print("D: "); Serial.print(response_array[3][i]); Serial.print("  ");
      Serial.print("E: "); Serial.print(response_array[4][i]); Serial.print("  ");
      Serial.print("F: "); Serial.print(response_array[5][i]); Serial.print("  ");
      Serial.print("G: "); Serial.print(response_array[6][i]); Serial.print("  ");
      Serial.print("H: "); Serial.print(response_array[7][i]); Serial.print("  ");
      Serial.println("uT");
    }
    Serial.print("IR_endflag");
    start_time = millis();
    line_to_write = 0;

  }
}
