from flask_restful import Resource
from app.db.models import User

    

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
    
    
        

class UserResource(Resource):
    def get(self,id):
        user=User.get_by_id(id)
        print(user)
        return 'success'

