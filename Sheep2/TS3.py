from gasp.utils import read_number
from gasp.utils import read_yesorno
from random import randint

def gm1 ():
    print("great\n please enter you 6 digit(s), within the number 40")
    l1 = []
    for i in range(0,6):
        k = int(input)
        l1.append(k)

def stp():
    print("then i'm afriad we have nothing left ot offer you.")
    SystemExit()

def op1():
    if read_yesorno("would you prefer a long game?"):
        print("great")
    else:
        stp()

print()
print("welcome back to the VA lottery") 
print("please make a selection")
if read_yesorno("would you like to play a quick game?"):
    gm1()
else: 
    op1() 