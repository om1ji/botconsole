from tkinter import *
from tkinter import ttk
import sys
from methods import *

root = Tk(screenName='TGBot Console')
root.title('TGBot Console')
root.geometry('300x150')

def reset(frame):
    frame.reset

def conf_ent(ent, str):
    return str


# "Send" commands

def send_message_frame():
    pass


# "Get" commands

def getMe_frame():

    token_label = Label(root, text='Token:')
    token = Entry(root, width=40, borderwidth=3)
    
    def press():
        output_label.configure(text=getMe(token.get()))

    button = Button(root, width=5, text='getMe', command=press)
    output_label = Label(root, width=34, height=4, wraplength=250, bd=20, background="#FEFEFE", border=10)
    
    token_label.grid(row=0, column=0)
    token.grid(row=0, column=1)
    button.grid(row=1, column=0, sticky='N')
    output_label.grid(row=1, column=1)
    



# "Group" commands

def group_commands():
    Frame(root).pack_forget

# "Commands" commands

def commands_commands():
    Frame(root).pack_forget

# Other commands

def other_commands():
    Frame(root).pack_forget

# Menus
menu = Menu(root)
root.config(menu=menu)

send_menu = Menu(menu)
send_menu.add_command(label='Message', command=send_message_frame)
send_menu.add_command(label='Photo')
send_menu.add_command(label='Audio')
send_menu.add_command(label='Document')
send_menu.add_command(label='Video')
send_menu.add_command(label='Animation')
send_menu.add_command(label='Voice')
send_menu.add_command(label='VideoNote')
send_menu.add_command(label='MediaGroup')
send_menu.add_command(label='Location')
send_menu.add_command(label='Venue')
send_menu.add_command(label='Contact')
send_menu.add_command(label='Poll')
send_menu.add_command(label='Dice')
send_menu.add_command(label='ChatAction')


get_menu = Menu(root)
get_menu.add_command(label='getMe', command=getMe_frame)
get_menu.add_command(label='UserProfilePhotos')
get_menu.add_command(label='File')

group_menu = Menu(root)
group_menu.add_command(label='banChatMember')
group_menu.add_command(label='unbanChatMember')
group_menu.add_command(label='restrictChatMember')
group_menu.add_command(label='promoteChatMember')
group_menu.add_command(label='setChatAdministrationCustomTitle')
group_menu.add_command(label='setChatPermissions')
group_menu.add_command(label='exportChatInviteLink')
group_menu.add_command(label='createChatInviteLink')
group_menu.add_command(label='editChatInviteLink')
group_menu.add_command(label='revokeChatInvoteLink')
group_menu.add_command(label='setChatPhoto')
group_menu.add_command(label='deleteChatPhoto')
group_menu.add_command(label='setChatTitle')
group_menu.add_command(label='setChatDescription')
group_menu.add_command(label='pinChatMessage')
group_menu.add_command(label='unpinChatMessage')
group_menu.add_command(label='unpinAllChatMessages')
group_menu.add_command(label='leaveChat')
group_menu.add_command(label='getChat')
group_menu.add_command(label='getChatAdministrators')
group_menu.add_command(label='getChatMemberCount')
group_menu.add_command(label='getChatMember')
group_menu.add_command(label='setChatStickerSet')
group_menu.add_command(label='deleteChatStickerSet')

commands_menu = Menu(root)
commands_menu.add_command(label='setMyCommands')
commands_menu.add_command(label='deleteMyCommands')
commands_menu.add_command(label='getMyCommands')

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
