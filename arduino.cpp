#include <SoftwareSerial.h>

SoftwareSerial BTSerial(2, 3); // RX, TX 

const int touch = 2; // button A pin 2
const int boton| = 3; // button B pin 3
//nota: cortocircutamos el puente B para el comportmaiento de boton en el touch TTP223 
void setup() {
  pinMode(touch, INPUT_PULLUP); // button A entrada con pull-up
  pinMode(boton|, INPUT_PULLUP); // button B entrada con pull-up
  
  // start bluthot module jejej
  BTSerial.begin(9600);
}

void loop() {
  // Si se presiona el botón A, enviar "A" por Bluetooth
  if (digitalRead(touch) == LOW) {
    BTSerial.write('A');
    delay(100); // Debounce
  }

  // Si se presiona el botón B, enviar "B" por Bluetooth
  if (digitalRead(boton|) == LOW) {
    BTSerial.write('B');
    delay(100); // Debounce
  }
}
