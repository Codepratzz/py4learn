assign = 40  # no need to typecast me, i am self independent to do so
assign2 = 'I told my friend, "Python is my favorite language!"'  # A string is simply a series of characters.
# -------------------------------------------------------------------------------------------------------------------------
# Anything inside quotes is considered
# a string in Python, and you can use single or double quotes around your strings like this:
print('assign variable is = ', assign,
      'variable string =', assign2)
print('Hello world!')
print('What is your name?')  # ask for their name
myName = input()  # always return the values as strings
print('It is good to meet you, ' + myName)  # Python uses the plus symbol (+) to combine/concatenate strings.
print('The length of your name is:')
print(len(myName))
print('What is your age?')  # ask for their age
# myAge = input() print('You will be ' + str(int(myAge) + 1) + ' in a year.')
# -------------------------------------------------------------------------------------------------------------------------
# print allows you to print the values
# in either int or string The str(), int(), and float() Functions convert one type of variable into another type of
# variable method is an action that Python can perform on a piece of data. The dot (.) after name in name.title()
# tells Python to make the title() method act on the variable name. Every method is followed by a set of parentheses,
# because methods often need additional information to do their work. That information is provided inside the
# parentheses.
#  -------------------------------------------------------------------------------------------------------------------------
print(assign2.title())
print(assign2.upper())
# In programming, whitespace refers to any nonprinting character, such as
# spaces, tabs, and end-of-line symbols.
print("Languages:\nPython\n\tC\nJavaScript")
# -------------------------------------------------------------------------------------------------------------------------
favorite_language = ' pyt\'hon '
print(len(favorite_language), favorite_language.rstrip())
print(len(favorite_language), favorite_language.lstrip())
print(len(favorite_language), favorite_language.strip())
# In this example, we start with a value that has whitespace at the beginning
# and the end u. We then remove the extra space from the right side
# at v, from the left side at w, and from both sides at x
# -------------------------------------------------------------------------------------------------------
print('Hello', end='')  # when you dont want to create a new line inn printing
print('World')
