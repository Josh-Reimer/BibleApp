files = ["genesis", "exodus", "leviticus", "numbers", "deuteronomy", "joshua", "judges", "ruth", "first_samuel", "second_samuel", "first_kings", "second_kings", "first_chronicles", "second_chronicles", "ezra", "nehemiah", "esther", "job", "psalms", "proverbs", "eccliasiastes", "song_of_solomon", "isaiah", "jeremiah", "lamentations", "ezekial", "daniel", "hosea", "joel", "amos", "obadiah", "jonah", "micah", "nahum", "habakkuk", "zephaniah", "haggai", "zechariah", "malachi", "matthew", "mark", "luke", "john", "acts", "romans", "first_corinthians", "second_corinthians", "galatians", "ephesians", "philippians", "colossians", "first_thessalonians", "second_thessalonians", "first_timothy", "second_timothy", "titus", "philemon", "hebrews", "james", "first_peter", "second_peter", "first_john", "second_john", "third_john", "jude", "revelation"]
bible = open("Bible.txt", "w")
for file in files:
  every = open(f"{file}.txt", "r")
  bible.write(every.read())
bible.close()