int trig = 10; // attach pin 10 to Trig
int echo = 11; //attach pin 1158 to Echo

const int ledPin = 13;

const int f = 2;                 
const int b = 3;                 
const int l = 4;                 
const int r = 5;                 

const int motorL0 = 6;                 //Left Motor 1
const int motorL1 = 7;                 //Left Motor 2
const int motorR0 = 8;                 //Right Motor 1
const int motorR1 = 9;                 //Right Motor 2

void setup() {

  pinMode(f, INPUT);
  pinMode(b, INPUT);
  pinMode(l, INPUT);
  pinMode(r, INPUT);
  
  pinMode(motorL0, OUTPUT);
  pinMode(motorL1, OUTPUT);
  pinMode(motorR0, OUTPUT);
  pinMode(motorR1, OUTPUT);
  
  pinMode(ledPin, OUTPUT);
  
// initialize serial communication:
Serial.begin(9600);

}

void loop()
{
// establish variables for duration of the ping,
// and the distance result in inches and centimeters:
long duration, inches, cm;

// The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
// Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
pinMode(trig, OUTPUT);
digitalWrite(trig, LOW);
delayMicroseconds(2);
digitalWrite(trig, HIGH);
delayMicroseconds(5);
digitalWrite(trig, LOW);


pinMode(echo,INPUT);
duration = pulseIn(echo, HIGH);

// convert the time into a distance
inches = microsecondsToInches(duration);
cm = microsecondsToCentimeters(duration);

Serial.print(inches);
Serial.print("in, ");
Serial.print(cm);
Serial.print("cm");
Serial.println();

delay(100);

boolean fwd = digitalRead(f);
boolean back = digitalRead(b);
boolean left = digitalRead(l);
boolean right = digitalRead(r);

 if (cm > 12) {
    
    digitalWrite(ledPin, LOW);
    
    if (fwd == HIGH)
    {
    digitalWrite(motorL0, HIGH);
    digitalWrite(motorL1, LOW);
    digitalWrite(motorR0, HIGH);
    digitalWrite(motorR1, LOW);
    }
    
    if (back == HIGH)
    {
    digitalWrite(motorL0, LOW);
    digitalWrite(motorL1, HIGH);
    digitalWrite(motorR0, LOW);
    digitalWrite(motorR1, HIGH);
    }
    
    if (left == HIGH)
    {
    digitalWrite(motorL0, HIGH);
    digitalWrite(motorL1, LOW);
    digitalWrite(motorR0, LOW);
    digitalWrite(motorR1, HIGH);
    }
    
    if (right == HIGH)
    {
    digitalWrite(motorL0, LOW);
    digitalWrite(motorL1, HIGH);
    digitalWrite(motorR0, HIGH);
    digitalWrite(motorR1, LOW);
    }
    
    if (fwd == LOW && back == LOW && left == LOW && right == LOW)
    {
    digitalWrite(motorL0, LOW);
    digitalWrite(motorL1, LOW);
    digitalWrite(motorR0, LOW);
    digitalWrite(motorR1, LOW);
  }
    
  }
  else {
    digitalWrite(ledPin, HIGH);
  
      if (back == HIGH)
    {
    digitalWrite(motorL0, LOW);
    digitalWrite(motorL1, HIGH);
    digitalWrite(motorR0, LOW);
    digitalWrite(motorR1, HIGH);
    }
    
    if (left == HIGH)
    {
    digitalWrite(motorL0, HIGH);
    digitalWrite(motorL1, LOW);
    digitalWrite(motorR0, LOW);
    digitalWrite(motorR1, HIGH);
    }
    
    if (right == HIGH)
    {
    digitalWrite(motorL0, LOW);
    digitalWrite(motorL1, HIGH);
    digitalWrite(motorR0, HIGH);
    digitalWrite(motorR1, LOW);
    }
    
    if (back == LOW && left == LOW && right == LOW)
    {
    digitalWrite(motorL0, LOW);
    digitalWrite(motorL1, LOW);
    digitalWrite(motorR0, LOW);
    digitalWrite(motorR1, LOW);
  }
}
}

long microsecondsToInches(long microseconds)
{
return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds)
{
return microseconds / 29 / 2;
}

