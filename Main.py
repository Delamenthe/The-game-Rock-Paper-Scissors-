import sys
import secrets
import hashlib, hmac
from prettytable import PrettyTable
import copy


class Table:
    def generateTable (self, args):
        names = copy.copy(args)
        names.insert(0," ")
        table_of_moves = PrettyTable()
        table_of_moves.field_names = names
        size=len(args)
        rez=[["Lose" for j in range(size)] for i in range(len(args))]
        k=(size-1)/2
        for i in range(size):
            for j in range(size):
                if i==j: rez[i][j]='Draw'
                elif i>j+k or (j > i > j - k - 1): rez[i][j]= 'Win'

        for i in range(size):
            rez[i].insert(0,args[i])
            table_of_moves.add_row(rez[i])
        return table_of_moves


class Main:
    args = sys.argv
    args.pop(0)
    table = Table()
    print(table.generateTable(args))


    if len(args) < 3:
        print("Error! The number of arguments cannot be less than 3. Please enter more arguments")
        exit()
    elif not len(args) & 1:
        print("Error! The number of arguments cannot be even. Please enter an odd number of arguments")
        exit()
    else:
        for i in args:
            if args.count(i) > 1:
                print("Error! Arguments should not be repeated. Please change the list of arguments")
                exit()
    print('\nComputers move:')
    s = secrets.choice(args)
    h = hmac.new(s.encode(), None, hashlib.sha256)
    print(h.hexdigest().upper())

    print('\nYour turn. Please, select the move number from the list below:')
    while True:
        for i in range(len(args)):
            print(i + 1, '. ', args[i], sep='')
        moveNumStr = input("Move number:")
        try:
            int(moveNumStr)
            moveNum = int(moveNumStr)
        except ValueError:
            print('Error! Not a number is entered. Please enter the move number from the list below:')
            continue
        if moveNum < 0 or moveNum > len(args):
            print('Error! You are enter not a number', moveNum,
                  '. Please select the option number from the menu list. For example \"1\"')
            continue
        else:
            print('Your move:', args[moveNum - 1])
            exit()
