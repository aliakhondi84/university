import turtle
import random
import math
turtle.bgcolor("white")
turtle.penup()
turtle.speed(0)
colores=["red","blue","green"]
turtle.tracer(0)
turtle.hideturtle()
turtle.goto(-100,0)
a=[(-200,0),(200,0),(0,(200*math.sqrt(3)))]

for j in range(10000):
    i=random.randrange(len(a))
    if a[i] == a[0]:
        turtle.pencolor("red")
    elif a[i] == a[1]:
        turtle.pencolor("blue")
    elif a[i] == a[2]:
        turtle.pencolor("green")
    turtle.setheading(turtle.towards(a[i]))
    turtle.forward(turtle.distance(a[i])/2)
    if(j%10000==0):
        turtle.update()
    turtle.dot(3)
turtle.done()