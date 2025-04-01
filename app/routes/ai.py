from flask_restful import Resource
from flask import request
from app.util import validate_data

from os import getenv

from google import genai

def askQuestion(question):

    client = genai.Client(api_key=getenv('API_KEY'))

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[question])
    return response.text


class Ai(Resource):
    def post(self):
        data=request.get_json()
        print(data)
        if not data:
            return {"status": "error", "message": "No data provided"}, 400 
        required_field=['query']
        is_valid,missing,correct=validate_data(data,required_field,optional='user_id')

        if not is_valid:
            return {'status':'error','message':'required field missing','error':{'field':[miss for miss in missing]}},400
        answer=askQuestion(correct['query'])
        print(answer)
        return {'status':'success','message':'response was brought','data':answer}
    

    def get(self):
        result=askQuestion("How does AI work?")
        return result
