import list_and_str_ops as list
from BibleFileNames import files
import sys
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

#function above code below
def searchBible():
  while True:
    search_input = input("Bible Search\n-->")
    if search_input == "exit()":
      sys.exit()
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