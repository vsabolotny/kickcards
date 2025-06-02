from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

from .. import db # Import the db instance from app/__init__.py

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'