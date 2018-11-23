from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usn = db.Column(db.String(64), index=True,unique=True)
    sem = db.Column(db.String(120), index=True)
    interets = db.Column(db.Text,index=True)
    cgpa = db.Column(db.Float,index=True)
    def __repr__(self):
        return '<User {}>'.format(self.username) 

class Elective(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	electiveNo = db.Column(db.Integer)
	courseName = db.Column(db.String(100),index = True)
	description = db.Column(db.Text,index = True)
	teacher = db.Column(db.String(30),index = True)
	specialization = db.Column(db.String(30),index=True)
	prerequisites = db.Column(db.String(30),index = True)

	def __repr__(self):
		return '<Elective {}>'.format(self.courseName)



