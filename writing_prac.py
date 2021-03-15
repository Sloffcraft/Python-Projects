import turtle

#just a window
wn = turtle.Screen()
wn.title("penup_testing")
wn.bgcolor("green")
wn.setup( width = 800 , height = 600)
wn.tracer()

#a object to write with 
pen = turtle.Turtle()
pen.color("black")
pen.penup()
pen.write("Hello There" , font = ("courier" , 14 , "bold" ))
pen.speed(0)
pen.hideturtle()

#second object
sq = turtle.Turtle()
sq.shape("square")
sq.penup()
sq.speed(0)
sq.color("black")
sq.goto(0,-280)

#functions of the player 
def sq_up():
	y = sq_up.ycor()
	y += 20
	sq_up.sety(y)
	
def sq_right():
	x = sq.xcor()
	x += 20
	sq.setx(x)
	
def sq_left():
	x = sq.xcor()
	x -= 20
	sq.setx(x)
	
#keyboard binding 
wn.listen()
wn.onkeypress(sq_up , "w")
wn.onkeypress(sq_right , "d")
wn.onkeypress(sq_left , "a")

#loop
while True :
    wn.update()