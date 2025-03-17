def register_resource(api):
    from app.routes.user import UsersResource,UserResource
    
    api.add_resource(UsersResource,'/users')
    api.add_resource(UserResource,'/users/<string:id>')