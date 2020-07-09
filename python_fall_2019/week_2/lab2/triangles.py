# Angela Holden
# triangles.py

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
# Style
alex.pensize(2)
alex.color('blue')
# Inner
alex.up()
alex.forward(50)
alex.down()
alex.right(120)
alex.forward(100)
alex.right(120)
alex.forward(100)
alex.right(120)
alex.forward(100)
# Outer
alex.left(120)
alex.forward(100)
alex.left(120)
alex.forward(200)
alex.left(120)
alex.forward(200)
alex.left(120)
alex.forward(100)
# Position
alex.up()
alex.left(120)
alex.forward(100)
alex.left(60)
# Exit
wn.exitonclick()
