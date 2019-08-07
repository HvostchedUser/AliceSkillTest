from flask import Flask, request
import os

app=Flask(__name__)

players=[]

@app.route('/',methods=['post'])
def echo():
    response ={
        'version': request.json['version'],
        'session': request.json['session'],
        'response':{
            'text':str(request.json[text][::-1]==request.json[text])
    }
    return response
app.run(host='0.0.0.0',port=os.getenv('PORT',5000))
