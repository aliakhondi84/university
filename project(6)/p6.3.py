import turtle as t
from random import *
t.colormode(255)
t.bgcolor('black')
for i in range(100):
    t.color(int(randint(0,255)),int(randint(0,255)),int(randint(0,255)))
    steps=int(random()*100)
    angle=int(random()*360)
    
    t.right(angle)
    t.forward(steps)
t.done()    
