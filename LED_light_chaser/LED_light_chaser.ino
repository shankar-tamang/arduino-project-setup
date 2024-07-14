const int PinNum = 6;
int LedPin[PinNum] = {2, 3, 4, 5, 6, 7};

void setup(){
   for (int i = 0; i<= PinNum; i++){
    pinMode(LedPin[i], OUTPUT);
   }
}


void loop(){
  for (int i = 0; i<= PinNum - 1; i++){
    digitalWrite(LedPin[i], HIGH);
    delay(100);
    digitalWrite(LedPin[i], LOW);
    
  }
}
