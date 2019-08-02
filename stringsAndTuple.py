# Lists aren’t the only data types that represent ordered sequences of values.
# For example, strings and lists are actually similar, if you consider a string to
# be a “list” of single text characters.A list value is a mutable
# data type: It can have values added, removed, or changed. However, a string
# is immutable: It cannot be changed. The proper way to “mutate” a string is to use slicing and concatenation
# to build a new string by copying from parts of the old string. Enter the following into the interactive shell:
# Lists are useful data types since they allow you to write code that works on a
# modifiable number of values in a single variable. Later in this book, you will
# see programs using lists to do things that would be difficult or impossible to
# do without them.
# Lists are mutable, meaning that their contents can change. Tuples and
# strings, although list-like in some respects, are immutable and cannot be
# changed. A variable that contains a tuple or string value can be overwritten
# with a new tuple or string value, but this is not the same thing as modifying
# the existing value in place—like, say, the append() or remove() methods do on
# lists.
# Variables do not store list values directly; they store references to lists.
# This is an important distinction when copying variables or passing lists as
# arguments in function calls. Because the value that is being copied is the
# list reference, be aware that any changes you make to the list might impact
# another variable in your program. You can use copy() or deepcopy() if you
# want to make changes to a list in one variable without modifying the original
# list.

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName)

# ---------------------------------------------tuple-------------------------------------------------------------------
# The tuple data type is almost identical to the list data type, except in two ways. First, tuples are typed
# with parentheses, ( and ), instead of square brackets, [ and ]. But the main way that tuples are different
# from lists is that tuples, like strings, are immutable.Tuples cannot have their values modified, appended, or removed.
eggs = ('hello', 12, 14)
print(eggs[0])
# If you have only one value in your tuple, you can indicate this by placing a trailing comma after the value inside
# the parentheses. Otherwise, Python will think you’ve just typed a value inside regular parentheses
print(type(('hello',)), type(('hello')))

# ----------------------------------------converting tuple list string--------------------------------------------------
print(tuple(['cat', 'dog', 5]), list(('cat', 'dog', 5)), list('hello'))


# ----------------------------------------Passing References-----------------------------------------------------------
def eggs1(someParameter):
    someParameter.append('Hello')


spam = [1, 2, 3]
eggs1(spam)
print(spam)

# -----------------------------------------The copy Module’s copy() and deepcopy() Functions pn-100---------------------
# Although passing around references is often the handiest way to deal with lists and dictionaries, if the function
# modifies the list or dictionary that is passed, you may not want these changes in the original list or dictionary
# value. For this, Python provides a module named copy that provides both the copy() and deepcopy() functions.
import copy

spam4 = ['A', 'B', [4, 2, 2], 'C', 'D']
cheese = copy.copy(spam4)
cheese[1] = 42
print(spam4, cheese)

# If the list you need to copy contains lists, then use the copy.deepcopy() function instead of copy.copy().
# The deepcopy() function will copy these inner lists as well.
cheese1 = copy.deepcopy(spam4)
cheese1[2][1] = 'hello'
print(cheese1)
