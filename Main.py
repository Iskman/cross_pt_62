#!/usr/bin/env python3
# coding=utf-8

import turtle

hand = turtle.Turtle()


def draw_hand(left_or_right, angle, length):
    if left_or_right == "right":
        hand.right(angle)
    else:
        hand.left(angle)
    hand.forward(length)


def draw_turtle(left_or_right, angle, length):
    if left_or_right == "right":
        turtle.right(angle)
    else:
        turtle.left(angle)

    turtle.forward(length)

def finger(posx, posy, angle, thin):
    hand.penup()
    hand.goto(posx, posy) # перемещение без рисования
    hand.pendown()
    hand.begin_fill()
    hand.setheading(angle) # обнуление угла
    hand.heading()
    draw_hand("left", 90, 100)
    draw_hand("left", 25 + thin, 10)
    draw_hand("left", 25 + thin, 10)
    draw_hand("left", 25 + thin, 10)
    if thin == 0:
        draw_hand("left", 25 + thin, 10)
        draw_hand("left", 25 + thin, 10)
    draw_hand("left", 25 + thin, 10)
    draw_hand("left", 30 + thin, 10)
    draw_hand("left", 0, 90)
    hand.fillcolor("#FFF8EF")
    hand.end_fill()

hand.speed(0)
finger(0, 0, 0, 0)
finger(47, 15, 0, 0)
finger(80, 5, 0, 10)
finger(-30, -25, 20, 10)

# рисую ладонь
hand.penup()
hand.goto(-68, 5)  # перемещение без рисования
hand.pendown()
hand.setheading(0)  # обнуление угла
hand.heading()

hand.begin_fill()
draw_hand("left", -90, 100)
draw_hand("left", 45, 20)
draw_hand("left", 45, 120)
draw_hand("left", 45, 20)
draw_hand("left", 45, 130)
hand.fillcolor("#FFF8EF")
hand.end_fill()

# рисую ладонь
hand.penup()
hand.goto(10, -20)  # перемещение без рисования
hand.pendown()
hand.setheading(0)  # обнуление угла
hand.heading()

hand.begin_fill()
draw_hand("left", -45, 10)
draw_hand("left", -45, 10)
draw_hand("left", -45, 10)
draw_hand("left", -45, 10)
draw_hand("left", -45, 10)
draw_hand("left", -45, 10)
draw_hand("left", -45, 10)
draw_hand("left", -45, 10)
hand.fillcolor("#FF0000")
hand.end_fill()

hand.penup()
hand.goto(80, -100)  # перемещение без рисования
hand.pendown()
hand.setheading(0)  # обнуление угла
hand.heading()

hand.begin_fill()
draw_hand("left", -45, 10)
draw_hand("left", -45, 10)
draw_hand("left", -45, 10)
draw_hand("left", -45, 150)
draw_hand("left", -45, 10)
draw_hand("left", -45, 10)
draw_hand("left", -45, 10)
draw_hand("left", -45, 150)
hand.fillcolor("#FF0000")
hand.end_fill()

hand.penup()
hand.goto(-10, -80)  # перемещение без рисования
hand.pendown()
hand.setheading(0)  # обнуление угла
hand.heading()
draw_hand("left", -45, 10)
draw_hand("left", 45, 20)
draw_hand("left", 45, 10)


hand.penup()
hand.goto(-40, -10)  # перемещение без рисования
hand.pendown()
hand.setheading(0)  # обнуление угла
hand.heading()
draw_hand("left", 45, 10)
draw_hand("left", -45, 20)
draw_hand("left", -45, 10)

hand.penup()
hand.goto(20, -10)  # перемещение без рисования
hand.pendown()
hand.setheading(0)  # обнуление угла
hand.heading()
draw_hand("left", 45, 10)
draw_hand("left", -45, 20)
draw_hand("left", -45, 10)

turtle.done()
