from app import app, db, models
from flask import render_template, flash
from .forms import LoginForm


@app.route('/', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if user: 
			if user.password == form.password.data:
				user.authenticated = True
				db.session.add(user)
				db.session.commit()
				login_user(user, remember = True);                                                                                                                        
		flask.flash('Logged in successfully')
		

	return render_template("login.html", form=form)

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
	form = LoginForm()
	return render_template("signUp.html", form=form)
	newUser = models.User(username = form.username.data, password = form.password.data)
	db.session.add(newUser)
	db.session.commit()

@app.route('/home')
def home():
	return render_template("base.html")

@login_manager.user_loader
def load_user(user_id):
	return models.User.query.get(user_id)