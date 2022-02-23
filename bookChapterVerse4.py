import sys

from colorama import init
from termcolor import colored

import ChapterVerse as CV
import list_and_str_ops as list
from BibleFileNames import files
from charEliminator import onlyVerses, remove_only_chars
'''
DO NOT DELETE!
This is the book-chapter-verse feature alone in the cli program.
It is coloured.
This is the latest version of its kind
and the most stable.
'''
init() 
print(colored('\ndesktop version 4 of Bible\n','red'))
result = False
book = False
chapter = False
verse = False
while True:
  user = input("Book?\n-->")
  user = user.replace(" ", "").lower()
  if user == "exit()":
    sys.exit()
  for file in files:
    if user != list.clean(file):
      continue
    if list.clean(file) in user:
      book = list.disclean(user)
    else:
      continue
    user = input("Chapter?\n-->")
    user = user.replace(" ", "")
    if user == "exit()":
      sys.exit()
    if user.lower() == "n":
      chapter = False
    elif user.isdigit():
      noNums = remove_only_chars(open(book).readlines())
      for v in noNums:
        length = noNums[-1].split(":")[0]
        if int(user) > int(length):        
          print(colored(f"\nthere are only {int(length)} chapters in {list.clean(book)}\n\ndefualted to 1\n","red"))
          chapter = 1
          break
        else:
          chapter = int(user)
    else:
       print(colored("\nNon-numeric characters defualt to 1\n","yellow"))
       chapter = 1
    user = input("Verse?\n-->")
    user = user.replace(" ","")
    if user == "exit()":
      sys.exit()
    if user.lower() == "n":
      verse = False
    elif user.isdigit():
      number_of_verses = len(CV.get_chap(book,chapter))
      if int(user) > number_of_verses:
        print(colored(f"\nThere are only {number_of_verses} verses in {list.clean(book).title()}:{chapter}\n\ndefualted to 1\n","red"))
        verse = 1
      else:
        verse = int(user)   
    else: 
      print(colored("\nNon-numeric characters defualt to 1\n","red"))
      verse = 1
    if verse and chapter:
      print(colored(CV.get_verse(book,chapter,verse),"white"))
    if chapter and not verse:
      outchap = CV.get_chap(book,chapter)
      for o in outchap:
        print(colored(o,"white"))
    if not chapter and  not verse:
      print(colored(open(book).read(),"white"))
    if verse and not chapter:
      print(colored(CV.get_verse(book,1,verse),"white"))

#function for above code below

def bookChapterVerse():
  result = False
  book = False
  chapter = False
  verse = False
  while True:
    user = input("Book?\n-->")
    user = user.replace(" ", "").lower()
    if user == "exit()":
      sys.exit()
    for file in files:
      if user != list.clean(file):
        continue
      if list.clean(file) in user:
        book = list.disclean(user)
      else:
        continue
      user = input("Chapter?\n-->")
      user = user.replace(" ", "")
      if user == "exit()":
        sys.exit()
      if user.lower() == "n":
        chapter = False
      elif user.isdigit():
        noNums = remove_only_chars(open(book).readlines())
        for v in noNums:
          length = noNums[-1].split(":")[0]
          if int(user) > int(length):        
            print(colored(f"\nthere are only {int(length)} chapters in {list.clean(book)}\n\ndefualted to 1\n","red"))
            chapter = 1
            break
          else:
            chapter = int(user)
      else:
         print(colored("\nNon-numeric characters defualt to 1\n","yellow"))
         chapter = 1
      user = input("Verse?\n-->")
      user = user.replace(" ","")
      if user == "exit()":
        sys.exit()
      if user.lower() == "n":
        verse = False
      elif user.isdigit():
        number_of_verses = len(CV.get_chap(book,chapter))
        if int(user) > number_of_verses:
          print(colored(f"\nThere are only {number_of_verses} verses in {list.clean(book).title()}:{chapter}\n\ndefualted to 1\n","red"))
          verse = 1
        else:
          verse = int(user)   
      else: 
        print(colored("\nNon-numeric characters defualt to 1\n","red"))
        verse = 1
      if verse and chapter:
        print(colored(CV.get_verse(book,chapter,verse),"white"))
      if chapter and not verse:
        outchap = CV.get_chap(book,chapter)
        for o in outchap:
          print(colored(o,"white"))
      if not chapter and  not verse:
        print(colored(open(book).read(),"white"))
      if verse and not chapter:
        print(colored(CV.get_verse(book,1,verse),"white"))