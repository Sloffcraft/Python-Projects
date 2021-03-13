import turtle 

wn = turtle.Screen()
wn.title("Pingpong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer()

#paddle1
pa1 = turtle.Turtle()
pa1.shape("square")
pa1.shapesize(stretch_wid = 5 , stretch_len = 1)
pa1.color("white")
pa1.speed(0)
pa1.penup()
pa1.goto(-350,0)

#paddle2
pa2 = turtle.Turtle()
pa2.shape("square")
pa2.shapesize(stretch_wid = 5 , stretch_len = 1)
pa2.color("white")
pa2.speed(0)
pa2.penup()
pa2.goto(350,0)

#ball 
ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(1)
ball.color("white")
ball.penup()
ball.speed(0)
ball.goto(0,0)
ball.dx = 3
ball.dy = 3

#functions
#paddal1
def pa1_up():
    y = pa1.ycor()
    y += 20
    pa1.sety(y)

def pa1_down():
    y = pa1.ycor()
    y -= 20
    pa1.sety(y)
    
    #second paddle
    
def pa2_up():
    y = pa2.ycor()
    y += 20
    pa2.sety(y)

def pa2_down():
    y = pa2.ycor()
    y -= 20
    pa2.sety(y)


#keyboard binding 
wn.listen()
wn.onkeypress(pa1_up , "w")
wn.onkeypress(pa1_down, "s")
wn.onkeypress(pa2_up , "Up")
wn.onkeypress(pa2_down , "Down")

#main game loop
while True:
    wn.update()
    
    #move of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
    	ball.sety(-290)
    	ball.dy *= -1
    	
    if ball.xcor() > 390:
    	ball.goto(0,0)
    	ball.dx *= -1
    	
    if ball.xcor() < -390:
    	ball.goto(0,0)
    	ball.dx*= -1
    	