
int ledValue = 1;
int sensorValue;
int led = 13;
int alcIn = 1;

void setup()
{
  Serial.begin(9600);
  pinMode(led, OUTPUT); 
}

void loop()
{
  ledValue = (ledValue + 1) % 2;
  Serial.println(ledValue, DEC);
  digitalWrite(led, ledValue);
  sensorValue = analogRead(alcIn);
  Serial.println(sensorValue, DEC);
  delay(500);
}
