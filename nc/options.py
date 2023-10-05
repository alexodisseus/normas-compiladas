import app
import model


from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


options = Blueprint('options' , __name__ , url_prefix='/options/')



@options.route('/', methods = ['GET','POST'])
def index():

	if 'username' not in session:
		return redirect(url_for('admin.login'))

	return 'opções' 

@options.route('user/', methods = ['GET','POST'])
def user():

	if 'username' not in session:
		return redirect(url_for('admin.login'))

	return '<h1>asd</h1>' 




def configure(app):
	app.register_blueprint(options)