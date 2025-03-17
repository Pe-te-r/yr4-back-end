def register_resource(api):
    from app.routes.user import UsersResource,UserResource
    from app.routes.code import CodesResource
    
    api.add_resource(UsersResource,'/users')
    api.add_resource(UserResource,'/users/<string:id>')
    
    api.add_resource(CodesResource,'/codes/<string:id>')