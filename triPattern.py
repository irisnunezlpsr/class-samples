import turtle

def drawTri(mt):
	mt.forward(10)
	mt.left(120)
	mt.forward(10)
	mt.left(120)
	mt.forward(10)
	mt.left(120)

def drawLine(mt):
	c = 0
	while c < 4:
		mt.pendown()
		drawTri(mt)
		mt.penup()
		mt.forward(30)
		c = c + 1
	mt.backward(20)

def drawLL(mt):
	drawLine(mt)
	mt.backward(100)
	mt.right(180)
	drawLine(mt)
	mt.right(180)
	mt.penup()
	mt.forward(100)

def drawTriA(mt):
	c = 0
	while c < 3:
		drawLL(mt)
		mt.left(22.5)
		c = c + 1



tox = turtle.Turtle()

tox.color("red")
tox.speed(0)
drawTriA(tox)

turtle.exitonclick()
