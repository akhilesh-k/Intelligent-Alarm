int but1=A0;
int but2=A1;
int but3=A2;
int but4=A3;
int led1=10;
int led2=11;
int led3=12;
int led4=13;
int buz=8;
int freq=100;
void setup()
{
  pinMode(buz,OUTPUT);
  pinMode(but1,INPUT);
  pinMode(but2,INPUT);
  pinMode(but3,INPUT);
  pinMode(but4,INPUT);
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  pinMode(led3,OUTPUT);
  pinMode(led4,OUTPUT);
  Serial.begin(9600);
}
void loop()
{
  int a,b,c,d;
  digitalWrite(led1,HIGH);
  while(1)
  {
    a=analogRead(but1);
    tone(buz,freq);
    Serial.println(a);
    if(a>100)
    {
      digitalWrite(led1,LOW);
      break;
    }
  }
  digitalWrite(led2,HIGH);
  while(1)
  {
    b=analogRead(but2);
    tone(buz,freq);
    Serial.println(b);
    if(b>100)
    {
      digitalWrite(led2,LOW);
      break;
    }
  }
  digitalWrite(led3,HIGH);
  while(1)
  {
    c=analogRead(but3);
    tone(buz,freq);
    Serial.println(c);
    if(c>100)
    {
      digitalWrite(led3,LOW);
      break;
    }
  }
  digitalWrite(led4,HIGH);
  while(1)
  {
    d=analogRead(but4);
    tone(buz,freq);
    Serial.println(d);
    if(d>100)
    {
      digitalWrite(led4,LOW);
      break;
    }
  }
  noTone(buz);
  delay(5000);
}

