import tkinter as tk
from canvas import app


def clean_screen():
    for el in app.grid_slaves():
        el.destroy()
        tk.Button(app, text='Exit', command=app.destroy()).grid(row=10, column=10, pady=20)
        