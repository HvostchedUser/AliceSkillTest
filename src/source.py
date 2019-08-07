from flask import Flask, request
import os

app=Flask(__name__)

@app.route('/',methods=['post'])
def echo():
    response=request
    response.response.text=str(request)
    return response
app.run(host='0.0.0.0',port=os.getenv('PORT',5000))
