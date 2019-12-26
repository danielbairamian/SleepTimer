from timer import *


class Gui:
    def __init__(self, window, timer):
        self.timer = timer
        self.window = window


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

        # Set time button
        self.btn = Button(self.window, text="set time",
                          bg="brown", fg="pink",
                          command=lambda: self.timer.set_time(int(self.h_spin.get()),
                                                               int(self.m_spin.get()), int(self.s_spin.get()))
                          )
        self.btn.grid(column=3, row=3)



       # Start button
        self.btn = Button(self.window, text="Start Timer",
                          bg="orange", fg="red",
                          command=lambda: self.timer.countdown()
                          )
        self.btn.grid(column=3, row=5)

    def run(self):
        print("run gui")
        self.window.mainloop()


    def set_time(self, timer):
        print("set_time")
        # timer.

    # def update_gui(timer):

    # def create_gui(timer):
