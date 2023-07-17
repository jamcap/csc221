from gasp import *
from random import randint

player_x = randint(0, 63)
player_y = randint(0, 47)
player_shape = Circle((300,200), 15)

def place_player():
    Circle((10 * player_x, 10 * player_y), 5, filled=True)

def move_player():
    global player_x, player_y, player_shape

    key = update_when('key_pressed')
    print("moved")

    if key == 'k' and player_x <63:
        player_x += 1
    elif key == 'l':
        if player_x < 63:
            player_x += 1
        if player_y > 0:
            player_y -= 1 

    move_to(player_shape, (10 * player_x + 5, 10 * player_y + 5))

begin_graphics()
finished = False
c = Circle((300,200), 5)
key_text = Text("", (320,240), size =48)

place_player()
move_player()

while True:
    key = update_when('key_pressed')
    remove_from_screen(key_text)
    key_text = Text(key, (320,240), size=48)
    if key == 'q':
        break

end_graphics()
