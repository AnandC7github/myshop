from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
app.config['SECRET_KEY'] = 'jwkhfciuewhfwzf323f3'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#  Import routes at the end to avoid circular imports
from shop import routes
