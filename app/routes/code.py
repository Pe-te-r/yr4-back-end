from flask_restful import Resource
from app.db.models import User
from app.util import send_email

class CodesResource(Resource):
    def get(self,id):
        user_exits=User.get_by_id(id)
        if not user_exits:
            return {'status':'error','message':'user not found'},404
        user_exits.change_code()
        if send_email(user_exits.email,'Verification Code','code.html',username=user_exits.firstname,code=user_exits.code.code):
            return {'status':'success','message':'email sent successful'}
        return {'status':'error','message':'code not sent try again'}
        

        
