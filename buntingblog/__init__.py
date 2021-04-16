from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskext.markdown import Markdown
from flask_simplemde import SimpleMDE


app = Flask(__name__)
app.config['SECRET_KEY'] = '2f7a976b465ddfdb5fc50fb8cb1c6079' #hex generated using cmd
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info' #bootstrap makes things pretty :)
markdown = Markdown(app)

from buntingblog import routes
from buntingblog.errors.eHandlers import errors

app.register_blueprint(errors)


