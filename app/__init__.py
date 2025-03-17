from flask import Flask,jsonify
from config import Config

def create_app():
    app=Flask(__name__)
    
    app.config.from_object(Config)
    
    @app.route('/',methods=['GET'])
    def index():
        return jsonify({'status':'success','message':'api is working','data':None,'error':None})
    
    return app