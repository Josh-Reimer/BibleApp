import list_and_str_ops as list
from binary_search import binary_search
from BibleFileNames import files
from colorama import init
from termcolor import colored 
init()
'''The BibleSearch.py file is the colored version of the command line version
of the BibleApp.DO NOT DELETE!
'''
def clean(str):
  str = list.remove_underscore(str)
  halves = str.split(".")
  return str.replace(str, halves[0].title())

  

while True:
  search_input = input(colored("Bible Search\n-->","grey","on_white"))
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
   print(colored(f"{result}\n","white"))
  if len(multiple_results) == 0:
    print(colored(f"no results found for '{search_input}'","red"))
  elif len(multiple_results) == 1:
      print(colored(f"{len(multiple_results)} result found for '{search_input}'","green"))
  else:  
    print(colored(f"{len(multiple_results)} results found for '{search_input}'","green"))
  continue