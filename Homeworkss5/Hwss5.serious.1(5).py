def remove_dollar_sign(s):
    s = s.translate({ord("$"): None}) # Unicode line
    return s

s = input("Enter a string with the dollar symbol($) in it: ")
print(remove_dollar_sign(s))
