from gasp import *
from random import randint
import time

u_x = randint(0, 63)
u_y = randint(0, 47)

def move_player():
  global u_x, u_y, u_shape
  u_shape = (Circle((5*u_x,5*u_y),10, filled=True, color="#00FF00"))

  key = update_when('key_pressed')
  if key == 't':
   u_x += 1
   u_y += 0
  elif key == 'g':
    u_x += 1
    u_y += 1
  if key == 'b':
    u_x += 0
    u_y += 1
  if key == 'v':
    u_x -= 1
    u_y += 1
  if key == 'c':
    u_x -= 1
    u_y += 0
  if key == 'd':
    u_x -= 1
    u_y -= 1
  if key == 'e':
    u_x -= 0
    u_y -= 1
  if key == 'r':
    u_x += 1
    u_y += 1
  move_to(u_shape, (Circle((5*u_x,5*u_y),10, filled=True, color="#00FF00")))

def place_player():
 global u_shape

def pas():
  time.sleep(5)

begin_graphics()  
place_player()
move_player()
#key_text = Text("a", (320, 240), size=48)

end_graphics()