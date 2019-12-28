from flask import Flask, escape, request
from multiprocessing import Process, Value
from threading import Thread
from gui import *

app = Flask(__name__)

timer = Timer()
gui = Gui(timer)


def start_countdown():
    gui.countdown()

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route("/start")
def start():
    start_countdown()
    return f'200'


@app.route("/time")
def time():
    hours = int(request.args["hours"])
    minutes = int(request.args["minutes"])
    seconds = int(request.args["seconds"])
    timer.set_time(hours,minutes,seconds)


    #set_time(int(hours), int(minutes), int(seconds))
    return f'200'

@app.route("/printtime")
def printtime():
    print(timer)
    print(timer.get_time())
    return timer.get_time()



if __name__ == '__main__':

    thread = Thread(target=gui.run, args=(timer,))
    thread.start()
    #thread.join()

    app.run(debug=True, use_reloader=False)
    thread.join()
