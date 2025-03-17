def register_resource(api):
    from app.routes.user import UsersResouce
    
    api.add_resource(UsersResouce,'/users')