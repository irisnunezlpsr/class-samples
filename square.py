# square.py
import turtle

# make turtle
buzz = turtle.Turtle()
buzz.shape("turtle")
buzz.color("red")

# make a square
l = 0
while l < 4:
	buzz.forward(150)
	buzz.left(90)
	l = l + 1

# click to exit
turtle.exitonclick()
