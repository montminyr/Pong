import turtle
import math

# Set up display
display = turtle.Screen()
display.title("Pong")
display.bgcolor("black")
display.setup(width=600, height=400)
display.tracer(0)

# Shape
turtle.register_shape("rectangle.gif")

# Middle dotted line
middle = turtle.Turtle()
middle.penup()
middle.color("white")
middle.pensize(3)
middle.goto(0, 300)
middle.speed(0)

middle.pensize(1)
middle.setheading(90)
for i in range(24):
    middle.fd(-26)
    middle.penup()
    middle.fd(-26)
    middle.pendown()

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(0)
ballspeed = 0.75;

# Player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("rectangle.gif")
player1.color("white")
player1.penup()
player1.goto(-260, 0)
player1.direction = "stop"

# Player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("rectangle.gif")
player2.color("white")
player2.penup()
player2.goto(260, 0)
player2.direction = "stop"

# Pen
Score1 = 0
Score2 = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 160)
pen.write("{}    {}".format(Score1, Score2), align="center", font=("Courier", 24, "normal"))


def go_up1():
    y = player1.ycor()
    if y < 200:
        player1.sety(y + 20)
        player1.direction = "stop"


def go_down1():
    y = player1.ycor()
    if y > -200:
        player1.sety(y - 20)
        player1.direction = "stop"


def go_up2():
    y = player2.ycor()
    if y < 200:
        player2.sety(y + 20)
        player2.direction = "stop"


def go_down2():
    y = player2.ycor()
    if y > -200:
        player2.sety(y - 20)
        player2.direction = "stop"

def collision(t1, t2):
    dx = t1.xcor() - t2.xcor()
    dy = t1.ycor() - t2.ycor()
    distance = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2)) #sqrt(dx^2 + dy^2)
    if distance < 50:
        t2.right(90)


display.listen()
display.onkeypress(go_up1, "w")
display.onkeypress(go_down1, "s")
display.onkeypress(go_up1, "W")
display.onkeypress(go_down1, "S")

display.onkeypress(go_up2, "Up")
display.onkeypress(go_down2, "Down")

while True:
    display.update()
    ball.fd(ballspeed)
    y = ball.ycor()
    x = ball.xcor()
    if y > 200 or y < -200:
        ball.right(45)
    if x > 260:
        Score2 = Score2 + 1
        ball.goto(0,0)
        ball.clear()

    if x < -260:
        Score1 = Score1 + 1
        ball.goto(0, 0)
        ball.clear()

    pen.clear()
    pen.write("{}    {}".format(Score1, Score2), align="center", font=("Courier", 24, "normal"))
    collision(player1, ball)
    collision(player2, ball)

display.mainloop()