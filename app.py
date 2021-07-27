import PySimpleGUI as sg

menu_def = [['&Send', ['Message', 'Photo', 'Audio', 'Document', 'Video', 
                        'Animation', 'Voice', 'VideoNote', 'MediaGroup', 
                        'Location', 'Venue', 'Contact', 'Poll', 'Dice', 
                        'ChatAction']], 

            ['&Get', ['getMe', 'UserProfilePhotos', 'File']], 
            ['G&roup', ['banChatMember', 'unbanChatMember', 'restrictChatMember', '---',
                        'setChatAdministationCustomTitle', 'setChatPermissions', '---',
                        'exportChatInviteLink', 'createChatInviteLink', 
                        'editChatInviteLink', 'revokeChatInviteLink', '---',
                        'setChatPhoto', 'deleteChatPhoto', 'setChatTitle', 
                        'setChatDescription','pinChatMessage', 'unpinChatMessage', 
                        'unpinAllChatMessages', '---', 'leaveChat', 'getChat', 
                        'getChatAdministrators', 'getChatMemberCount', 
                        'getChatMember', '---', 'setChatStickerSet', 
                        'deleteChatStickerSet']], 

            ['&Commands', ['setMyCommands', 'deleteMyCommands', 'getMyCommands']], 

            ['&Other', ['1', '2', '3', '4']], 
            
            ['&Exit']]

layout = [[sg.Menu(menu_def)], [sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Console", layout, size=(1000,800))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()