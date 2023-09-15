import admin
import model
import norm

from flask import Flask
from flask_bootstrap import Bootstrap4


nr = norm
asdmin = admin
db = model


app = Flask(__name__)
app.config['TITLE'] = "Normas Compiladas"
app.secret_key = b'guerra aos senhores'


admin.configure(app)
nr.configure(app)
db.configure(app)
Bootstrap4(app)