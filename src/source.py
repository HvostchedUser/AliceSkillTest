from flask import Flask, request
import os

app=Flask(__name__)

@app.route('/',methods=['post'])
def echo():
    response ={
        'version': request.json['version'],
        'session': request.json['session'],
        'response':{
            'text':request
        }
    }
    return response
app.run(host='0.0.0.0',port=os.getenv('PORT',5000))
