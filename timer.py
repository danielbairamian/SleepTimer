import time
import ctypes
import wmi
import win32con
import win32gui
from pycaw.pycaw import AudioUtilities
from tkinter import *



class Timer:
    #def __init__(self):


    def format_seconds_to_hhmmss(self, seconds):

        hours = seconds / (60*60)
        seconds %= (60*60)
        minutes = seconds / 60
        seconds %= 60
        return "%02i:%02i:%02i" % (hours, minutes, seconds)


    def turn_off(self, window):

        window.destroy()

        # Set brightness to 0
        c = wmi.WMI(namespace='wmi')
        methods = c.WmiMonitorBrightnessMethods()[0]
        methods.WmiSetBrightness(int(0), 0)

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


    def countdown(self, window, hours, minutes, seconds):
        starting_time = time.time()
        time_limit = hours*3600 + minutes*60 + seconds

        time_remaining_label = Label(window)
        time_remaining_label.grid(column=3, row=5)

        while (time.time() - starting_time) < time_limit:
            label_text = "Turning off PC in: " + self.format_seconds_to_hhmmss(max(time_limit - (time.time() - starting_time), 0))
            time_remaining_label.config(text=label_text)
            window.update()

        self.turn_off(window)



