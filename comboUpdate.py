import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Combo
'''
I used this script to debug my issues with updating pysimplegui
combo boxes.
'''
sg.theme('green')
layout = [
    [sg.Combo(['hehe','hoho'],key='test',size=(20,5),enable_events=True),sg.Button('submit',key='submit')]
    ]

window = sg.Window('comboTest',layout,size=(400,356))
while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break
  if event == 'submit':
    window['test'].update(values=['string1','string2','string3','string4'])