from flask import Flask,jsonify
from flask_cors import CORS
from flask_mail import Mail
from flask_restful import Api
from flask_migrate import Migrate
from app.JwtManager import CustomJWT
from config import Config
from app.db.models import db

mail_ = Mail()
jwt=CustomJWT()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    mail_.init_app(app)
    jwt.init_app(app)
    CORS(app, supports_credentials=True)  # Enable CORS for all routes
    
    
    
    @app.route('/',methods=['GET']) 
    @jwt.jwt_required
    def index():
        return jsonify({'status':'success','message':'api is running','data':None,'error':None})

    api=Api(app,prefix='/api')
    from app.routes import register_resource
    register_resource(api)
    return app
