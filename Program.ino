#define led1 2
#define led2 4
#define led3 8
#define led4 8
#define led5 12

void setup() {
  Serial.begin(9600); // Initialize serial communication at 9600 bits per second
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  Serial.println("Setup complete.");
  delay(5000); // Delay for 5 seconds to allow for serial monitor checks
}

void loop() {
  if (Serial.available() > 0) {
    String msg = Serial.readString();
    Serial.print("Received message: ");
    Serial.println(msg);
    
    if (msg.startsWith("ZERO")|| msg.startsWith("0")){
      digitalWrite(led1, LOW);
      digitalWrite(led2, LOW);
      digitalWrite(led3, LOW);
      digitalWrite(led4, LOW);
      digitalWrite(led5, LOW);
      Serial.println("All LEDs off");
    }
    else if (msg.startsWith("ONE")) {
      digitalWrite(led1, HIGH);
      digitalWrite(led2, LOW);
      digitalWrite(led3, LOW);
      digitalWrite(led4, LOW);
      digitalWrite(led5, LOW);
      Serial.println("LED 1 on");
    }
    else if (msg.startsWith("TWO")) {
      digitalWrite(led1, HIGH);
      digitalWrite(led2, HIGH);
      digitalWrite(led3, LOW);
      digitalWrite(led4, LOW);
      digitalWrite(led5, LOW);
      Serial.println("LED 1 and 2 on");
    }
    else if (msg.startsWith("THREE")) {
      digitalWrite(led1, HIGH);
      digitalWrite(led2, HIGH);
      digitalWrite(led3, HIGH);
      digitalWrite(led4, LOW);
      digitalWrite(led5, LOW);
      Serial.println("LED 1, 2, and 3 on");
    }
    else if (msg.startsWith("FOUR")) {
      digitalWrite(led1, HIGH);
      digitalWrite(led2, HIGH);
      digitalWrite(led3, HIGH);
      digitalWrite(led4, HIGH);
      digitalWrite(led5, LOW);
      Serial.println("LED 1, 2, 3, and 4 on");
    }
    else if (msg.startsWith("5")) {
      digitalWrite(led1, HIGH);
      digitalWrite(led2, HIGH);
      digitalWrite(led3, HIGH);
      digitalWrite(led4, HIGH);
      digitalWrite(led5, HIGH);
      Serial.println("All LEDs on");
    }
     else {
      Serial.println("Unknown message");
    }
  }
  delay(1/24);
}