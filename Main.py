import sys
import secrets
import hashlib, hmac
from random import random

from prettytable import PrettyTable
import copy


class Table:
    def generate_table (self, args, size, rez):
        names = copy.copy(args)
        names.insert(0," ")
        table_of_moves = PrettyTable()
        table_of_moves.field_names = names
        for i in range(size):
            rez[i].insert(0,args[i])
            table_of_moves.add_row(rez[i])
        return table_of_moves

class Rules:
    def def_rules (self,args,size):
        rez=[["Lose" for j in range(size)] for i in range(len(args))]
        k=(size-1)/2
        for i in range(size):
            for j in range(size):
                if i==j: rez[i][j]='Draw'
                elif i>j+k or (j > i > j - k - 1): rez[i][j]= 'Win'
        return rez
class Encryption:
    key=0
    def hmac_calculate(self,move):
        key=secrets.randbits(256)
        unity=str(key)+move
        h = hashlib.sha3_256(unity.encode())
        print(h.hexdigest().upper())
        return key
class Main:
    args = sys.argv
    args.pop(0)

    rules = Rules()
    rezult=rules.def_rules(args,len(args))

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

    while True:
        print('\nComputers move:')
        computers_move = 'Rock'
        crypt = Encryption()
        key=crypt.hmac_calculate(computers_move)

        print('\nYour turn. Please, select the move number from the list below:')
        print('0 - exit')
        for i in range(len(args)):
            print(i + 1, '-', args[i])
        print('? - help')
        moveNumStr = input("Enter you move:")
        if moveNumStr=='0': exit()
        elif moveNumStr=='?':
            table = Table()
            print(table.generate_table(args,len(args),rezult))
        else:
            try:
                int(moveNumStr)
                moveNum = int(moveNumStr)
            except ValueError:
                print('Error! Not a number is entered.')
                continue
            if moveNum < 0 or moveNum > len(args):
                print('Error! There is no a number', moveNum,
                      'in the list. Please select the option number from the menu list. For example \"1\"')
                continue
            else:
                print('Your move:', args[moveNum - 1])
                print(rezult[args.index(computers_move)][moveNum-1])
                print('Computers move:', computers_move)
                print('Source key:', key)

