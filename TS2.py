from gasp import *
begin_graphics()
x=1
y=1
#such a square
Line((x+300,y+50),(x+25,y-50))
Line((x+300,y-188),(x+25,y+188))
Line((x+25,y+50),(x+25,y+188))
Line((x+300,y-50),(x+300,y+188))

#hats off
Arc((x+290,y+170),45, 155, -75)
Arc((x+290,y+170), 30, 145, -65)
Line((x+280,y+215),(x+315,y+280))
Line((x+330,y+190),(x+370,y+260))
Line((x+315,y+280),(x+370,y+260))

#symbolism
Line((x+40,y+118),(x+165,y+60))
Line((x+40,y+118),(x+165,y+178))
Line((x+285,y+118),(x+165,y+60))
Line((x+285,y+118),(x+165,y+178))
Circle((x+165,y+118), 30)
Line((x+130,y+130),(x+195,y+110))

update_when('key_pressed')
end_graphics
