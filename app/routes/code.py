from flask import request
from flask_restful import Resource
from app.db.models import User
from app.util import send_email,validate_data

class CodesResource(Resource):
    def get(self,id=None):
        if id:
            user_exits=User.get_by_id(id)
            if not user_exits:
                return {'status':'error','message':'user not found'},404
            user_exits.change_code()
            if send_email(user_exits.email,'Verification Code','code.html',username=user_exits.firstname,code=user_exits.code.code):
                return {'status':'success','message':'email sent successful'}
            return {'status':'error','message':'code not sent try again'}
        
        return {'status':'error','message':'id not provided'}
    
    def post(self):
        
        data=request.get_json()
        
        is_valid,missing_field,valid_field=validate_data(data,['email'])
        if is_valid:
            user_exits= User.get_by_email(valid_field['email'])
            if not user_exits:
                return {'status':'error','message':'Email not found'},404
            user_exits.change_code()
        
            if send_email(user_exits.email,'Verification Code','code.html',username=user_exits.firstname,code=user_exits.code.code):
                return {'status':'success','message':'Verification code sent to email'},200
            
            return {'status':'error','message':'code not sent try again'},304
        return {'status':'error','message':'missing field required','error':{'field':missing_field}}