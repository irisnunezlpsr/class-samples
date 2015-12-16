import turtle

t = turtle.Turtle()
t.speed(1)

count = 0
while count < 20:
	t.forward(5)
	t.penup()
	t.forward(5)
	t.pendown()
	count = count + 1

t.penup()
t.goto(-100,-55)
t.pendown()
t.circle(150)
