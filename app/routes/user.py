from flask_restful import Resource
from app.db.models import User
from app import jwt

    

class UsersResource(Resource):
    method_decorators=[jwt.jwt_required]
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
    
    
        

class UserResource(Resource):
    method_decorators=[jwt.jwt_required]
    def get(self,id):
        user=User.get_by_id(id)
        if not user:
            {'status':'error','message':'user not found'},404
        
        return {'status':'success','message':'user retrived success','data':user.to_json()},200


