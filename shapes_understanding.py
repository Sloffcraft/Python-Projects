import turtle

win = turtle.Screen()
win.title('@Sloffcraft')
win.bgcolor('white')
win.setup(width=600 , height = 500)
win.tracer()

#first object is Circle 
cr = turtle.Turtle()
cr.shape('circle')
cr.shapesize(10)
cr.color('black')
cr.penup()
cr.speed(0)
cr.goto(-250,0)

#Second object is triangle
tr = turtle.Turtle()
tr.shape('triangle')
tr.shapesize(8)
tr.color('black')
tr.speed(0)
tr.penup()
tr.goto(250 , 0)

#third object to be a square
sq = turtle.Turtle()
sq.shape("square")
sq.shapesize(stretch_wid = 5 , stretch_len = 5)
sq.color("black")
sq.penup()
sq.speed(0)
sq.goto(0 , 0)

 #loop
while True:
    win.update()