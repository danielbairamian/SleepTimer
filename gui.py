
from timer import *

def create_gui(timer):
    window = Tk()
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
    btn = Button(window, text="Start Timer",
                 bg="orange", fg="red",
                 command=lambda: timer.countdown(window, int(h_spin.get()), int(m_spin.get()), int(s_spin.get()))
                 )
    btn.grid(column=3, row=3)

    window.mainloop()