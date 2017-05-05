import flask
import datetime
from app import db
import requests
from app.models import *
a=None
while(1):	
    a=Alarm.query.all()
    for i in a:
        b=datetime.datetime.now()
	if(i.time.date()==b.date()):
		print 'asdasd chala oi'
		requests.get('http://0.0.0.0:80/asd')
		print 'asdasd'
		db.session.delete(i)
		db.session.commit()
				
