from flask import request
from flask_restful import Resource
from app import jwt
from app.db.models import User
from app.util import send_email,validate_data

class Register(Resource):
    def post(self):
        try:
            data=request.get_json()
            if not data:
                return {"status": "error", "message": "No data provided"}, 400 
            required_field=['firstname','email','contact','id_number','idType']
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

class Login(Resource):
    def post(self):
        data=request.get_json()
        print(data)
        if not data:
            return {"status": "error", "message": "No data provided"}, 400 
        required_field=['email','id_number','otp']
        is_valid,missing,correct=validate_data(data,required_field,optional='role')

        if not is_valid:
            return {'status':'error','message':'required field missing','error':{'field':[miss for miss in missing]}},400
        
        email_exits=User.get_by_email(correct['email'])
        if not email_exits:
            return {'status':'error','message':'Email not found exits'},400
        if email_exits.id_number != correct['id_number']:
            return {'status':'error','message': 'id number not correct'},404
        if email_exits.code.code != correct['otp']:
            return {'status':'error','message':'verification code not correct','error':{'code':False}},400
        token=jwt.create_access_token(identity=email_exits.email)
        print(token)
        return {'status':'success','message':'login was success','data':{'token':token,'id':str(email_exits.id),'role':email_exits.role.value}},200
        