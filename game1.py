import turtle

win = turtle.Screen()	
win.bgcolor ('black')
win.setup(width = 800 , height = 600)
win.title('To show someone')
win.tracer()

#object1
ob = turtle.Turtle()
ob.shape('square')
ob.shapesize (stretch_wid = 2, stretch_len=15)
ob.speed(0)
ob.color('white')
ob.penup()
ob.goto(0 , -450)

#Ball 
ball = turtle.Turtle()
ball.color('white')
ball.shape('triangle')
ball.speed(0)
ball.penup()
ball.goto (0,0)

#funtions
def ob_right():
       r  = ob.rcor()
   	
# keyboard
win.listen()
win.onkeypress(ob_right , "R")

#man game loop
while True:
	win.update()