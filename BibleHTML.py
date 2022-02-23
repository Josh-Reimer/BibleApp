'''
I used this script to take the Bible text files and convert them into
an html equivalent.
Adjust to your needs!
DO NOT DELETE!
'''
from BibleFileNames import files
for file in files:
  bible = open(f"{file}")
  site = open(f"web-{file.replace('.txt','')}.html","w")

  verses = bible.readlines()
  site.write('<!DOCTYPE html>\n<html>\n<head>\n<style>\nbody{\nbackground:linear-gradient(-90deg,#4e4444,#605d5d,grey);\n}\np{\nfont-family:monospace;\ncolor:black;\n}\ninput{\nbackground-color:black;\ndisplay:block;\nborder-radius:30px;\nmargin:auto;\nwidth:50%;\ncolor:white;\ntext-align:center;\n}\n</style>\n</head>\n<body>\n<input id="search" type="search" onfocus="this.value=''" value="search">\n')
  for verse in verses:
    site.write(f"<p>{verse}</p>")
  site.write("\n</body>\n</html>")
  site.close()
  bible.close()