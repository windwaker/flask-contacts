from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
url = "postgresql://postgres:avocado@192.168.0.101:5432/contacts"
app.config["SQLALCHEMY_DATABASE_URI"] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Contact(db.Model):

    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(80), nullable=False, unique=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(200), nullable=True)
    phone = db.Column(db.String(20), nullable=True, unique=False)

    def __repr__(self):
        return "<Contacts %r>" % self.name


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.String(15), nullable=False)
    to = db.Column(db.String(80), nullable=False)
    text = db.Column(db.String(150), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
