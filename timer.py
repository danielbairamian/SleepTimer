import time
import ctypes
import wmi
import win32con
import win32gui
from pycaw.pycaw import AudioUtilities
from tkinter import *



class Timer:
    def __init__(self):
        #, window, hours, minutes, seconds
        #self.window = window
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def format_seconds_to_hhmmss(self, seconds):
        #affected by self.h,m,s because they're used to calculate time_limit
        hours = seconds / (60*60)
        seconds %= (60*60)
        minutes = seconds / 60
        seconds %= 60
        return "%02i:%02i:%02i" % (hours, minutes, seconds)

    def set_time(self, h, m, s):
        print("set_time")
        print("h is: " , h)
        self.hours = h
        self.minutes = m
        self.seconds = s
        print(self.get_time())
    def get_time(self):
        return "%02i:%02i:%02i" % (self.hours, self.minutes, self.seconds)



    def turn_off(self, window):


        for i in range(0, 100):
            print("Turn off.")
        '''window.destroy()

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
        '''

    def countdown(self):
        starting_time = time.time()
        time_limit = self.hours*3600 + self.minutes*60 + self.seconds

        print("countdown")

        '''
        TODO: fix
        time_remaining_label = Label(self.window)
        time_remaining_label.grid(column=3, row=5)

        while (time.time() - starting_time) < time_limit:
            label_text = "Turning off PC in: " + self.format_seconds_to_hhmmss(max(time_limit - (time.time() - starting_time), 0))
            time_remaining_label.config(text=label_text)
            self.window.update()

        self.turn_off(self.window)
        '''



