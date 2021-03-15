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
pen.write("Hello There" , align = "center" , font = ("courier" , 14 , "bold" ))
pen.speed(0)
pen.hideturtle()
pen.goto(0,240)

#corse1
ob = turtle.Turtle()
ob.shape("square")
ob.shapesize(stretch_wid = 20 , stretch_len = 1)
ob.penup()
ob.speed(0)
ob.color("black")
ob.goto(30,-240)

#corse2
ob1 = turtle.Turtle()
ob1.shape("square")
ob1.shapesize(stretch_wid = 20 , stretch_len = 1)
ob1.penup()
ob1.speed(0)
ob1.color("black")
ob1.goto(-30,-270)

#corse3
ob2 = turtle.Turtle()
ob2.shape("square")
ob2.shapesize(stretch_wid = 1 , stretch_len = 10)
ob2.penup()
ob2.speed(0)
ob2.color("black")
ob2.goto(-60,-30)

#corse4
ob3 = turtle.Turtle()
ob3.shape("square")
ob3.shapesize(stretch_wid = 1 , stretch_len = 10)
ob3.penup()
ob3.speed(0)
ob3.color("black")
ob3.goto(-120,-80)

#Player 
sq = turtle.Turtle()
sq.shape("square")
sq.penup()
sq.speed(0)
sq.color("black")
sq.goto(0,-240)

#functions of the player 
def sq_up():
	y = sq.ycor()
	y += 20
	sq.sety(y)
	
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
