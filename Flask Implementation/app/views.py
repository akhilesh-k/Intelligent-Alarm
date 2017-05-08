from flask import render_template,Flask, request,flash, redirect, url_for,session
import serial
import string
from app import app, db
from app.models import *
import datetime 
import os,time
from itertools import cycle
import RPi.GPIO as GPIO
from gpiozero import Buzzer
GPIO.setmode(GPIO.BOARD)
but1=15
but2=16
but3=22
but4=19
led1=10
led2=11
led3=12
led4=13
#buz=Buzzer(40)
#freq=100;


GPIO.setup(int(but1),GPIO.IN)
GPIO.setup(int(but2),GPIO.IN)
GPIO.setup(int(but3),GPIO.IN)
GPIO.setup(int(but4),GPIO.IN)
GPIO.setup(int(led1),GPIO.OUT)
GPIO.setup(int(led2),GPIO.OUT)
GPIO.setup(int(led3),GPIO.OUT)
GPIO.setup(int(led4),GPIO.OUT)
#GPIO.setup(
@app.route('/' )
def index():
        return render_template('alarm.html',a=None)
   

@app.route('/link',methods=["POST"])
def da():
	print request.form
	time=request.form['usr_time']
    	everyday=request.form['freq1']
	db.session.add(Alarm(time,everyday))
	db.session.commit()
        se=Alarm.query.all()
	a=None
        for i in se:
		if(a==None):
			a=i.time
		else:		
			if(a>i.time):
				a=i.time 
        return render_template('alarm.html',a=a)
@app.route('/asd')
def asd():
    print 'asddddddddddddddddddddddddddddddddddddddd\nasddddddddddddddddd\nasdasd'
    GPIO.output(led1,GPIO.HIGH)
    print '\n\nasdasd'	
    #buz.on()
    while(1):
		a=GPIO.input(but1) 
		print a
		if(a==1):
			print "Led1", GPIO.input(led1)
			GPIO.output(led1,FALSE)
			break
    GPIO.output(led2,GPIO.HIGH)#digitalWrite(led2,HIGH);
    while(1):
		b=GPIO.input(but2) 
		if(b==1):
			GPIO.output(led2,FALSE)
			break
    
    GPIO.output(led3,GPIO.HIGH)#digitalWrite(led3,HIGH);
    while(1):
		c=GPIO.input(but3) 
		if(c==1):
			GPIO.output(led3,FALSE)
			break
    
    GPIO.output(led4,GPIO.HIGH)#digitalWrite(led3,HIGH);
    while(1):
		d=GPIO.input(but4) 
		if(d==1):
			GPIO.output(led4,FALSE)
			break

    #buz.off()
    return 'asd'
