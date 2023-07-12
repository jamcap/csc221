from gasp.utils import read_number
from gasp.utils import read_yesorno
from random import randint

print()
print("welcome back to the VA lottery") 
print("please make a selection")
if read_yesorno("would you like to play a quick game?"):
    print("great")
else: 
    print("would you prefer a long game?")