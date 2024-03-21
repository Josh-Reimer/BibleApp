from binary_search import binary_search
import ChapterVerse as CV
from BibleFileNames import files
import list_and_str_ops as list 
from charEliminator import onlyVerses,remove_only_chars
import sys
import os

colorful = True

try:
	import colorama
	from colorama import init
	from termcolor import colored
except:
	colorful = False
	print("for a colored terminal, use pip to install colorama and termcolor")
'''
DO NOT DELETE!
Currently, connector.py is the final version of the command
line BibleApp.
It is a coloured version.
'''

os.system('cls' if os.name == 'nt' else 'clear') # multi-platform clear statement
if colorful:
	print(colored('Welcome to the python Bible App!','red'))	
	print(colored('With this application you can do the following things:','cyan'))
	print(colored('1.search the Bible for keywords or phrases\n2.navigate to a specific scriptual reference\n3.print an entire book or chapter to the screen','magenta', attrs=['bold']))
else:
	print('Welcome to the python Bible App!')
	print('With this application you can do the following things:')
	print('1.search the Bible for keywords or phrases\n2.navigate to a specific scriptual reference\n3.print an entire book or chapter to the screen')
print('\nto search type "search"\nto navigate to specific references, type "ref"\nafter each command press enter to see results\nat any time type exit() to go back to command prompt or exit application\n')
while True:
    appfunction = input('what do you want to do?\n-->')
    if appfunction == 'search':
        def clean(str):
          str = list.remove_underscore(str)
          halves = str.split(".")
          return str.replace(str, halves[0].title())
        while True:
          search_input = input("Bible Search\n-->")
          if search_input == "exit()":
            break
          multiple_results = []
          verses = ""
          for book in files:
            verses = open(book).readlines()
            book = clean(book)
            for verse in verses:
              if search_input.lower() in verse.lower(): 
                multiple_results.append(f"{book}\n{verse}")
          for result in multiple_results:
            print(f"{result}\n")
          if len(multiple_results) == 0:
            print(f"no results found for '{search_input}'")
          elif len(multiple_results) == 1:
            print(f"{len(multiple_results)} result found for '{search_input}'")
          else:  
            print(f"{len(multiple_results)} results found for '{search_input}'")            
          continue
    elif appfunction == 'ref':
        result2 = False
        book2 = False
        chapter = False
        verse = False
        while True:
          user = input("Book?\n-->")
          user = user.replace(" ", "").lower()
          if user == "exit()":
            break
          for file in files:
            if user != list.clean(file):
              continue
            if list.clean(file) in user:
              book2 = list.disclean(user)
            else:
              continue
            user = input("Chapter?\n-->")
            user = user.replace(" ", "")
            if user == "exit()":
              sys.exit()
            if user.lower() == "n":
              chapter = False
            elif user.isdigit():
              noNums = remove_only_chars(open(book2).readlines())
              for v in noNums:
                length = noNums[-1].split(":")[0]
                if int(user) > int(length):        
                  print(f"\nthere are only {int(length)} chapters in {list.clean(book2)}\n\ndefualted to 1\n")
                  chapter = 1
                  break
                else:
                  chapter = int(user)
            else:
              print("\nNon-numeric characters defualt to 1\n")
              chapter = 1
            user = input("Verse?\n-->")
            user = user.replace(" ","")
            if user == "exit()":
              sys.exit()
            if user.lower() == "n":
              verse = False
            elif user.isdigit():
              number_of_verses = len(CV.get_chap(book2,chapter))
              if int(user) > number_of_verses:
                print(f"\nThere are only {number_of_verses} verses in {list.clean(book).title()}:{chapter}\n\ndefualted to 1\n")
                verse = 1
              else:
                verse = int(user)   
            else: 
              print("\nNon-numeric characters defualt to 1\n")
              verse = 1
            if verse and chapter:
              print(CV.get_verse(book2,chapter,verse))
            if chapter and not verse:
              outchap = CV.get_chap(book2,chapter)
              for o in outchap:
                print(o)
            if not chapter and  not verse:
              print(open(book2).read())
            if verse and not chapter:
              print(CV.get_verse(book2,1,verse))
    elif appfunction == 'exit' or appfunction == 'exit()':
      sys.exit()