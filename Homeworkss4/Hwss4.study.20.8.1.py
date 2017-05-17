import string

string_to_read = input("Input a string: ")
string_to_read = string_to_read.lower()
string_to_read = string_to_read.replace(" ","")

# Using string

##for letter in string.ascii_lowercase:
##    if string_to_read.count(letter)>0:
##        print(letter,"  ",string_to_read.count(letter))


# Using dictionary

letter_counts ={}
for letter in string_to_read:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

letter_items = list(letter_counts.items())
letter_items.sort()

for letter, number in letter_items:
    print(letter,"  ",number)


