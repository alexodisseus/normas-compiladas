import app
import model

from flask import Blueprint, render_template, current_app , request , session, redirect, url_for

norm = Blueprint('norm' , __name__ , url_prefix='/norm/')


@norm.route('/', methods = ['GET'])
def index():

	if 'username' not in session:
		return redirect(url_for('admin.login'))

	# fazer a busca das tags
	# colocar a tag na busca da lista
	# fazer

	busca = request.args.get('busca', '')
	tags = request.args.getlist('tags')
	page = request.args.get('page')
	
	
	data = model.read_norm_list(busca , tags , page)

	pagination = []
	item = []
	for x in data:
		if x[1] in item:
			pass
		else:
			item.append(x[1])
	

	return render_template('norm/list.html' , 
		data = data , 
		item=item , 
		pagination = pagination)




@norm.route('/create_iten/', methods = ['GET','POST'])
def create_iten():
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	if request.method == 'POST':
		iten = request.form['iten']
		tag = request.form['tag']
		title = request.form['title']
		types = "titulo"


		model.create_norm_iten(iten,title , types,tag)
		return redirect(url_for('norm.index'))

	return render_template('norm/create_iten.html')




@norm.route('/create_iten_sub/', methods = ['GET','POST'])
def create_iten_sub():
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	if request.method == 'POST':
		iten = request.form['iten']
		iten_sub = request.form['iten_sub']
		tag = request.form['tag']
		
		description = request.form['description']
		print('asdasdasdasd')
		print(iten)
		print(iten_sub)

		model.create_norm_iten_sub(iten,iten_sub,tag,description)

		return redirect(url_for('norm.index'))
	
	data = model.read_norm_list_ids()

	return render_template('norm/create_iten_sub.html' , data = data)

@norm.route('/add_apply/<id>', methods = ['GET','POST'])
def add_apply(id):
	
	print(id)

	if 'username' not in session:
		return redirect(url_for('admin.login'))

	if request.method == 'POST':

		norm_id = request.form['id']
		

		model.add_apply()
		return redirect(url_for('norm.view_iten_sub', id=norm_id))
	
	data = model.read_norm_list_ids()
	return render_template('norm/add_apply.html' , data=data)


@norm.route('/view/<id>', methods = ['GET','POST'])
def view(id):
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	data = model.read_norm_iten_view(id)
	
	return render_template('norm/view.html' , data=data)

@norm.route('/view_iten_sub/<id>', methods = ['GET','POST'])
def view_iten_sub(id):
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	data = model.read_norm_iten_sub_view(id)
	
	return render_template('norm/view_iten_sub.html' , data=data)





"""
@admin.route('/login', methods = ['GET','POST'])
def login():
	if request.method == 'POST':

		name = request.form['name']
		password = request.form['password']
		data = model.read_user(name,password)

		if data:

			session['username'] = data.name
			session['userid'] = data.id
			print(session)
			return redirect(url_for('admin.index'))

		return render_template('login.html' )


	return render_template('login.html' )



@admin.route('/admis', methods = ['GET','POST'])
def admis():
	if 'username' not in session:
		return redirect(url_for('admin.login'))
	return render_template('login.html')


@admin.route('/view/<id>', methods = ['GET','POST'])
def view(id):
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	data = model.read_tasks_view(id)
	#sai da sessao se o usuario estiver errado
	if data.person_id != session['userid']:
		return redirect(url_for('admin.login'))

	return render_template('view.html' , data=data)


@admin.route('/create/', methods = ['GET','POST'])

def create():
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	if request.method == 'POST':
		user = request.form['name']
		password = request.form['password']

		model.create_user(user,password)
		return redirect(url_for('admin.login'))

	return render_template('create.html')





@admin.route('/create_task/', methods = ['GET','POST'])
def create_task():

	if request.method == 'POST':
		title = request.form['title']
		status = request.form['status']

		model.create_tasks(title,status , session['userid'])
		return redirect(url_for('admin.index'))

	return render_template('create_task.html')


@admin.route('/logout', methods = ['GET','POST'])
def logout():

	session.pop('username', None)
	return redirect(url_for('admin.login'))

"""

def configure(app):
	app.register_blueprint(norm)

	