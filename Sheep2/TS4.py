from gasp import *
from random import randint
import time

class User():
  pass

class Rob():
  pass 

def place_user():
  global u
  u = User()
  u.x = randint(0, 63)
  u.y = randint(0, 47)

def no_danger_zone():
  global u
  place_user()
  u.shape =Circle((10*u.x+5, 10*u.y+5), 8, filled=True, color="#008000")

def place_rob():
  global robs
  robs = []

  while len(robs) > 8:
    r = Rob()
    r.x = (0,63)
    r.y = (0, 47)
    r.mothball = False
    r.shape = Box((10*r.x, 10*r.y),10, 10, filled=True, color="#FFA500")
    robs.append(r)
  
def move_player():
  global User

  key = update_when("key_pressed")

  if key == 'r':
    remove_from_screen(u.shape)
    no_danger_zone()
  elif key == 'w':
    u.x += 0
    u.y += 1
  elif key == 'd':
    u.x += 1
    u.y += 0
  elif key == 's':
    u.x += 0
    u.y -= 1
  elif key == 'a':
    u.x -= 1 
    u.y += 0
  move_to(u.shape, Circle((10*u.x+5, 10*u.y+5), 8, filled=True, thickness=8, color="#008000"))

def move_rob():
  global robs
  for r in robs:
    if not r.mothball:
      if r.x > u.x:
        r.x -= 1
      elif r.y > u.y:
        r.y -1
      
      if r.x < u.x:
        r.x += 1
      elif r.y < u.y:
        r.y += 1
    move_to(r.shape,(10*r.x, 10*r.y), 10, 10, filled=True, color="#FFA500")

def collision_detected(item1, list):
  for item2 in list:
    if item1.x == item2.x and item1.y == item2.y: 
      return True
    return False

def mothball(bot):
  for bot1 in robs:
    if bot1 == bot:
      return False
    if bot1.x == bot.x and bot1.y == bot.y:
      return bot1
    return False
  
def check_collisions():
  global finished, robs

  if collision_detected(User, Rob):
    finished = True
    Text("game over", 320, 340, size =22)
    pas()
    return
  
  survived_rob = []

  for r in robs: 
    if collision_detected(r, waste): 
      continue

  husk = mothball(r)
  if not husk:
    survived_rob.append(r)
  else:
    remove_from_screen(husk.shape)
    husk.waste(True)
    husk.shape = Box((10*r.x, 10*r.y), 10, 10, filled=True, color="#FFA500")
    waste.append(husk)

  robs = []
  for r in survived_rob:
    if not collision_detected(r, husk):
      robs.append(r)

  if not robs:
    finished = True
    Text("you win", (160, 240), size = 22)
    pas()
    return

def pas():
  time.sleep(5)

begin_graphics()  
finished = False
waste = []
place_rob()
no_danger_zone()
while not finished:
    move_player()
    move_rob()
    check_collisions()
 
end_graphics()