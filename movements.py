import turtle

win = turtle.Screen()
win.title("Movements of a triangle")
win.bgcolor("white")
win.setup(width = 800 , height = 600)
win.tracer()

#main player
pl = turtle.Turtle()
pl.shape("triangle")
pl.shapesize(3)
pl.color = ("black")
pl.speed(0)
pl.penup()
pl.goto(0,0)

#functions
def pl_up():
	y = ob.ycor()
	y += 20
	pl.sety(y)
	
def pl_down():
	y = pl.ycor()
	y -= 20
	pl.sety(y)
	
	
#keyboard signals
win.listen()
win.onkeypress(pl_up , "w")


#loop
while True:
    win.update()