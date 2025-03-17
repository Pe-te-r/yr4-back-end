from flask_sqlalchemy import SQLAlchemy
import uuid
from enum import Enum


db = SQLAlchemy()
class Role(Enum):
    USER = "user"
    ADMIN = "admin"

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
    role = db.Column(db.Enum(Role), nullable=False, default=Role.USER) 
    # One-to-one relationship with Code
    code = db.relationship('Code', backref='user', uselist=False, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User {self.firstname}>'
    
    def to_json(self):
        return {
            'id':str(self.id),
            'email':self.email,
            'contact':self.contact,
            'id_type':self.id_type.value,
            'id_number':self.id_number,
            'firstname':self.firstname,
        }
        
    @classmethod
    def get_by_id(cls,id):
        try:
            # Convert the input ID to a UUID object
            user_id = uuid.UUID(id)
        except ValueError:
            # Handle invalid UUID format
            print(f"Invalid UUID format: {id}")
            return None
        try:
            print(id)
            user= cls.query.filter(cls.id==user_id).first()
            print(user)
            return user

        except Exception as e:
            print(e)
            return False
    
    @classmethod
    def get_all(cls):
        return cls.query.all()

class Code(db.Model):
    __tablename__ = 'codes'
    user_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('users.id'), primary_key=True)
    code = db.Column(db.String(4), nullable=False)

    def __repr__(self):
        return f'<Code {self.code}>'
