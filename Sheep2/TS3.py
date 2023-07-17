from gasp.utils import read_number
from gasp.utils import read_yesorno
from collections import Counter
from random import randint
on = True
l1 =[]
x = l1
l2 =[]
y = l2

#quickGame
def op1 ():
    while on == True:
        print("great\nplease enter you 6 numbers(s), within the number 40")
        for i in range(0,6):
            k = int(input())
            l1.append(k)
        for i in range(0,6):
            k1 = randint(0,40)
            l2.append(k1)
        print("the random numbers were " + str(l2))
        acc()
        if read_yesorno("would you like to play agian?"):
            print("ok")
        else:
            print("thanks for playing")
            break


def gm2():
    while on == True:
        print("great\nplease enter you 8 numbers(s), within the number 40")
        for i in range(0,8):
           k = int(input())
           l1.append(k)
        for i in range(0,8):
            k1 = randint(0,80)              
            l2.append(k1)
        print("the random numbers were " + str(l2))
        acc()
        if read_yesorno("would you like to play agian?"):
            print("ok")
        else:
            print("thanks for playing")
            break

def acc():
    c1 = Counter(l1)
    c2 = Counter(l2)
    c3 = list((c1 & c2).elements())
    c5 = len(c3) / len(set(l1 + l2))*100
    print("you had an accuracy of " + str(c5) + "%")

#finished
def stp():
    print("then i'm afriad we have nothing left to offer you.")
    SystemExit()

#longGame
def op2():
    if read_yesorno("would you prefer a long game?"):
        gm2()
    else:
        stp()

#start
print()
print("welcome back to the VA lottery\nplease make a selection")
if read_yesorno("would you like to play a quick game?"):
    op1()
else: 
    op2() 