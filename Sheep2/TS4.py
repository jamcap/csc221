from gasp import *
from random import randint
import time

u_x = randint(0, 63)
u_y = randint(0, 47)

def place_player():
     global c
     c = Circle((10 * u_x + 5, 10 * u_y + 5), 10, filled=True, color= "#008000")

def move_player():
    global u_x, u_y
    while True:
        key = update_when('key_pressed')
        if key == '1':
            u_x += 1
            u_y += 0
        elif key == '2':
            u_x += 1
            u_y += 1
            if key == '3':
                u_x += 0
                u_y += 1
            if key == '4':
                u_x -= 1
                u_y += 1
            if key == '5':
                u_x -= 1
                u_y += 0
            if key == '6':
                u_x -= 1
                u_y -= 1
            if key == '7':
                u_x -= 0
                u_y -= 1
            if key == '8':
                u_x += 1
                u_y += 1

def pas():
    time.sleep(5)

begin_graphics()  
c = Circle((320, 200), 10, filled=True, color="#FFFF00")
place_player()
move_player()
#key_text = Text("a", (320, 240), size=48)

end_graphics()