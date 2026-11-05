import turtle as t
import random
t.bgcolor("#221F1F")
t.color('cyan')
t.speed(0)
t.penup() 
t.tracer(0)
t.hideturtle()
x=0
y=0
for i in range(1000000):
    r=random.randint(1,100)
   
    if r<=40:
        xn=(0.31*x) - (0.53*y) + (0.89)
        yn=(-0.46*x) - (0.29*y) + (1.04)
    elif r<=55:
        xn=(0.31*x) - (0.08*y) + (0.22)
        yn=(0.15*x) - (0.45*y) + (0.34)
    else:
        xn=(0.55*y) + (0.01)
        yn=(0.69*x) - (0.20*y) + (0.38)
    x=xn
    y=yn
    t.goto(x*400-250,y*400-250)
    if(i%10000==0):
        t.update()
    t.dot(2)
    
t.done()