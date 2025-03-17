from flask_restful import Resource
from flask import request
from app.db.models import User
from app.util import send_email

def validate_data(data,valid,optional=None):
    missing_field=[]
    correct_field=[]
    for value in valid:
        if value not in data:
            missing_field.append(value)
        else:
            correct_field.append({value:data[value]})
    if optional:
        if optional in data:
            correct_field.append({optional:data[optional]})
    data_={}
    for field in correct_field:
        for key,value in field.items():
            data_[key]=value
    
    return len(missing_field)<=0,missing_field,data_

    

class UsersResource(Resource):
    def get(self):
        try:
            users=User.get_all()
            # print(users)
            if not users:
                return {'status':'error','message':'no user found'}
            return {'status':'success','message':'users retrived success','data':[user.to_json() for user in users]}
        except Exception as e:
            print(e)
            return False
    
    def post(self):
        try:
            data=request.get_json()
            if not data:
                return {"status": "error", "message": "No data provided"}, 400 
            required_field=['firstname','email','contact','id_number','id_type']
            is_valid,missing,correct=validate_data(data,required_field,optional='role')

            if not is_valid:
                return {'status':'error','message':'required field missing','error':{'field':[miss for miss in missing]}},400
            email_exits=User.get_by_email(correct['email'])
            id_exits=User.get_by_id_number(correct['id_number'])
            if email_exits or id_exits:
                error='email' if email_exits else 'id'
                return {'status':'error','message':f'{error} already exits'},400
            new_user=User.create_user(correct)
            if not new_user:
                return {'status':'error','message':'User not created'},500
            send_email(new_user.email,'Welcom to SHA','welcome.html',username=new_user.firstname)
            return {'status':'success','message':'users created success','data':new_user.to_json()},201
        except Exception as e:
            return False
        
        

class UserResource(Resource):
    def get(self,id):
        user=User.get_by_id(id)
        print(user)
        return 'success'