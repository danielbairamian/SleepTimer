from flask import Flask, escape, request
from multiprocessing import Process, Value

from gui import *

app = Flask(__name__)

timer = Timer()
gui = Gui(timer)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route("/start")
def start():
    return f'200'


@app.route("/time")
def time():
    print(request.args)
    hours = int(request.args["hours"])
    minutes = int(request.args["minutes"])
    seconds = int(request.args["seconds"])
    print("--->", hours, minutes, seconds)
    timer.set_time(hours,minutes,seconds)
    print("set time")
    print(hours, minutes, seconds)


    #set_time(int(hours), int(minutes), int(seconds))
    return f'200'

@app.route("/printtime")
def printtime():
    print(timer)
    print(timer.get_time())
    return timer.get_time()

if __name__ == '__main__':

    print("in main, starting up")
    print(timer)

    print("new process inc")
    #gui.run(timer)
    gui_process = Process(target=gui.run, args=(timer,))
    gui_process.start()

    #app.run(debug=True, use_reloader=False)

    #gui_process.join()
    #create_gui(timer)
