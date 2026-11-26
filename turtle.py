import turtle

i = 10
turtle.speed(0)
turtle.color('red')
turtle.bgcolor('black')
turtle.speed(0)
for i in range(100):
    turtle.circle(50)
    turtle.left(5)
turtle.penup()
turtle.color('orange')
turtle.pendown()
for i in range(100):
    turtle.circle(100)
    turtle.left(5)
turtle.penup()
turtle.color('yellow')
turtle.pendown()
for i in range(100):
    turtle.circle(150)
    turtle.left(5)
turtle.penup()
turtle.color('green')
turtle.pendown()
for i in range(100):
    turtle.circle(200)
    turtle.left(5)
turtle.penup()
turtle.color('blue')
turtle.pendown()
for i in range(100):
    turtle.circle(250)
    turtle.left(5)
turtle.penup()
turtle.color('purple')
turtle.pendown()
for i in range(100):
    turtle.circle(300)
    turtle.left(5)
turtle.penup()
turtle.color('pink')
turtle.pensize(2)
turtle.pendown()
for i in range(100):
    for i in range(5):
        turtle.left(144)
        turtle.forward(320)
    turtle.left(5)