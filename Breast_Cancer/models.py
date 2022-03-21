from enum import unique
from pickle import TRUE
from . import db
from flask_login import UserMixin

# Create your db here.

class Doctor(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),unique=True)
    email=db.Column(db.String(60),unique=True)
    password=db.Column(db.String(20))
    def __repr__(self) -> str:
        return '<Doctor %r>' % self.username