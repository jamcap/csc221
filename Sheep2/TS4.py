from gasp import *
from random import randint
import time


def check_collision():
  global r_x, r_y, u_x, u_y, finished, done
  if r_x == u_x and r_y == u_y: finished= True; done = Text("game over", (320, 240), size=48) 
  pas()


def place_player():
  global u_x, u_y, u_shape
  u_x = randint(0, 63)
  u_y = randint(0, 47)
  u_shape = (Circle((10*u_x+5,10*u_y+5),10, filled=True, color="#00FF00"))

def place_rob():
  global r_shape, r_y, r_x
  r_x = randint(0, 63)
  r_y = randint(0, 47)
  r_shape = (Circle((10*r_x+5,10*r_y+5),10, filled=True, color="#800080"))

def move_rob():
  global r_shape, r_x, r_y
  if u_x > r_x: 
    r_x += 1
  elif u_y > r_y:
    r_y += 1
  elif u_y < r_y: 
    r_y -= 1
  elif u_x < r_x:
    r_x -= 1
  move_to(r_shape, ((10*r_x+5,10*r_y+5)))

def move_player():
  global u_x, u_y, u_shape
 
  key = update_when('key_pressed')
  if key == 'w':
   u_x += 0
   u_y += 1
  elif key == 'a':
    u_x -=1
    u_y +=0
  elif key == 's':
    u_x += 0
    u_y -=1
  elif key == 'd':
    u_x += 1
    u_y +=0
  move_to(u_shape, ((10*u_x+5,10*u_y+5)))

def pas():
  time.sleep(5)

begin_graphics()  
finished = False
place_player()
place_rob()
while not finished:
    move_player()
    move_rob()
    check_collision()
 
end_graphics()