from tkinter import *
from tkinter import ttk


def update_clicks():
    global clicks
    clicks += 1
    label.config(text=clicks)

root = Tk()
root.title("Calculator")
root.geometry("200x200+600+200")
root.resizable(0, 0)

clicks = 0

label = ttk.Label(text=clicks, font=30)
label.pack(anchor='center', pady=20)

button = Button(root, text='Click', command=lambda: update_clicks())
button.pack(anchor='s', pady=10)

root.mainloop()