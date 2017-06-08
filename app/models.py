from app import db
class Alarm(db.Model):
	__tablename__="time"	
	id=db.Column(db.Integer,primary_key=True)
	time=db.Column(db.DateTime,nullable=False)
	everyday=db.Column(db.Integer,nullable=False)
	def __init__(self, time,everyday):
		self.time = time
		self.everyday =everyday
