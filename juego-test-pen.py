import turtle
import time
import random

#ventana
ventana = turtle.Screen()
ventana.title("Hamilton: The Broadway Musical: The game")
ventana.bgcolor("white")
ventana.setup(width=600,height=600)
ventana.cv._rootwindow.resizable(True, True)
ventana.listen()

#definicion de personaje
alexander = turtle.Turtle()
alexander.shape("turtle")
alexander.speed(10)
alexander.color("green")
alexander.goto(0,0)
alexander.direction = "stop"

#Movimiento
def arriba():
    alexander.direction = "up"

def abajo():
    alexander.direction = "down"

def izquierda():
    alexander.direction = "left"

def derecha():
    alexander.direction = "right"
    
ventana.onkeypress(derecha,"Right")
    
ventana.onkeypress(izquierda,"Left")
    
ventana.onkeypress(abajo,"Down")
    
ventana.onkeypress(arriba,"Up")

def movimiento():
    if(alexander.direction == "up"):
        y = alexander.ycor()
        alexander.sety(y+20)
        alexander.direction = "stop"
    if(alexander.direction == "down"):
        y = alexander.ycor()
        alexander.sety(y-20)
        alexander.direction = "stop"
    if(alexander.direction == "left"):
        x = alexander.xcor()
        alexander.setx(x-20)
        alexander.direction = "stop"
    if(alexander.direction == "right"):
        x = alexander.xcor()
        alexander.setx(x+20)
        alexander.direction = "stop"

while True:

    if(alexander.ycor()<-280):
        alexander.direction = "stop"
        y = alexander.ycor()
        alexander.sety(y+10)
    if(alexander.ycor()>280):
        alexander.direction = "stop"
        y = alexander.ycor()
        alexander.sety(y-10)
    if(alexander.xcor()<-280):
        alexander.direction = "stop"
        x = alexander.xcor()
        alexander.setx(x+10)
    if(alexander.xcor()>280):
        alexander.direction = "stop"
        x = alexander.xcor()
        alexander.setx(x-10)
    
    movimiento()

    ventana.update()


turtle.done
