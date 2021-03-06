import time
import ctypes
import wmi
import win32con
import win32gui
from pycaw.pycaw import AudioUtilities
from tkinter import *

import logging
import threading
import time

hours = 0
minutes = 0
seconds = 0


def format_seconds_to_hhmmss(seconds):
    hours = seconds / (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds / 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)


def turn_off(window):
    window.destroy()

    # Set brightness to 0
    # c = wmi.WMI(namespace='wmi')
    # methods = c.WmiMonitorBrightnessMethods()[0]
    # methods.WmiSetBrightness(int(0), 0)

    # Mute all sessions
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        volume.SetMute(1, None)

    # lock computer
    ctypes.windll.user32.LockWorkStation()

    # turn off monitors
    SC_MONITORPOWER = 0xF170
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, 2)


def start_countdown(window):
    starting_time = time.time()
    x = threading.Thread(target=countdown, args=(window, starting_time))
    x.start()


def countdown(window, starting_time):
    nonlocal hours, minutes, seconds
    time_limit = hours * 3600 + minutes * 60 + seconds

    print(starting_time)
    time_remaining_label = Label(window)
    time_remaining_label.grid(column=3, row=5)
    while (time.time() - starting_time) < time_limit:
        label_text = "Turning off PC in: "
        '''+ format_seconds_to_hhmmss(
            max(time_limit - (time.time() - starting_time), 0))'''
        time_remaining_label.config(text=label_text)
        window.update()

    turn_off(window)


def set_time(h, m, s):
    nonlocal hours
    hours = h
    nonlocal minutes
    minutes = m
    nonlocal seconds
    seconds = s


def run_app(window):
    window.title("Sleep Timer")
    window.configure(background="white")
    window.geometry('400x100')

    # Hours label
    h_lbl = Label(window, text="Hours")
    h_lbl.grid(column=0, row=0)
    h_spin = Spinbox(window, from_=0, to=24, width=5)
    h_spin.grid(column=1, row=0)

    # Minutes label
    m_lbl = Label(window, text="Minutes")
    m_lbl.grid(column=2, row=0)
    m_spin = Spinbox(window, from_=0, to=24, width=5)
    m_spin.grid(column=3, row=0)

    # Seconds label
    s_lbl = Label(window, text="Seconds")
    s_lbl.grid(column=4, row=0)
    s_spin = Spinbox(window, from_=0, to=24, width=5)
    s_spin.grid(column=5, row=0)

    # Start button
    btn = Button(window, text="Set time",
                 bg="orange", fg="red",
                 command=lambda: set_time(int(h_spin.get()), int(m_spin.get()), int(s_spin.get()))
                 )
    btn.grid(column=3, row=3)

    # Start button
    btn2 = Button(window, text="Start Timer",
                  bg="orange", fg="red",
                  command=lambda: start_countdown(window)
                  )
    btn2.grid(column=3, row=4)

    window.mainloop()


if __name__ == "__main__":
    window = Tk()
    run_app(window)
