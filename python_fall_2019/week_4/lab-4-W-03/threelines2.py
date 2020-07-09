# Angela Holden
# threelines.py

import turtle as t

def draw_line(a_turtle):
    a_turtle.down()
    a_turtle.forward(200)
    a_turtle.up()
    a_turtle.backward(200)

def draw_3_lines(larry):
    larry.left(90)
    draw_line(larry)
    larry.up()
    larry.rt(90)
    larry.fd(30)
    larry.lt(90)
    draw_line(larry)
    larry.up()
    larry.rt(90)
    larry.fd(30)
    larry.lt(90)
    draw_line(larry)
    larry.up()
    larry.lt(90)
    larry.fd(30*2)
    #larry.rt(90)

def spike_circle(a_turtle):
    
    for count in range(60):

        draw_line(a_turtle)
        a_turtle.left(6)

def main():
    
    wn = t.Screen()
    larry = t.Turtle()

    larry.speed(0)

    # for count in range(4):
    #     larry.fd(100)
    #     spike_circle(larry)
    #     larry.left(90)

    # spike_circle(larry)

    for count in range(60):
        draw_3_lines(larry)
        larry.left(6)
    
    wn.exitonclick()

main()
