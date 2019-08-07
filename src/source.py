from flask import Flask, request
import os
import peewee

db=peewee.SqliteDatabase('users.db')



class User(peewee.Model):
    chat_id = peewee.TextField(unique=True)
    v1 = peewee.TextField(default="!@#$ )(*&")
    v2 = peewee.TextField(default="!@#$ )(*&")
    class Meta:
        database=db
def init():
    db.connect()
    db.create_tables([User],safe=True)
    db.close()


app=Flask(__name__)

users={}


def get_user_v1(chat_id):
    user=User.get_or_none(chat_id=chat_id)
    if user is None:
        return None
    return user.v1
def get_user_v2(chat_id):
    user=User.get_or_none(chat_id=chat_id)
    if user is None:
        return None
    return user.v2
def set_user_v1(chat_id,state):
    user,created=User.get_or_create(chat_id=chat_id)
    user.v1=state
    user.save()
def set_user_v2(chat_id,state):
    user,created=User.get_or_create(chat_id=chat_id)
    user.v2=state
    user.save()
def delete(chat_id):
    user,created=User.get_or_create(chat_id=chat_id)
    user.v1="!@#$ )(*&"
    user.v2="!@#$ )(*&"
    user.save()



@app.route('/',methods=['post'])
def echo():
    resptext="Ошибка. Попробуйте позже."
    user_id=request.json['session']['user_id']
    if request.json['request']["command"]=="сброс":
        delete(user_id)
    if get_user_v1(user_id) is None or get_user_v1(user_id)=="!@#$ )(*&":
        set_user_v1(user_id,"")
        set_user_v2(user_id,"")
        resptext="Введите V1"

    if get_user_v1(user_id)=="":
        set_user_v1(user_id,request.json['request']["command"])
        resptext="V1 Принято. Введите V2"
    else:
        if get_user_v2(user_id)=="":
            set_user_v2(user_id,request.json['request']["command"])
            resptext="V2 Принято."


    response ={
        'version': request.json['version'],
        'session': request.json['session'],
        'response':{
            'text':resptext
        }
    }
    return response
init()
app.run(host='0.0.0.0',port=os.getenv('PORT',5000))
