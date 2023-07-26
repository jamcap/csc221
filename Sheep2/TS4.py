from gasp import *
from random import randint
import time

def place_player():
  global u_x, u_y, u_shape
  u_x = randint(0, 63)
  u_y = randint(0, 47)
  u_shape = (Circle((10*u_x+5,10*u_y+5),10, filled=True, color="#00FF00"))

def move_player():
  global u_x, u_y, u_shape
 
  key = update_when('key_pressed')
  if key == 't':
   u_x += 1
   u_y += 0
  elif key == 'g':
    u_x += 1
    u_y += 1
  elif key == 'b':
    u_x += 0
    u_y += 1
  elif key == 'v':
    u_x -= 1
    u_y += 1
  elif key == 'c':
    u_x -= 1
    u_y += 0
  elif key == 'd':
    u_x -= 1
    u_y -= 1
  elif key == 'e':
    u_x -= 0
    u_y -= 1
  elif key == 'r':
    u_x += 1
    u_y += 1
  move_to(u_shape, ((10*u_x+5,10*u_y+5)))

def pas():
  time.sleep(5)

begin_graphics()  
finished = False
place_player()
while not finished:
  move_player()
#key_text = Text("a", (320, 240), size=48)

end_graphics()