# ---------------------------------------------------------- Double Quotes 124-------------------------------
# Strings can begin and end with double quotes, just as they do with single quotes. One benefit of using double quotes
# is that the string can have a single quote character in it
spam = "this is prateek's python"
print(spam)
# A raw string completely ignores all escape characters and prints any backslash that appears in the string
print(r'That is Carol\'s cat.')

"""
A multiline string in Python begins and ends with either three single quotes or three double quotes. Any quotes,
tabs, or newlines in between the “triple quotes” are considered part of the string.
"""

aba = ''' hi this prateek, i am in a deep
 trouble, but can not expresed to an
 one'''
print(aba)

# --------------------------------------------------------------strings method 128-------------------------------
# The upper(), lower(), isupper(boolean values), and islower(boolean values) String Methods that these methods do not change the string itself but return
# new string values. If you want to change the original string, you have to call or
# on the string and then assign the new string to the upper() lower() variable where the original was stored.

aba = aba.upper()
print(aba)
print(aba.islower())

"""
isalpha()---- returns True if the string consists only of letters and is not blank.
• isalnum() ---returns True if the string consists only of letters and numbers
and is not blank.
• isdecimal() --returns True if the string consists only of numeric characters
and is not blank.
isspace() returns True if the string consists only of spaces, tabs, and newlines
and is not blank.
• istitle() returns True if the string consists only of words that begin with
an uppercase letter followed by only lowercase letters.
"""
print(aba.isalnum(), aba.isalpha(), aba.isdecimal(), aba.istitle())

# -------------------------------------------------------------------------------------------------------------
"""
The startswith() and endswith() String Methods
The startswith() and endswith() methods return True if the string value they
are called on begins or ends (respectively) with the string passed to the
method; otherwise, they return False
"""
print(aba.startswith('hi'))  # case sensitive
# The join() and split() String Methods 131-- return always a list
# Copying and Pasting Strings with the pyperclip Module        135---------------------------------
"""
The pyperclip module has copy() and paste() functions that can send text
to and receive text from your computer’s clipboard Pyperclip does not come with Python.imprt it
"""
import pyperclip

print(pyperclip.paste())
