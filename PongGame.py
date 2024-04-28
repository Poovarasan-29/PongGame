import turtle

#WINDOW SETUP

win = turtle.Screen()
win.setup(800,600)
win.bgcolor("blue")
win.title("Pong Game")
win.tracer(n=1, delay=0)

#WON

WON = turtle.Turtle()
WON.penup()
WON.hideturtle()
WON.color("yellow")

#SCORE

PLAYER_A = 0
PLAYER_B = 0
SCORE = turtle.Turtle()
SCORE.hideturtle()
SCORE.color("white")
SCORE.penup()
SCORE.goto(0,265)
SCORE.write("Player A: 0  Player B: 0",align="center",font=("Ariel",20,"bold"))

#LEFT SIDE

LEFT_SIDE = turtle.Turtle()
LEFT_SIDE.speed(0)
LEFT_SIDE.shape("square")
LEFT_SIDE.color("white")
LEFT_SIDE.shapesize(stretch_wid=5, stretch_len=1)
LEFT_SIDE.penup()
LEFT_SIDE.goto(-380,0)

#RIGHT SIDE

RIGHT_SIDE = turtle.Turtle()
RIGHT_SIDE.speed(0)
RIGHT_SIDE.shape("square")
RIGHT_SIDE.color("white")
RIGHT_SIDE.shapesize(stretch_wid=5, stretch_len=1)
RIGHT_SIDE.penup()
RIGHT_SIDE.goto(380,0)

#LEFT SIDE onkeypress => w->move up s->move down

def left_up():
    if LEFT_SIDE.ycor()>230:
        LEFT_SIDE.sety(230)
    LEFT_SIDE.sety(LEFT_SIDE.ycor()+20)

def left_down():
    if (LEFT_SIDE.ycor()< (-230)):
        LEFT_SIDE.sety(-230)
    LEFT_SIDE.sety(LEFT_SIDE.ycor()-20)

#RIGHT SIDE onkeypress => up ->move up , down->move down

def right_up():
    if RIGHT_SIDE.ycor()>230:
        RIGHT_SIDE.sety(230)
    RIGHT_SIDE.sety(RIGHT_SIDE.ycor()+20)

def right_down():
    if (RIGHT_SIDE.ycor()< (-230)):
        RIGHT_SIDE.sety(-230)
    RIGHT_SIDE.sety(RIGHT_SIDE.ycor()-20)

#onkeypress

win.listen()
win.onkeypress(left_up, "w")
win.onkeypress(left_down, "s")
win.onkeypress(right_up, "Up")
win.onkeypress(right_down, "Down")

#BALL

BALL = turtle.Turtle()
BALL.shape("circle")
BALL.color("white")
BALL.penup()
BALL.dy = 0.36
BALL.dx = 0.36 #0.16

while True:
    BALL.setx(BALL.xcor()+BALL.dx)
    BALL.sety(BALL.ycor()+BALL.dy)
    #TOP WALL
    if BALL.ycor() > 290:
        BALL.sety(290)
        BALL.dy *= -1

    #RIGHT WALL

    if BALL.xcor() > 390:
        BALL.setx(390)
        BALL.dx *= -1
        PLAYER_A += 1
        SCORE.clear()
        SCORE.write("Player A: {}  Player B: {}".format(PLAYER_A, PLAYER_B),align="center",font=("Ariel",20,"bold"))

    #BOTTOM WALL

    if BALL.ycor() < -290: 
        BALL.sety(-290)
        BALL.dy *= -1

    #LEFT WALL

    if BALL.xcor() < -390: 
        BALL.setx(-390)
        BALL.dx *= -1
        PLAYER_B += 1
        SCORE.clear()
        SCORE.write("Player A: {}  Player B: {}".format(PLAYER_A, PLAYER_B),align="center",font=("Ariel",20,"bold"))

    #RIGHT PADDLE TOUCH

    if BALL.xcor() > 360 and RIGHT_SIDE.ycor()+50 > BALL.ycor() and RIGHT_SIDE.ycor()-50 < BALL.ycor():
        BALL.setx(360)
        BALL.dx *= -1
        
        
    #LEFT PADDLE TOUCH

    if BALL.xcor() < -360 and LEFT_SIDE.ycor()+50 > BALL.ycor() and LEFT_SIDE.ycor()-50 < BALL.ycor():
        BALL.setx(-360)
        BALL.dx *= -1
        

    #WON THE MATCH

    if PLAYER_A == 5: 
        WON.write("Player A Won the Match",align="center",font=("Ariel",35,"bold"))

    if PLAYER_B == 5:
        WON.write("Player B Won the Match",align="center",font=("Ariel",35,"bold"))
