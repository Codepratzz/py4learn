# All the regex functions in Python are in the import re module.
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # passing the regular exp to compile and save in
mo = phoneNumRegex.search('My number is 415-555-4242.')  # passing the string to search for a particular match
print('Phone number found: ' + mo.group())

# grouping can be done through adding parantheses () in the regular exp
phoneNumRegex1 = re.compile(r'(\(\d\d\d\d\))-(\d\d\d\d\d\d)')  # passing the regular exp to compile and save in
mo1 = phoneNumRegex1.search('My number is (0535)-202511.')  # passing the string to search for a particular match
# areaCode, phoneno = mo.groups() # it wil return a tuple
print(mo1.group(1), mo1.group(2))

# -------------------------------------------------153---------------------------------------------------------------
heroRegex = re.compile(r'Batman|Tina Fey')
mo2 = heroRegex.search('Batman and Tina Fey.')
mo4 = heroRegex.search('baba ji ka thullu')
print(mo2.group(), mo4)
# The character is called a | pipe. You can use it anywhere you want to match one | of many expressions. For example,
# the regular expression r'Batman|Tina Fey' will match either or Fey'. 'Batman''Tina
# -------------------------------------------------------find all 158--------------------------------
phoneNumRegex2 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
mo3 = phoneNumRegex2.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo3)  # returns a list object

xmasRegex = re.compile(r'\d+\s\w+')  # start with digit then space and then worf
xmas = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7'
                         'swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(xmas)

# ----------------------------------------------------159------------------------------------------------------------
"""
Making Your Own Character Classes There are times when you want to match a set of characters but the shorthand
character classes (\d, \w, \s, and so on) are too broad. You can define
your own character class using square brackets.
"""

# -----------------------------caret and dollar charater--------------------------
vowelRegex1 = re.compile(r'[^aeiouAEIOU]')  # ^ other than aeiou--
vowel1 = vowelRegex1.findall('RoboCop eats baby food. BABY FOOD.')
print(vowel1)
