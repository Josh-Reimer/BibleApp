while True:
  book = input("input book of the Bible\n:")
  try:
    with open(f"{book}.txt",     mode='r') as f:
      content = f.read()
      print(content)
  except:
    print(f"{book} is not a book of the Bible\n")
  continue    

'''
try except probably is probably not best practice but
it sure makes this a lot simpler!
I had a lot of trouble with not using try except
back when I first started with the command line version
of the BibleApp.
I am writing this as of Feb. 15,2022 but this file is much older than that.
KEEP THIS FILE -- DO NOT DELETE!!!
'''