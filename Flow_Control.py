#  Conditions always evaluate down to a Boolean value, True or False.
#  Blocks of Code
# Lines of Python code can be grouped together in blocks. You can tell when a block begins and ends from
# the indentation of the lines of code. There are three rules for blocks.
# 1. Blocks begin when the indentation increases.
# 2. Blocks can contain other blocks.
# 3. Blocks end when the indentation decreases to zero or to a containing block’s indentation.
# if-else statment plus elif (else if - to recheck another conditions) When there is a chain of elif statements, only one or none of the
# clauses will be executed. Once one of the statements’ conditions is found
# to be True, the rest of the elif clauses are automatically skipped. When there is a chain of elif statements,
# only one or none of the clauses will be executed. Once one of the statements’ conditions is found
# to be True, the rest of the elif clauses are automatically skipped.
# -------------------------------------------------------------------------------------------------------------------------------
spam = 0
while spam < 5:  # block starts
    print('Hello, world.')
    spam = spam + 1  # block ends
# ------------------------------------------------with break and continue-------------------------------------------------------
while False:
    print('Please type your name.')  # block starts
    name = input()  # same block
    if name == 'your name':  # 2nd block starts
        break  # 2nd block
    if name == 'prateek':
        continue
print('Thank you!')  # blocks ends
# -----------------------------------------------for Loops and the range() Function----------------------------------------------
# Some functions can be called with multiple arguments separated by a comma, and range() is one of them. range(start,end, steps)
for i in range(0, 10, 2):
    print(i)

# ------------------------------------------------IMPORTING---------------------------------------------------------------------
import random  # random is a library which contain several modules of similar type
import sys  # multiple calling of libraries

for i in range(5):
    print(random.randint(1, 10))

# ------------------------------------------------IMPORTING---------------------------------------------------------------------
# from import Statements An alternative form of the import statement is composed of the from keyword,
# followed by the module name, the import keyword, and a star; for example, from random import *.With this form of import statement,
# calls to functions in random will not need the random. prefix. However, using the full name makes for more readablecode,
# so it is better to use the normal form of the import statement.
# -------------------------------------------Ending a Program Early with sys.exit()-----------------------------------------------
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
print('You typed ' + response + '.')  # no working of this statement
# -------------------------------------------------------------------------------------------------------------------
