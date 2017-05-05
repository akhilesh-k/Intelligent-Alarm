import RPi.GPIO as GPIO
import os
from gpiozero import Buzzer
from time import sleep
from flask import Flask,render_template.url_for,request
GPIO.setmode(GPIO.BCM)
but1=15
but2=16
but3=22
but4=19
led1=10
led2=11
led3=12
led4=13
buz=Buzzer(40)
GPIO.setup(int(buz),GPIO.OUT)
GPIO.setup(int(but1),GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(int(but2),GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(int(but3),GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(int(but4),GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(int(led1),GPIO.OUT)
GPIO.setup(int(led2),GPIO.OUT)
GPIO.setup(int(led3),GPIO.OUT)
GPIO.setup(int(led4),GPIO.OUT)
#GPIO.setup(
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('main.html')#Return the main.html template to the web browser using the variables in the templateData dictionary
@app.route('/link',methods=["POST"])
def da():
    hours=request.form['hours']
    #minutes=request.form['mins']
    #add to database
    ##compare
    return ##reversewatch 
@app.route('/asd')
def asd():
    GPIO.output(led1,GPIO.HIGH)
     buz.on()
    while(1):
    a=GPIO.Input(but1) 
    print a
    if(a==1):
      GPIO.output(led1,FALSE)
      break
  #---------------
  GPIO.output(led2,GPIO.HIGH)#digitalWrite(led2,HIGH);
  while(1):
      b=GPIO.Input(but2) 
      if(b==1):
          GPIO.output(led2,FALSE)
          break
    
  GPIO.output(led3,GPIO.HIGH)#digitalWrite(led3,HIGH);
  while(1):
    c=GPIO.Input(but3) 
    if(c==1):
      GPIO.output(led3,FALSE)
      break
    
  GPIO.output(led4,GPIO.HIGH)#digitalWrite(led3,HIGH);
  while(1):
    d=GPIO.Input(but4) 
    if(d==1):
      GPIO.output(led4,FALSE)
      break

  buz.off()
  return #render_remplate(awqe)

@app.route('/')
def index():
    return render_template('index.html')# Flask will look for index.html template in the templates folder, and render it.

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=TRUE)
