import sys
from asyncio.windows_events import NULL
from msilib.schema import Icon
from os import close
from tkinter.ttk import Button

import pyperclip
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Combo

import ChapterVerse as CV
import list_and_str_ops as list
from BibleFileNames import files
from charEliminator import onlyVerses, remove_only_chars

'''
DO NOT DELETE!
THIS IS THE ULTIMATE BIBLEAPP!
it is the graphical user interface version(finally) of 
the BibleApp.
'''

sg.theme('green')
file = open('bibleSearchResult.txt','w')
file.write('')
#clearing results so next results don't have previous results mixed in
file.close()
#******favorite themes:******
#DarkGray3 is a nice one
#green is my favorite
#darkamber is also a nice one
#******favorite fonts********
#Corbel,LucidaConsole,and Consolas all look like monospace
#Fixedsys is a my favorite
def setsearchrange(startbook,endbook,listoffiles):
  indexoffirstbook = listoffiles.index(f'{list.disclean(startbook)}')
  indexofendbook = listoffiles.index(f'{list.disclean(endbook)}')
  files = listoffiles[indexoffirstbook:indexofendbook+1]
  return files
def linearsearch(searchkey):
  #argument should be search_input
  '''This is the initial search engine for the BibleApp.\n
  It takes a string as input and ouputs to the pysimplegui window
  '''
  for book in files:
    verses = open(book).readlines()
    book = clean(book)
    for verse in verses:
      if searchkey.lower() in verse.lower(): 
        multiple_results.append(f"{book}\n{verse}")
  for result in multiple_results:
    open("bibleSearchResult.txt",'a').write(f'{result}')
  window['RESULT'].update(value = f"{open('bibleSearchResult.txt').read()}")
  if len(multiple_results) == 0:
    window['howMany'].update(value = f"no results found for '{searchkey}'")
    window['RESULT'].update(value="Sorry, the keywords you searched for are not in the Bible. Try searching the same keyword(s) with different spacing or punctuation.(The search is not case sensitive.)")
  elif len(multiple_results) == 1:        
    window['howMany'].update(value = f"{len(multiple_results)} result found for '{searchkey}'")
  else:  
    window['howMany'].update(value = f"{len(multiple_results)} results found for '{searchkey}'")

def clean(str):
  '''This function is similar to the clean() function in list_and_str_ops module except that it uses .title() instead of .lower()'''
  str = str.replace("_", " ")
  halves = str.split(".")
  return str.replace(str, halves[0].title())
def cleanlist(list):
  '''This function needs the clean() function to work. It takes list of strings and returns a list of strings that have to first letter of each string capitalized and without the .txt file extension or underscores.'''
  out = []
  for item in list:
    item = clean(item)
    out.append(item)
  return out
def hasonlyspaces(string):
  '''hasonlyspaces() is a function that returns True if the string it recieves as input consists of only spaces and returns False otherwise.'''
  spaces = []
  for character in string:
    if character == " ":
      spaces.append(character)
  if len(spaces) == len(string):
    return True
  else:
    return False
def create_range_window():
  rangelayout = [
      [sg.Text('Select the book and/or chapter of the Bible to search in.')]
      ,[sg.Text('starting book: ')]  
      ,[sg.Combo(cleanlist(files),key='--book1--',size=(20,5),enable_events=True)]
      ,[sg.Text('ending book: ')]
      ,[sg.Combo(cleanlist(files),key='--book2--',size=(20,5),enable_events=True)]
      ,[sg.Button('set range',key='--submit-search-range-values--',size=(7,2))]
      ,[sg.Text('All the searches you perform will be in the above selected\nrange until you change it.')]
      ,[sg.Button('reset to defuault',key='--reset-to-defualt--',size=(12,2))]
    ]
  return sg.Window('select range to search',rangelayout,size=(384,300),modal=True,icon=r'C:\Users\Joel\Documents\Josh_coding_projects\python_projects\BibleApp\blackbible.ico',finalize=True)
def create_main_window():
  layout = [[
[sg.Text('enter search keywords: ',tooltip='enter search keywords to search entire bible', key='intro',font='Corbel')
,sg.Input(size=(40,4),right_click_menu=['&Right',['copy','paste','search range']], enable_events=True,key='!searched_term!',font='Corbel')
,sg.Button('clear',key='clear',tooltip='clear search bar',font='Fixedsys')
,sg.Button(size=(4,4),key='home',tooltip='home',image_data=b'iVBORw0KGgoAAAANSUhEUgAAAC4AAAArCAYAAAAHdLqEAAAAAXNSR0IArs4c6QAAArNJREFUaEPtmc9rE1EQx7+zbRpi4qE9RAQRmm5QURGJIkWTVYv/gJ4ED0FB8BirCegfYLfqtYL/gD1oQfTQW2uVYk/2lxXtpSiiGE9VosVNtqRt2uzu2923zdu0ld3rznvvM98ZZubtUqlU0rEDHwrATVHreTSO4pKG6ZwC6OKDKl5xIiTVVwY35gvi4cWCM6BrHnwqKCCG8hJRnZM6KpzBEQfuAL0On1dA2CC78mQSE18WDdH5pwMLhYxruRADzgHNgk/2jzEBB7MnkYpHHOEbBiciyKacdpPrY16BBB124AOXjuBCV4eP4CQhqY66cTLfv+9N4/DD18x3voJvRmleD30DJ0mC3Lc5pXngfQH3U+maU8LBSSLIfcbmwqOgVxuh4H6nR71z4sA91Gmv6rLshYBXABywaRQiIFl73FY6cf3UfqCuy5rtHBtQGYSD/f7nNAt+9lYGYcleGlvwrYSu4U73ZhBpYcMzwTUQDm2R0mbMdzfTiLXWT5CrFhbwMiQk1BG0GcZNv7KZb19W2ljA7QYfviP8s5rPG0ddA3hJl3Dsvn+tvBG3hrIpHI1H17fYOYqbrn8W8Oos8uDNAoq//iIcasWSVsGzqW+NiOV5bVpux55o28odOxYO4e55GaRXO8rG43qR+Ppbw9mBcc+HN7JASOf878EXtTK+3zkHa8Vd054I++6NICI5tMM106Yqbi5XdqmSUMfQYuvd6qqmgXfsDmHiRjdXWl8cnMTMZ+MnCfPCpoF3xaMYzqa4wHMv5vDyw09H2wDcrRwGije7qgSKB4oD4Gn5QaoEqQKgAkKnOup4BxWdKlO5M9gVch7GXOfxavRmin9w+vFb0MrsV/0VYpySuvfGMHz1BFfLv/Z8Dk9nf9jY6hi6fBw9iXbHj0HMWz7X6dvAiEvxbcBpQVgG27DeBvmxJ9oAAAAASUVORK5CYII=')
,sg.Button('SEARCH',key='enteredSEARCH',tooltip='search keyword', bind_return_key=True,font='Fixedsys')
,sg.Input('No search results yet',font=('Fixedsys','5'),disabled=True,disabled_readonly_background_color='lightgrey',disabled_readonly_text_color='black',key='howMany',size=(37,4))
,sg.Combo(cleanlist(files),tooltip='choose book of Bible to be displayed',default_value='Genesis',key='booksOfBible',enable_events=True,background_color='silver', size = (20,10))
,sg.Combo([],key='chaptersInBook',tooltip='choose chapter from selected book at left to be displayed',enable_events=True,size=(3,7),background_color='silver')
,sg.Combo([],key='versesInChapter',tooltip='choose verse from chapter of book selected at left to be displayed',enable_events=True,size=(3,7),background_color='silver')
]
,[sg.Multiline(f'{open("Bible.txt").read()}',key='RESULT',right_click_menu=['&Right', ['copy', 'read-aloud','bookmark']],font='Consolas',size=(300,200),disabled=True)]
]]
  return sg.Window('Desktop Bible', layout,icon=r'C:\Users\Joel\Documents\Josh_coding_projects\python_projects\BibleApp\blackbible.ico', size=(1000,700),finalize=True,resizable=True).Maximize()

  
def nums(first_number, last_number, step=1):
    '''This function is for loops.'''
    return range(first_number, last_number+1, step)
def strlist(list):
  '''This function takes a list and returns a list of strings.'''
  a = []
  for i in list:
    a.append(str(i))
  return a
window1, window2 = create_main_window(), None
while True:
  open('bibleSearchResult.txt','w').write('')
  window, event, values = sg.read_all_windows()           #read signals from all windows
  if event == sg.WIN_CLOSED:
    if window == window2:       # if closing winow 2, mark as closed
      window2.close()
      window2 = None    
    else:         # under all other conditions, exit the program
      break
  elif event == 'clear':
    window['!searched_term!'].update('')
  elif event == 'home':
    window['RESULT'].update(open('Bible.txt').read())
  elif event == 'booksOfBible':
    combo = values['booksOfBible'].replace(' ', '_')
    bookFromUser = open(f'{combo}.txt').readlines()
    chapsInBook = bookFromUser[-1].split(':')[0]
    chapnumforbox = []
    for i in nums(1,int(chapsInBook)):
      chapnumforbox.append(i)
    window['chaptersInBook'].update(values=chapnumforbox)
    window['versesInChapter'].update([])
    window['RESULT'].update(open(f'{combo}.txt').read())
  elif event == 'chaptersInBook':
    #get values in chaptersInBook
    chapterFromUser = values['chaptersInBook']
    fileFromUser = f'{combo}.txt'.replace(' ','_')
    verseInChap = len(CV.get_chap(fileFromUser,chapterFromUser))
    chapterforresult = CV.get_chap(fileFromUser,chapterFromUser)
    searchResultFile = open('bibleSearchResult.txt','w')
    #append mode not work, write mode does!?
    for verse in chapterforresult:
      searchResultFile.write(verse)
    searchResultFile.close()
    versenumforbox = []
    for e in nums(1,verseInChap):
      versenumforbox.append(e)
    window['versesInChapter'].update([])
    window['versesInChapter'].update(values=versenumforbox)
    window['RESULT'].update(f"{open('bibleSearchResult.txt','r').read()}")
  elif event =='versesInChapter':
    verseFromUser = values['versesInChapter']
    verseForUser = CV.get_verse(fileFromUser,chapterFromUser,int(verseFromUser))
    window['RESULT'].update(verseForUser)
  elif event == 'copy':
    try:
      selection = window['RESULT'].Widget.selection_get()
    except sg.tk.TclError:
      break
    #code to copy to clipboard
    pyperclip.copy(selection)
  elif event == 'paste':
    #code to paste
    text = pyperclip.paste()
    window['!searched_term!'].update(text)
  elif event == 'search range':   #and not window2
    window2 = create_range_window()
  elif event == '--submit-search-range-values--':      #submitting the search range values in the search range window
    #the code in this block submits the values in the search range window and then closes the window
    startingbook = values['--book1--']
    endingbook = values['--book2--']
    if startingbook == '' and endingbook == '':
      sg.popup('You must select a book!',icon=r'C:\Users\Joel\Documents\Josh_coding_projects\python_projects\BibleApp\blackbible.ico')
    elif startingbook == '' or endingbook == '':
      sg.popup('You must fill in all the choices!',icon=r'C:\Users\Joel\Documents\Josh_coding_projects\python_projects\BibleApp\blackbible.ico')
    elif files.index(list.disclean(startingbook)) > files.index(list.disclean(endingbook)):
      sg.popup('The end of the range comes before the start of the range.\nFor best results, please change this.',icon=r'C:\Users\Joel\Documents\Josh_coding_projects\python_projects\BibleApp\blackbible.ico')
    else:
      files = setsearchrange(startingbook,endingbook,files)
      window2.close()
  elif event == '--reset-to-defualt--':
    files = ["genesis.txt", "exodus.txt", "leviticus.txt", "numbers.txt", "deuteronomy.txt", "joshua.txt", "judges.txt", "ruth.txt", "first_samuel.txt", "second_samuel.txt", "first_kings.txt", "second_kings.txt", "first_chronicles.txt", "second_chronicles.txt", "ezra.txt", "nehemiah.txt", "esther.txt", "job.txt", "psalms.txt", "proverbs.txt", "eccliasiastes.txt", "song_of_solomon.txt", "isaiah.txt", "jeremiah.txt", "lamentations.txt", "ezekial.txt", "daniel.txt", "hosea.txt", "joel.txt", "amos.txt", "obadiah.txt", "jonah.txt", "micah.txt", "nahum.txt", "habakkuk.txt", "zephaniah.txt", "haggai.txt", "zechariah.txt", "malachi.txt", "matthew.txt", "mark.txt", "luke.txt", "john.txt", "acts.txt", "romans.txt", "first_corinthians.txt", "second_corinthians.txt", "galatians.txt", "ephesians.txt", "philipians.txt", "colossians.txt", "first_thesselonians.txt", "second_thesselonians.txt", "first_timothy.txt", "second_timothy.txt", "titus.txt", "philemon.txt", "hebrews.txt", "james.txt", "first_peter.txt", "second_peter.txt", "first_john.txt", "second_john.txt", "third_john.txt", "jude.txt", "revelation.txt"]
    window2.close()
  elif event == 'enteredSEARCH':
    search_input = values['!searched_term!']
    multiple_results = []
    verses = ""
    if search_input == "exit()":
      sys.exit()
    elif search_input == '':
      continue
    elif search_input == " " or hasonlyspaces(search_input) or len(search_input) <= 2:
      longsearch = sg.popup_ok_cancel("You are about to initiate a long search.Searches that consist of spaces only or less than two characters usually take a while. Would you like to continue?",icon=r'C:\Users\Joel\Documents\Josh_coding_projects\python_projects\BibleApp\blackbible.ico')
      if longsearch == 'OK':
        linearsearch(search_input)
      elif longsearch == 'Cancel':
        continue
    else:
      linearsearch(search_input)
window.close()
