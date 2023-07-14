from gasp.utils import read_number
from gasp.utils import read_yesorno
from random import randint

#quickGame
def op1 ():
    print("great\nplease enter you 6 digit(s), within the number 40")
    l1 = []
    for i in range(0,6):
        k = int(input())
        l1.append(k)

#finishOne
def stp():
    print("then i'm afriad we have nothing left to offer you.")
    SystemExit()

#longGame
def op2():
    if read_yesorno("would you prefer a long game?"):
        print("great")
    else:
        stp()

#start
print()
print("welcome back to the VA lottery\nplease make a selection")
if read_yesorno("would you like to play a quick game?"):
    op1()
else: 
    op2() 