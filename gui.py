
from timer import *

class Gui:
    def __init__(self, timer):
        self.window = Tk()
        self.window.title("Sleep Timer")
        self.window.configure(background="white")
        self.window.geometry('400x100')

        # Hours label
        self.h_lbl = Label(self.window, text="Hours")
        self.h_lbl.grid(column=0, row=0)
        self.h_spin = Spinbox(self.window, from_=0, to=24, width=5)
        self.h_spin.grid(column=1, row=0)

        # Minutes label
        self.m_lbl = Label(self.window, text="Minutes")
        self.m_lbl.grid(column=2, row=0)
        self.m_spin = Spinbox(self.window, from_=0, to=24, width=5)
        self.m_spin.grid(column=3, row=0)

        # Seconds label
        self.s_lbl = Label(self.window, text="Seconds")
        self.s_lbl.grid(column=4, row=0)
        self.s_spin = Spinbox(self.window, from_=0, to=24, width=5)
        self.s_spin.grid(column=5, row=0)

        # Start button
        self.btn = Button(self.window, text="Start Timer",
                     bg="orange", fg="red",
                     command=lambda: timer.countdown(self.window, int(self.h_spin.get()), int(self.m_spin.get()), int(self.s_spin.get()))
                     )
        self.btn.grid(column=3, row=3)


    def run(self):
        self.window.mainloop()

    def set_time(self, timer):
        print("set_time")
        #timer.

    #def update_gui(timer):


    #def create_gui(timer):
