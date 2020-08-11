import turtle
import time
import random

ventana = turtle.Screen()
ventana.title("snook")
ventana.bgcolor("black")
ventana.setup(width=600,height=600)
ventana.cv._rootwindow.resizable(False, False)
ventana.listen()

snook = turtle.Turtle()
snook.shape("turtle")
snook.speed(10)
snook.color("white")
snook.goto(0,0)
snook.direction = "stop"
snook.penup()

num1 = random.randint(-280,280)
num2 = random.randint(-280,280)
block1 = turtle.Turtle()
block1.shape("square")
block1.color("white")
block1.penup()
block1.hideturtle()
block1.goto(num1,num2)
block1.showturtle()

block2 = turtle.Turtle()
block2.shape("square")
block2.color("white")
block2.penup()
block2.hideturtle()
block2.goto(300,300)

points = 0
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(-280,280)
text.write(f"Current score: {points}")

def snooup():
    snook.direction = "up"

def snoodown():
    snook.direction = "down"

def snooft():
    snook.direction = "left"

def snooght():
    snook.direction = "right"

ventana.onkeypress(snooup,"Up")

ventana.onkeypress(snoodown,"Down")

ventana.onkeypress(snooft,"Left")

ventana.onkeypress(snooght,"Right")

def snoovment():
    if(snook.direction == "up"):
        y = snook.ycor()
        snook.sety(y+15)
        snook.direction = "stop"
    if(snook.direction == "down"):
        y = snook.ycor()
        snook.sety(y-15)
        snook.direction = "stop"
    if(snook.direction == "left"):
        x = snook.xcor()
        snook.setx(x-15)
        snook.direction = "stop"
    if(snook.direction == "right"):
        x = snook.xcor()
        snook.setx(x+15)
        snook.direction = "stop"

while(True):
    
    if(snook.ycor()<-280):
        snook.hideturtle()
        y = snook.ycor()
        snook.sety(280)
        snook.showturtle()
    if(snook.ycor()>280):
        snook.hideturtle()
        y = snook.ycor()
        snook.sety(-280)
        snook.showturtle()
    if(snook.xcor()<-280):
        snook.hideturtle()
        x = snook.xcor()
        snook.setx(280)
        snook.showturtle()
    if(snook.xcor()>280):
        snook.hideturtle()
        x = snook.xcor()
        snook.setx(-280)
        snook.showturtle()
    if(snook.distance(block1)<15):
        num3 = random.randint(-280,280)
        num4 = random.randint(-280,280)
        block1.hideturtle()
        block1.goto(300,300)
        block2.goto(num3,num4)
        block2.showturtle()
        points + 1
        text.undo()
        text.write(f"Current score: {points}")
    if(snook.distance(block2)<15):
        num1 = random.randint(-280,280)
        num2 = random.randint(-280,280)
        block2.hideturtle()
        block2.goto(300,300)
        block1.goto(num1,num2)
        block1.showturtle()
        points + 1
        text.undo()
        text.write(f"Current score: {points}")

    snoovment()

    ventana.update()

turtle.done