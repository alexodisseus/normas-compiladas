from typing import Optional, List
from sqlmodel import SQLModel , Field, create_engine, Session, select, Relationship


db = SQLModel()

def configure(app):
    app.db = db



class Person(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	name:str
	password:str
	todos:List['Todo']=Relationship()



class Todo(SQLModel, table=True):
	"""docstring for Todo"""
	id: Optional[int] = Field(default=None, primary_key=True)
	title: str
	status: str = "todo"
	person_id: int = Field(foreign_key='person.id')
	"""
	def __init__(self, arg):
		super(Todo, self).__init__()
		self.arg = arg
	"""



class Norm_iten(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	iten:str
	sub_iten:str = Field(default=None)
	title:str = Field(default=None)
	tag:str
	description:str = Field(default=None)
	types:str

"""
class Norm_iten_sub(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	iten_sub:str
	
	tag:str
	norm_iten_id: int = Field(foreign_key='norm_iten.id')
"""



class To_apply(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	name:str
	norm_iten_id: int = Field(foreign_key='norm_iten.id')
	person_id: int = Field(foreign_key='person.id')



engine = create_engine('sqlite:///db.db')

SQLModel.metadata.create_all(engine)


def relaciotion():

	with Session(engine) as session:
		query = select(Person).where(Person.id == 1 )
		result = session.exec(query).first()

		print(result.name)

		print(result.name, result.todos)


#relaciotion()



def create_user(name:str, password:str):
	with Session(engine) as session:
		session.add(Person(name=name,password=password))
		session.commit()


def create_tasks(title:str, status:str = 'todo',user:str = 1 ):
	with Session(engine) as session:
		session.add(Todo(title=title, status=status, person_id=user))
		session.commit()

def read_tasks(person_id:int):
	with Session(engine) as session:
		person=session.get(Person, person_id)
		return person.todos


def read_tasks_view(task_id:int):
	with Session(engine) as session:
		query= select(Todo).where(Todo.id == task_id)
		data = session.exec(query).first()
		return data

def update_tasks(task_id:int, task_title:str =None, task_status:str=None):
	with Session(engine) as session:
		task = session.get(Todo, task_id)
		if task_title:
			task.title = task_title
		if task_status:
			task.status = task_status
		session.commit()

def delete_tasks(task_id:int,):
	with Session(engine) as session:
		task=session.get(Todo, task_id)
		session.delete(task)
		session.commit()


def read_user(name:str,password:str):
	with Session(engine) as session:

		query= select(Person).where(Person.name == name).where(Person.password == password)

		data = session.exec(query).first()
		return data






#model para norm
def read_norm_list(description:str=None , tags:str=None):
	with Session(engine) as session:
		query= select(Norm_iten)
		if description:
			query = query.where( Norm_iten.description.contains(description))
		if tags != []:
			for x in tags:
				query = query.where( Norm_iten.tag == x)

		data = session.exec(query).all()
		return data


def read_norm_list_ids():
	with Session(engine) as session:
		query= select(
			Norm_iten.iten,
			Norm_iten.title, 
			Norm_iten.id).where(
			Norm_iten.sub_iten ==None
			)
		
		data = session.exec(query).all()
		return data
		
def read_norm_view(id:str):
	with Session(engine) as session:
		query= select(Norm_iten).where(Norm_iten.id == id)
		

		data = session.exec(query).all()
		return data


def read_norm_iten_view(iten:str):
	with Session(engine) as session:
		query= select(Norm_iten).where(Norm_iten.iten == iten)
		
		data = session.exec(query).all()
		return data

def read_norm_iten_sub_view(id:str):
	with Session(engine) as session:
		query= select(Norm_iten).where(Norm_iten.id == id)
		
		data = session.exec(query).first()
		return data

		

def create_norm_iten(iten:str, title:str, types:str , tag:str ):
	with Session(engine) as session:
		session.add(Norm_iten(iten = iten, title=title ,types=types,  tag=tag ))
		session.commit()


def create_norm_iten_sub(iten:str,sub_iten:str, tag:str,types:str, description:str ):
	with Session(engine) as session:
		session.add(Norm_iten(iten = iten,sub_iten=sub_iten, tag=tag,types=types, description=description ))
		session.commit()



