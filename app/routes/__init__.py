def register_resource(api):
    from app.routes.user import UsersResource,UserResource
    from app.routes.code import CodesResource
    from app.routes.auth import Register,Login
    from app.routes.ai import Ai
    
    api.add_resource(Register,'/register')
    api.add_resource(Login,'/login')
    api.add_resource(UsersResource,'/users')
    api.add_resource(UserResource,'/users/<string:id>')
    api.add_resource(Ai,'/ai')
    
    api.add_resource(CodesResource,'/codes','/codes/<string:id>')