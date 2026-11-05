import turtle as t
import random
t.bgcolor("#0A0501")
t.color('green')
t.speed(0)
t.penup() 
t.hideturtle()

x=0
y=0
for i in range(10000):
    r=random.randint(1,100)
   
    if r<=2:
        xn=(0.50)
        yn=(0.27*y)
    elif r<=17:
        xn=(-0.14*x) + (0.26*y) + (0.57)
        yn=(0.25*x) + (0.22*y) - (0.04)
    elif r<=30:
        xn=(0.17*x) - (0.21*y) + (0.41)
        yn=(0.22*x) + (0.18*y) + (0.09)
    else:
        xn=(0.78*x) + (0.03*y) + (0.11)
        yn=(-0.03*x) + (0.74*y) + (0.27)
    x=xn
    y=yn
    t.goto(x*500-250,y*500-250)
    t.dot(2)
t.done()
