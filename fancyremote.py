import random
import turtle
from Tkinter import *

def regular_octagon(myTurtle):
	myTurtle.penup()
        myTurtle.goto(0,0)
        myTurtle.pendown()
        myTurtle.color(random.choice(c))
        sidecount = 0
        while sidecount < 8:
		myTurtle.forward(100)
		myTurtle.left(45)
		sidecount = sidecount + 1

# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)
# create our turtle
shawn = turtle.Turtle()
c = ['yellow','green','red','blue','cyan','purple','magenta','violetRed']
# make some simple buttons
fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))
right = Button(frame, text="right", command=lambda: shawn.right(90))
bwd = Button(frame, text="bwd", command=lambda: shawn.backward(50))
up = Button(frame, text="up", command=lambda: shawn.penup())
down = Button(frame, text="down", command=lambda: shawn.pendown())
color = Button(frame, text="color", command=lambda: shawn.color(random.choice(c)))
octagon = Button(frame, text="octagon", command=lambda: regular_octagon(shawn))

# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
bwd.pack(side=LEFT)
up.pack(side=LEFT)
down.pack(side=LEFT)
color.pack(side=LEFT)
octagon.pack(side=LEFT)
frame.pack()

turtle.exitonclick()
