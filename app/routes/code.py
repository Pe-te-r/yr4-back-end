from flask_restful import Resource
from app.db.models import User

class CodesResource(Resource):
    def get(self,id):
        user_exits=User.get_by_id(id)
        if not user_exits:
            return {'status':'error','message':'user not found'},404
        user_exits.change_code()
        return user_exits.code.code
        
