import turtle
import random
import time

ventana = turtle.Screen()
ventana.title("Snook 2 Electric Boogaloo")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)
ventana.cv._rootwindow.resizable(False, False)
ventana.register_shape(r"C:\Users\marti\Documents\Python projects\Game Finale\up.gif")
ventana.register_shape(r"C:\Users\marti\Documents\Python projects\Game Finale\down.gif")
ventana.register_shape(r"C:\Users\marti\Documents\Python projects\Game Finale\left.gif")
ventana.register_shape(r"C:\Users\marti\Documents\Python projects\Game Finale\right.gif")
ventana.register_shape(r"C:\Users\marti\Documents\Python projects\Game Finale\apple.gif")
ventana.register_shape(r"C:\Users\marti\Documents\Python projects\Game Finale\bad.gif")

random1 = random.randint(-280,280)
random2 = random.randint(-280,280)
random3 = random.randint(-280,280)
random4 = random.randint(-280,280)

sniik = turtle.Turtle()
sniik.shape(r"C:\Users\marti\Documents\Python projects\Game Finale\up.gif")
sniik.speed(10)
sniik.color("white")
sniik.goto(0,0)
sniik.direction = "stop"
sniik.penup()

points = 0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(-280,280)
score.write(f"Score: {points}")

ap1 = turtle.Turtle()
ap1.shape(r"C:\Users\marti\Documents\Python projects\Game Finale\apple.gif")
ap1.speed("fastest")
ap1.penup()
ap1.hideturtle()
ap1.goto(random1,random2)
ap1.showturtle()

ap2 = turtle.Turtle()
ap2.shape(r"C:\Users\marti\Documents\Python projects\Game Finale\apple.gif")
ap2.speed("fastest")
ap2.penup()
ap2.hideturtle()
ap2.goto(300,300)

spiky = turtle.Turtle()
spiky.shape(r"C:\Users\marti\Documents\Python projects\Game Finale\bad.gif")
spiky.speed("fastest")
spiky.penup()
spiky.hideturtle()
spiky.goto(random3,random4)
spiky.showturtle()

def sup():
    sniik.direction = "up"
    sniik.shape(r"C:\Users\marti\Documents\Python projects\Game Finale\up.gif")

def sdown():
    sniik.direction = "down"
    sniik.shape(r"C:\Users\marti\Documents\Python projects\Game Finale\down.gif")

def sleft():
    sniik.direction = "left"
    sniik.shape(r"C:\Users\marti\Documents\Python projects\Game Finale\left.gif")

def sright():
    sniik.direction = "right"
    sniik.shape(r"C:\Users\marti\Documents\Python projects\Game Finale\right.gif")

ventana.onkeypress(sup,"Up")
ventana.onkeypress(sdown,"Down")
ventana.onkeypress(sleft,"Left")
ventana.onkeypress(sright,"Right")

def svent():
    if(sniik.direction == "up"):
        y = sniik.ycor()
        sniik.sety(y+10)
        sniik.direction = "stop"
    if(sniik.direction == "down"):
        y = sniik.ycor()
        sniik.sety(y-10)
        sniik.direction = "stop"
    if(sniik.direction == "left"):
        x = sniik.xcor()
        sniik.setx(x-10)
        sniik.direction = "stop"
    if(sniik.direction == "right"):
        x = sniik.xcor()
        sniik.setx(x+10)
        sniik.direction = "stop"

while True:

    if(sniik.ycor()<-280):
        sniik.hideturtle
        ap1.hideturtle()
        ap2.hideturtle()
        spiky.hideturtle()
        ventana.bgcolor("white")
        gg1 = turtle.Turtle()
        gg1.speed(0)
        gg1.color("black")
        gg1.penup()
        gg1.hideturtle()
        gg1.goto(0,0)
        gg1.write(f"Game Over", align="center",font=("Courier",24,"normal"))
        time.sleep(5)
        ventana.bye()
    if(sniik.ycor()>280):
        sniik.hideturtle
        ap1.hideturtle()
        ap2.hideturtle()
        spiky.hideturtle()
        ventana.bgcolor("white")
        gg1 = turtle.Turtle()
        gg1.speed(0)
        gg1.color("black")
        gg1.penup()
        gg1.hideturtle()
        gg1.goto(0,0)
        gg1.write(f"Game Over", align="center",font=("Courier",24,"normal"))
        time.sleep(5)
        ventana.bye()
    if(sniik.xcor()<-280):
        sniik.hideturtle
        ap1.hideturtle()
        ap2.hideturtle()
        spiky.hideturtle()
        ventana.bgcolor("white")
        gg1 = turtle.Turtle()
        gg1.speed(0)
        gg1.color("black")
        gg1.penup()
        gg1.hideturtle()
        gg1.goto(0,0)
        gg1.write(f"Game Over", align="center",font=("Courier",24,"normal"))
        time.sleep(5)
        ventana.bye()
    if(sniik.xcor()>280):
        sniik.hideturtle()
        ap1.hideturtle()
        ap2.hideturtle()
        spiky.hideturtle()
        ventana.bgcolor("white")
        gg1 = turtle.Turtle()
        gg1.speed(0)
        gg1.color("black")
        gg1.penup()
        gg1.hideturtle()
        gg1.goto(0,0)
        gg1.write(f"Game Over", align="center",font=("Courier",24,"normal"))
        time.sleep(5)
        ventana.bye()
    if(sniik.distance(ap1)<10):
        random3 = random.randint(-280,280)
        random4 = random.randint(-280,280)
        random5 = random.randint(-280,280)
        random6 = random.randint(-280,280)
        ap1.hideturtle()
        ap1.goto(300,300)
        spiky.hideturtle()
        spiky.goto(random3,random4)
        spiky.showturtle()
        ap2.goto(random5,random6)
        ap2.showturtle()
        points += 1
        score.undo()
        score.write(f"Score: {points}")
    if(sniik.distance(ap2)<10):
        random1 = random.randint(-280,280)
        random2 = random.randint(-280,280)
        random3 = random.randint(-280,280)
        random4 = random.randint(-280,280)
        ap2.hideturtle()
        ap2.goto(300,300)
        spiky.hideturtle()
        spiky.goto(random3,random4)
        spiky.showturtle()
        ap1.goto(random1,random2)
        ap1.showturtle()
        points += 1
        score.undo()
        score.write(f"Score: {points}")
    if(sniik.distance(spiky)<10):
        sniik.hideturtle()
        ap1.hideturtle()
        ap2.hideturtle()
        spiky.hideturtle()
        ventana.bgcolor("white")
        gg1 = turtle.Turtle()
        gg1.speed(0)
        gg1.color("black")
        gg1.penup()
        gg1.hideturtle()
        gg1.goto(0,0)
        gg1.write(f"Game Over", align="center",font=("Courier",24,"normal"))
        time.sleep(5)
        ventana.bye()
    if(points>=25):
        sniik.hideturtle()
        ap1.hideturtle()
        ap2.hideturtle()
        spiky.hideturtle()
        ventana.bgcolor("white")
        gg2 = turtle.Turtle()
        gg2.speed(0)
        gg2.color("black")
        gg2.penup()
        gg2.hideturtle()
        gg2.goto(0,0)
        gg2.write(f"Why are you still playing this? Get the hell outta here", align="center",font=("Courier",24,"normal"))
        time.sleep(5)
        ventana.bye()

    ventana.update

    svent()

turtle.done
