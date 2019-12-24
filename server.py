from flask import Flask, escape, request
from multiprocessing import Process, Value

from gui import *

app = Flask(__name__)

timer = Timer

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
    #set_time(int(hours), int(minutes), int(seconds))
    return f'200'


if __name__ == '__main__':

    gui_process = Process(target=create_gui, args=(timer,))
    gui_process.start()

    app.run(debug=True, use_reloader=False)

    gui_process.join()
    #create_gui(timer)
