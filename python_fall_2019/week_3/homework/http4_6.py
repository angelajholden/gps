# Angela Holden
# http4_6.py

# Write a program that asks the user for the number of sides, the length of the side, the color,
# and the fill color of a regular polygon. The program should draw the polygon and then fill it in.

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

num_sides = int(input('Enter the number if sides: '))
length_sides = int(input('Enter the length of sides: '))
color_sides = input('Enter the line color: ')
fill_color = input('Enter the fill color: ')

def draw(alex):
    alex.forward(length_sides)
    alex.left(360/num_sides)

def make_shape():
    alex.pensize(2)
    alex.color(color_sides)
    alex.fillcolor(fill_color)
    alex.begin_fill()
    for count in range(num_sides):
        draw(alex)
    alex.end_fill()

make_shape()

wn.exitonclick()

