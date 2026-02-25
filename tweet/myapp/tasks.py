from tweet.celery import app
from time import sleep
from celery import shared_task

@app.task
def add(x,y):
    sleep(5)
    return x+y

@shared_task
def mul(x,y):
    sleep(10)
    return x*y

@shared_task
def texts(a):
    print('this is the text shown::',a)
