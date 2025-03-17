from flask_restful import Resource

class UsersResouce(Resource):
    def get(self):
        return {'status':'success','message':'users retrived success','data':'users list'}