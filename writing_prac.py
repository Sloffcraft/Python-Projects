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

#loop
while True :
    wn.update()