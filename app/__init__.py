from flask import Flask,jsonify
from flask_cors import CORS
from flask_mail import Mail
from flask_restful import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from app.db.models import db

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    mail.init_app(app)
    JWTManager(app)
    CORS(app, supports_credentials=True)  # Enable CORS for all routes
    
    
    
    @app.route('/',methods=['GET']) 
    def index():
        return jsonify({'status':'success','message':'api is running','data':None,'error':None})

    api=Api(app,prefix='/api')
    from app.routes import register_resource
    register_resource(api)
    return app
