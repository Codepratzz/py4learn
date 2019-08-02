# Like a list, a dictionary is a collection of many values. But unlike indexes for
# lists, indexes for dictionaries can use many different data types, not just
# integers. Indexes for dictionaries are called keys, and a key with its associated
# value is called a key-value pair.
from typing import Dict, Union

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}  # combiantion of key value pair and each key value pair
# called as item

# -------------------------------------------------Dictionaries vs. Lists pn-106----------------------------------------
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)

# While the order of items matters for determining whether two lists are the same, it does not matter in what
# order the key-value pairs are typed in a dictionary. Because dictionaries are not ordered, they can’t be sliced
# like lists

# -------------------------------------The keys(), values(), and items() Methods pn 307--------------------------------
# There are three dictionary methods that will return list-like values of the dictionary’s keys, values, or both keys
# and values: keys(), values(), and items(). The values returned by these methods are not true lists: They cannot be
# modified and do not have an append() method.

for key in eggs.keys():
    print('key vlue =', key)
for value in eggs.values():
    print('values =', value)
for items in eggs.items():  # return the tupels as item : list(items) returns as the list
    print('items in ', list(items))
# You can also use the multiple assignment trick in a loop to assign forthe key and value to separate variables.
# Enter the following into the inter active shell:
# can Check Whether a Key or Value Exists in a Dictionary like itme in dicitonary or not in

# ----------------------------------------The get() Method 109----------------------------------------------------------
# It’s tedious to check whether a key exists in a dictionary before accessing
# that key’s value. Fortunately, dictionaries have a get() method that takes two
# arguments: the key of the value to retrieve and a fallback value to return if
# that key does not exist.Because there is no 'eggs' key in the picnicItems dictionary, the default
# value 0 is returned by the get() method. Without using get(), the code
# would have caused an error message
picnicItems = {'apples': 4, 'eggs': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# --------------------------The setdefault() Method-----------------------------------------------------------
# You’ll often have to set a value in a dictionary for a certain key only if that
# key does not already have a value.
spam1: Dict[str, Union[str, int]] = {'name': 'Pooka', 'age': 5}
print(spam1.setdefault('color', 'black'))
print(spam1)

# ----------------------------------------------Pretty Printing------------------------------
# This is helpful when you want a cleaner display of the items in a dictionary than what print() provides------------
#  compare list values with dictionary keys and make a new dictionary of it using python
lis = ('name', 'color')
item_generator = {k: spam1[k] for k in lis if k in spam1}
print(item_generator)
print(list(item_generator.values()))  # converting dictionary values into the list
