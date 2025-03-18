from flask_sqlalchemy import SQLAlchemy
import uuid
from enum import Enum
from random import randint


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
   
    def change_code(self):
       self.code.code=Code.random_()
       db.session.add(self.code)
       db.session.commit()
    
    @classmethod
    def get_by_email(cls,email):
        return cls.query.filter(cls.email==email).first()
        
    @classmethod
    def get_by_id(cls,id):
        try:
            # Convert the input ID to a UUID object
            user_id = uuid.UUID(id)
        except ValueError:
            # Handle invalid UUID format
            return None
        try:
            user= cls.query.filter(cls.id==user_id).first()
            return user

        except Exception as e:
            return False
    @classmethod
    def get_by_id_number(cls,id):
        return cls.query.filter(cls.id_number==id).first()
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod 
    def create_user(cls,user):
        try:
            new_user =cls(id=uuid.uuid4(),firstname=user['firstname'],email=user['email'],id_type=IDType(user['idType']),contact=user['contact'],id_number=user['id_number'])
            db.session.add(new_user)
            db.session.flush()
            new_code=Code(user_id=new_user.id,code=Code.random_())
            db.session.add(new_code)
            db.session.commit()
            db.session.refresh(new_user)
            return new_user
        except Exception as e:
            print(e)
            print('above')
            db.session.rollback()
            return False

class Code(db.Model):
    __tablename__ = 'codes'
    user_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('users.id'), primary_key=True)
    code = db.Column(db.String(4), nullable=False)

    def __repr__(self):
        return f'<Code {self.code}>'

    @staticmethod
    def random_():
        return ''.join(str(randint(0, 9)) for _ in range(4))