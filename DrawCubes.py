import turtle

# draw one rhombus as base
def drawPara(mt):
	mt.begin_fill()
	mt.speed(0)
 	mt.right(30)
	mt.forward(25)
	mt.right(120)
	mt.forward(25)
	mt.right(60)
	mt.forward(25)
	mt.right(120)
	mt.forward(25)
	mt.right(20)
	mt.end_fill()
# will start at one side of rhombus
	mt.penup()
	mt.right(40)
	mt.forward(25)
	mt.right(120)
	mt.forward(25)
	mt.right(60)
 	mt.forward(25)

# fill in main line with color --top of cube--
def colorPline(mt):
	c = 0
# will repeat top of cube 8 times
	while c < 8:
		mt.color("dark red")
		drawPara(mt)
		mt.penup()
		mt.forward(25)
		mt.right(150)
		c = c + 1

# move down to next row
def move(mt):
	mt.right(30)
	mt.penup()
        mt.forward(50)
        mt.right(30)


# Sides of the cube --rhombus at an angle
def anglePara(mt):
	colorPline(mt)
	move(mt)
	c = 0
# will repeat making both sides (cube sides) 8 times and different color
	while c < 8:
		mt.color('indian red')
		drawPara(mt)
		mt.color('red')
		mt.penup()
		mt.right(120)
		mt.forward(25)
		mt.left(90)
		drawPara(mt)
		mt.right(120)
		mt.forward(25)
		mt.right(60)
		mt.forward(25)
		mt.right(120)
		mt.left(60)
		mt.forward(25)
		mt.right(30)
		c = c + 1
# moves to next row
	mt.right(90)
	mt.forward(25)
	mt.right(210)

# repeats cube row to make 6 lines down
def repeat(mt):
	c = 0
	while c < 6:
		anglePara(mt)
		c = c + 1

# turtle named t
t = turtle.Turtle()

repeat(t)

turtle.exitonclick()
