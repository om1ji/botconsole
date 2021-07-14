from tkinter import *
from blocks import *

root = Tk(screenName='TGBot Console')
root.title('TGBot Console')
root.geometry('300x150')

token_block = GetMe(root, 'GetMe')
root.mainloop()
