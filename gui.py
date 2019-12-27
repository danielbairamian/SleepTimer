from timer import *


class Gui:
    def __init__(self, timer):
        self.timer = timer
        #timer = t


    def update_time(self):
        print("update time")


    def countdown(self):
        print("start countdown")

        #print(self.timer)
        #self.timer.set_time(10,10,100)
        #print(self.timer.get_time())
        #print(self.timer.hours)
        #print(self.timer.seconds)
        starting_time = time.time()
        time_limit = self.timer.hours * 3600 + self.timer.minutes * 60 + self.timer.seconds

        #TODO: fix
        time_remaining_label = Label(self.window)
        time_remaining_label.grid(column=3, row=5)

        while (time.time() - starting_time) < time_limit:
            label_text = "Turning off PC in: " + self.timer.format_seconds_to_hhmmss(max(time_limit - (time.time() - starting_time), 0))
            time_remaining_label.config(text=label_text)
            self.window.update()

        self.timer.turn_off(self.window)


    def run(self):
        print("run gui")
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
                          command=lambda: self.countdown()
                          )
        self.btn.grid(column=3, row=5)
        self.window.mainloop()


    def set_time(self, timer):
        print("set_time")
        # timer.

    # def update_gui(timer):

    # def create_gui(timer):
