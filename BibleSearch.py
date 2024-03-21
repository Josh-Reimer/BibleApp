import list_and_str_ops as list
from binary_search import binary_search
from BibleFileNames import files

colorful = True
#this variable stores the state of the colored terminal, for example whether the text is colored or not

try:
	from colorama import init
	from termcolor import colored 
	init()
except:
	colorful = False
	print("for a colored terminal, use pip to install colorama and termcolor")
'''The BibleSearch.py file is the colored version of the command line version
of the BibleApp.DO NOT DELETE!
'''
def clean(str):
  str = list.remove_underscore(str)
  halves = str.split(".")
  return str.replace(str, halves[0].title())

  

while True:
  if colorful:
  	search_input = input(colored("Bible Search\n-->","grey","on_white"))
  else:
  	search_input = input("Bible Search\n-->")
  if search_input == "exit()":
    break
  multiple_results = []
  verses = ""
  for book in files:
    #if search_input == f"#{clean(book).lower()}":
#      files = files[:files[f"{book}.txt"]
    verses = open(book).readlines()
    book = clean(book)
    for verse in verses:
      if search_input.lower() in verse.lower(): 
        multiple_results.append(f"{book}\n{verse}")
  for result in multiple_results:
   if colorful:
   	print(colored(f"{result}\n","white"))
   else:
   	print(f"{result}\n")
  if len(multiple_results) == 0:
    if colorful:
    	print(colored(f"no results found for '{search_input}'","red"))
    else:
    	print(f"no result found for {search_input}")
  elif len(multiple_results) == 1:
      if colorful:
      	print(colored(f"{len(multiple_results)} result found for '{search_input}'","green"))
      else:
      	print(f"{len(multiple_results)} result found for '{search_input}'")
  else:
    if colorful:  
    	print(colored(f"{len(multiple_results)} results found for '{search_input}'","green"))
    else:
    	print(f"{len(multiple_results)} results found for '{search_input}'")
  continue