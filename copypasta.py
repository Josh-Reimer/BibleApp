import PySimpleGUI as sg
import pyperclip

'''copypaste.py is a file that I used to debug
 the copy and paste issues with bibleGUI.py. 
 In the end, it wasn't pysimplegui or tkinter at fault; 
 it was a misspelling of the copy keyword on the right click menu!
 '''
layout1 = [
    [sg.Input(key='-search-',right_click_menu=['&Right',['copy','paste','cut']])],
    [sg.Multiline('1:1: In the beginning God created the heaven and the earth. 1:2: And the earth was without form, and void; and darkness was upon the face of the deep.  And the Spirit of God moved upon the face of the waters.',size=(80, 80), key='-IN-',right_click_menu=['&Right', ['copy']])]
    ,[sg.OK(key="-ok-")]
]
window1 = sg.Window('copy not Copy', layout1, finalize=True,size=(600,500))

while True:  # Event Loop
    event, values = window1.read()
    print('reading window...')
    if event == sg.WIN_CLOSED:
        print('closed window')
        break
    elif event == 'copy':
        try:
            print('getting selection...')
            selection = window1['-IN-'].Widget.selection_get()
        except sg.tk.TclError:
            print('error!')
            
        print('copied')
        pyperclip.copy(selection)
        print(selection)
    elif event == 'paste':
        print('pasted')
        pasted = pyperclip.paste()
        window1['-search-'].update(pasted)