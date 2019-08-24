from flask import Flask, escape, request
from main import run_app, set_time
from tkinter import *

app = Flask(__name__)

window = Tk()
run_app(window)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route("/start")
def start():
    return f'200'


@app.route("/time")
def time():
    hours = request.args["hours"]
    minutes = request.args["minutes"]
    seconds = request.args["seconds"]
    set_time(int(hours), int(minutes), int(seconds))
    return f'200'

