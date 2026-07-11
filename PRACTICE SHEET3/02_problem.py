# write a program to fill in a letter template given below with name and date.
#letter ='''Dear <|NAME|>,
#You are selected!
#Date: <|DATE|>'''

letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''

print(letter.replace("<|NAME|>", "esha").replace("<|DATE|>", "12/06/2024"))

