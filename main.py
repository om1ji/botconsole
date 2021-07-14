from tkinter import *
from tkinter import ttk
import sys
from methods import *

root = Tk(screenName='TGBot Console')
root.title('TGBot Console')
root.geometry('300x150')

# "Send" commands

def send_frame():
    send_frame = Frame(root)
    button = Button(send_frame, text='Bruh')
    button.pack()
    send_frame.pack()

# "Get" commands

def get_commands():
    Frame(root).pack_forget

# "Group" commands

def group_commands():
    Frame(root).pack_forget

# "Commands" commands

def commands_commands():
    Frame(root).pack_forget

# Other commands

def other_commands():
    Frame(root).pack_forget
    frame = Frame(root)

    token = Entry(frame, width=50)
    token.insert(0, 'Token')
    token.grid(row=0, column=1)

    button = Button(frame, width=20, text='getMe', command=getMe)

    label = Label(frame, width=100, height=4, wraplength=280, bd=20)
    label['text'] = button

# Menus
menu = Menu(root)
root.config(menu=menu)

send_menu = Menu(menu)
send_menu.add_command(label='1', command=send_frame)
send_menu.add_command(label='2')
send_menu.add_command(label='3')
send_menu.add_command(label='4')

get_menu = Menu(root)
get_menu.add_command(label='1')
get_menu.add_command(label='2')
get_menu.add_command(label='3')
get_menu.add_command(label='4')

group_menu = Menu(root)
group_menu.add_command(label='1')
group_menu.add_command(label='2')
group_menu.add_command(label='3')
group_menu.add_command(label='4')

commands_menu = Menu(root)
commands_menu.add_command(label='1')
commands_menu.add_command(label='2')
commands_menu.add_command(label='3')
commands_menu.add_command(label='4')

other_menu = Menu(root)
other_menu.add_command(label='1')   
other_menu.add_command(label='2')
other_menu.add_command(label='3')
other_menu.add_command(label='4')

menu.add_cascade(label='Send', menu=send_menu)
menu.add_cascade(label='Get', menu=get_menu)
menu.add_cascade(label='Group', menu=group_menu)
menu.add_cascade(label='Commands', menu=commands_menu)
menu.add_cascade(label='Other', menu=other_menu)
menu.add_command(label='Exit', command=sys.exit)

root.mainloop()
