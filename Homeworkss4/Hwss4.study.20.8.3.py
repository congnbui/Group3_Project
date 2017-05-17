
# alice_words.py

import re
import string

# import alice_text.txt and turn it into a string, of which each item is a word from the text
alice_w = []
with open("alice_text.txt","r") as alice:
    for line in alice:
        for word in line.split():
            word = word.lower()
            word = " ".join(re.findall("[a-z]+", word)) # extracting only characters(letters) from word
            if word != "":
                alice_w.append(word)
          
# count the words

alice_counts = {}

for word in alice_w:
    alice_counts[word] = alice_counts.get(word, 0) + 1

alice_items = list(alice_counts.items())
alice_items.sort()

x = 20 # the number of spaces. Indent perfectly in Pythonshell but fail to work in text file :((

with open("alice_words.txt","w") as f:
    f.write("Word{0}Count\n".format(" "*(x-9)))
    f.write("="*x + "\n")
    for word, number in alice_items:
        f.write(word + " "*(x-len(word)-len(str(number))) + str(number) + "\n")

print("'alice' word appears {0} times in the story".format(alice_counts["alice"]))
    



