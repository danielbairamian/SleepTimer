import time
import ctypes
import wmi
import win32con
import win32gui
from pycaw.pycaw import AudioUtilities


class Timer:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def format_seconds_to_hhmmss(self, seconds):
        hours = seconds / (60*60)
        seconds %= (60*60)
        minutes = seconds / 60
        seconds %= 60
        return "%02i:%02i:%02i" % (hours, minutes, seconds)

    def set_time(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def get_time(self):
        return "%02i:%02i:%02i" % (self.hours, self.minutes, self.seconds)


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


