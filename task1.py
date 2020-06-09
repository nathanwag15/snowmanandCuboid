#Nathan Wagstaff Assignment #4
# A snowman with two arms and a hat.

import turtle

#settings

turtle.speed(1)
turtle.width(10)

#base
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()
turtle.circle(150)

#middle
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.circle(105)

#buttons
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.circle(1)

turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.circle(1)

turtle.penup()
turtle.goto(0,150)
turtle.pendown()
turtle.circle(1)

#head
turtle.penup()
turtle.goto(0, 210)
turtle.pendown()
turtle.circle(60)

#Hat
turtle.penup()
turtle.goto(0, 330)
turtle.pendown()
turtle.forward(70)
turtle.begin_fill()

turtle.goto(40, 330)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(40)

turtle.fillcolor("black")
turtle.end_fill()

turtle.goto(-70, 330)

#Eyes
turtle.penup()
turtle.goto(-20, 280)
turtle.pendown()

turtle.circle(2)

turtle.penup()
turtle.goto(20, 280)
turtle.pendown()

turtle.circle(2)

#mouth
turtle.penup()
turtle.goto(-20, 240)
turtle.pendown()

turtle.left(-90)
turtle.circle(20, 180)

#right arm
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()

turtle.left(200)
turtle.forward(150)
turtle.left(70)
turtle.forward(30)

turtle.left(180)
turtle.forward(30)
turtle.left(20)
turtle.forward(30)

turtle.left(180)
turtle.forward(30)
turtle.left(270)
turtle.forward(30)

#right arm
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()

turtle.left(200)
turtle.forward(150)
turtle.left(70)
turtle.forward(30)

turtle.left(180)
turtle.forward(30)
turtle.left(20)
turtle.forward(30)

turtle.left(180)
turtle.forward(30)
turtle.left(270)
turtle.forward(30)
