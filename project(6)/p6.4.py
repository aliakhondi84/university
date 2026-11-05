import turtle
turtle.color("red")
turtle.pensize(4)
turtle.hideturtle()
for i in range(3):
    turtle.forward(120)
    turtle.penup()
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown() 
    turtle.circle(20)
    turtle.penup()
    turtle.right(90)
    turtle.forward(-20)
    turtle.pendown()
    turtle.left(120) 
turtle.done()
    
