from random import randint
from collections import Counter
print("welcome to the VA lottery")
q1 = 23, 45, 78 ,94, 35, 76
print("example " + str(q1))
ul = []
print("Please enter your six sets of two digits")
for i in range(0,6):
    ky = int(input())
    ul.append(ky)

print()
rl = []
for i in range(0,6):
    k = randint(10,99)
    rl.append(k)
print("the winning numbers were " + str(rl))

print()
cla = Counter(ul)
clo = Counter(rl)
cn = list((cla & clo).elements())
pc = len(cn) / len(set(ul + rl))*100
print("your ticket had an accuracy of " + str(pc) + "%")

print()
if pc >= 15.00:
    print("your entry qualfies for a $20 return")
else:
    print("your ticket does not qualify for a $20 return")
