import random

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ''
                                                                             '', 'mid-R': ' ', 'low-L': ' ',
            'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'
for i in random.randint(1, 9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = printBoard(i)
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)

if (theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] == 'X') or (theBoard['top-L'] == theBoard['top-M']
                                                                            == theBoard['top-R'] == 'O'):
    print('you won the match')
