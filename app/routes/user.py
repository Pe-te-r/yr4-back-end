from flask_restful import Resource
from app.db.models import User

class UsersResource(Resource):
    def get(self):
        users=User.get_all()
        # print(users)
        if True:
            return {'status':'error','message':'no user found'}
        
        # return {'status':'success','message':'users retrived success','data':[user.to_json() for user in users]}

class UserResource(Resource):
    def get(self,id):
        user=User.get_by_id(id)
        print(user)
        return 'success'