# A list is a value that contains multiple values in an ordered sequence.
spam = ['cat', 'bat', 'Rat',
        'elephant']  # spam is list type variable which contains 4 values and starts from spam[0]-spam[3] like array C
spam1 = [['cat', 'bat'], [10, 20, 30, 40, 50]]  # list containing another list like 2d array
print(spam[0], spam1[0], spam1[0][1])
#  While indexes start at and go up, you can also use negative integers for 0 the index. The integer value
# refers to the last index in a list, the value -1 -2 refers to the second-to-last index in a list, and so on. Enter
print(spam[-2], spam1[-1], spam1[-1][0])

# -----------------------------------Getting Sublists with Slices---------------------------------------------------
# Just as an index can get a single value from a list, a slice can get several values rom a list,
# in the form of a new list. A slice goes up to, but will not include, the value at the second index. A
print(spam[0:4], spam[:4], spam[:], spam1[0:])

# -------------------------------------------------------------------------------------------------------------
spam3 = spam + spam1  # concatenating 2 lists
print(spam3)
spam3[4][0] = 'donkey'  # changing the values into list
print(spam3)
spam3 = spam3 * 2  # duplicating the list
print(spam3)
del spam3[len(spam3) - 2]  # deleting an element
print(spam3)

# -------------------------------------------------------------------------------------------------------------
# You can determine whether a value is or isn’t in a list with the in and not in operators.
print('horse' not in spam3)
print('cat' not in spam3)
# The multiple assignment trick is a shortcut that lets you assign multiple variables
# with the values in a list in one line of code
cat = ['fat', 'black', 'loud']
size, color, disposition = cat  # kind of enumeration
print(cat)
print(size)
# Finding a Value in a List with the index() Method
print(spam3.index('bat'))
# The previous append() method call adds the argument to the end of
# the list. The insert() method can insert a value at any index in the list
spam.append('horse')
spam.insert(2, 'jaguar')
print(spam)

# -------------------------------------------------------------------------------------------------------------
# Sorting the Values in a List with the sort() Method by default ascending
spam.sort(reverse=True)
print(spam)
# Second, you cannot sort lists that have both number values and string values in them, since Python doesn’t know how to
# compare these values. Type the following into the interactive shell and notice the error  TypeError
spam.sort(key=str.lower)
print(spam)
