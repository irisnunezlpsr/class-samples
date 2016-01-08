import turtle


def drawSq(mt):
	mt.forward(20)
	mt.right(90)
	mt.forward(20)
	mt.right(90)
	mt.forward(20)
	mt.right(90)
	mt.forward(20)
	mt.right(90)
	mt.forward(20)


def drawCS(mt):
	mt.color('red')
	drawSq(mt)
	mt.color('blue')
	drawSq(mt)
	mt.right(90)
	mt.forward(20)
        mt.color('green')
        drawSq(mt)
	mt.right(90)
	mt.forward(20)
        mt.color('yellow')
        drawSq(mt)


def drawClm(mt):
	c = 0
	while c < 4:
		drawCS(mt)
		mt.right(90)
		mt.penup()
		mt.forward(4)
		mt.right(90)
		mt.forward(20)
		mt.pendown()
		c = c + 1


tox = turtle.Turtle()

tox.speed(0)

drawClm(tox)


turtle.exitonclick()
