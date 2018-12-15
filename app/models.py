from app import db

class Book(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	author = db.Column(db.String(100))
	yearOfPublication = db.Column(db.String(100))
	dateRead = db.Column(db.DateTime)
	bookList = db.Column(db.Integer)

class User(db.Model):
	username = db.Column(db.String(100), primary_key = True)
	password = db.Column(db.String(100)) 
	authenticated = db.Column(db.Boolean, default = False)

	def is_active(self):
		return True

	def get_id(self):
		return self.username

	def is_authenticated(self):
		return self.authenticated

	def is_anonymous(self):
		return False