from gasp import *

x=0
y=0
begin_graphics()

#such a square
Line((x+300,y+50),(x+25,y+50), color='#008000')
Line((x+300,y+188),(x+25,y+188), color='#008000')
Line((x+25,y+50),(x+25,y+188), color='#008000')
Line((x+300,y+50),(x+300,y+188), color='#008000')

#hats off
Arc((x+290,y+170),45, 155, -75, thickness=3)
Arc((x+290,y+170), 30, 145, -65, thickness=3)
Line((x+280,y+215),(x+315,y+280))
Line((x+330,y+190),(x+370,y+260))
Line((x+315,y+280),(x+370,y+260))

#symbolism
Line((x+40,y+118),(x+165,y+60), color='#FFFF00')
Line((x+40,y+118),(x+165,y+178), color='#FFFF00')
Line((x+285,y+118),(x+165,y+60), color='#FFFF00')
Line((x+285,y+118),(x+165,y+178), color='#FFFF00')
Circle((x+165,y+118), 30, filled=True, color='#000080')
Line((x+130,y+130),(x+195,y+110), color='#ffffff', thickness=7)

update_when('key_pressed')
end_graphics

