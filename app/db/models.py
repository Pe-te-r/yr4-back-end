from flask_sqlalchemy import SQLAlchemy
import uuid
from enum import Enum


db = SQLAlchemy()

class IDType(Enum):
    KENYAN_CITIZEN = "Kenyan Citizen"
    FOREIGN_CITIZEN = "Foreign Citizen"
    REFUGEE = "Refugee"
    MANDATE = "Mandate"
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    firstname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contact = db.Column(db.String(15), nullable=False)
    id_type = db.Column(db.Enum(IDType), nullable=False)  # Use Enum for id_type
    id_number = db.Column(db.String(50), unique=True, nullable=False)
    role=db.Column(db.String(8),nullable=False,default='user')

    # One-to-one relationship with Code
    code = db.relationship('Code', backref='user', uselist=False, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User {self.firstname}>'


class Code(db.Model):
    __tablename__ = 'codes'
    user_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('users.id'), primary_key=True)
    code = db.Column(db.String(4), nullable=False)

    def __repr__(self):
        return f'<Code {self.code}>'
