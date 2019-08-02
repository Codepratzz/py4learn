# -----------------------------A function is like a mini-program within a program.-----------------------------------
# def statement, which defines a function named
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')


hello()


def hello(name):
    print('Hello ' + name)


hello('prateek')

# -----------------------------Return Values and return Statements------------------------------------------------
# In general, the value that a function call evaluates to is called the return value of the function.
from random import *


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'


r = randint(1, 5)  # whenever r = 5 this program return a none value which is  only value of the NoneType data type
fortune = getAnswer(r)
print(fortune)
