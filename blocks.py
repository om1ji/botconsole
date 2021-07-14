from tkinter import *
import requests
import json

class GetMe:
    def __init__(self, window,  func):
        self.ent = Entry(window, width=50, textvariable='Token')
        self.but = Button(window, text="getMe")
        self.lab = Label(window, width=40, height=4, bg='white', fg='black', wraplength=280, border=20)
        self.but['command'] = getattr(self, func)
        self.ent.pack()
        self.but.pack()
        self.lab.pack()

    def GetMe(self):
        token = self.ent.get()
        r = requests.get(f'https://api.telegram.org/bot{token}/getMe')
        self.lab['text'] = json.loads(r.text)
