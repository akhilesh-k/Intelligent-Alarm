from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#Create an Instance of Flask
app = Flask(__name__)
#Include config from config.py
app.config.from_object('config')
app.secret_key = '\xff}M\xac\xbd#4F\xab\xcc.\x9b\xf3\xa7\xf8\x80x`Yu'
#Create an instance of SQLAclhemy
db = SQLAlchemy(app)
from app import views, models
