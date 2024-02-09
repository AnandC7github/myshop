from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
db = SQLAlchemy(app)

#  Import routes at the end to avoid circular imports
from shop import routes
