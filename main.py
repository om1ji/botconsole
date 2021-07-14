import requests
import os
import telebot
from tkinter import *

root = Tk()

class Blocks:
    def __init__(self, window,  func):
        self.ent = Entry(window, width=20)
        self.but = Button(window, text="Токен")
        self.lab = Label(window, width=20, bg='black', fg='white')
        self.but['command'] = getattr(self, func)
        self.ent.pack()
        self.but.pack()
        self.lab.pack()

    def init_token(self):
        self.lab['text'] = self.ent.get()
        token = self.lab['text']

token_block = Blocks(root, 'init_token')


if __name__=='__main__':
    root.mainloop()

#BOT = telebot.TeleBot(TOKEN)
