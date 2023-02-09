from app import app
from flask_sqlalchemy import SQLAlchemy
import pymysql

app.config['SECRET_KEY'] = "Rodrigue"
app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root:rodrigue@localhost/rodrigue"

db = SQLAlchemy(app)