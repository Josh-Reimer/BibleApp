import ChapterVerse as CV
from BibleFileNames import files
import list_and_str_ops as list

'''I am not sure if this file is referenced by anything.'''

while True:
  
  result = False
  book = False
  chapter = False
  verse = False
  for file in files:
    user = input("Book?\n-->")
    user = user.replace(" ", "")
    if list.clean(file) in user.lower():
      book = file
      
    elif not list.clean(file) in user.lower():
      print("\nunidentified strings will defualt to the first book in the list\n")
      book= files[0]
    user = input("Chapter?\n-->")
    user = user.replace(" ", "")
    if user.lower() == "n":
      chapter = False
    elif user.isdigit():
      chapter = int(user)
      
    else:
       print("\nNon-numeric characters defualt to 1\n")
       chapter = 1
    user = input("Verse?\n-->")
    user = user.replace(" ","")
    if user.lower() == "n":
      verse = False
    elif user.isdigit():
      verse = int(user)
      
    else: 
      print("\nNon-numeric characters defualt to 1\n")
      verse = 1

    if verse and chapter:
      print(CV.get_verse(book,chapter,verse))
    if chapter and not verse:
      outchap = CV.get_chap(book,chapter)
      for o in outchap:
        print(o)
    if not chapter and  not verse:
      print(open(book).read())
    if verse and not chapter:
      print(CV.get_verse(book,1,verse))
  continue