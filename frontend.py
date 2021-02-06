#for the http requests
import requests
from flask import request
from tkinter import *
root = Tk()
root.title("Message Your Mates")
BASE = 'http://127.0.0.1:5000/'
def post():
    #send the message to the person who you want with the message you want
    message = entry.get()
    person = to.get()
    name = fromm.get()
    label = Label(root, text=message)
    label.pack()
    response = requests.post(BASE + 'person1/' + message + '/' + person + '/' + name)
def get1():
    #when you refresh 
    person = to.get()
    name = fromm.get()
    http = BASE + 'person1/none' + '/' + person + '/' + name
    response = requests.get(http)
    response = response.json()
    label = Label(root, text=response['message'])
    label.pack()
#tkinter gui setup
fromm = Entry(root, width=50, bg='red', borderwidth=10)
fromm.pack()
to = Entry(root, width=50, bg='red', borderwidth=10)
to.pack()
entry = Entry(root, width=50, bg='red', borderwidth=10)
entry.pack()
submit = Button(root, text='Submit', command=post)
submit.pack()
refresh = Button(root, text='Refresh', command=get1)
refresh.pack()



