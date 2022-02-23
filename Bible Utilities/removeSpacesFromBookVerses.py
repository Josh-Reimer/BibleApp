from BibleFileNames import files
from list_and_str_ops import join as join

results = []

File = input("book?\n-->")
verses = open(f"{File}.txt").readlines()
  
for verse in verses:
    
  if verse[0] == " ":
      
    verse = verse[1:len(verse)] 
    results.append(f"{verse}")


new_book = open(f"{File}.txt","w")

for result in results:
  new_book.write(f"{result}")
print(results)
