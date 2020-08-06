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
# alexander.penup()

#Movimiento
def arriba():
    alexander.direction = "up"

def abajo():
    alexander.direction = "down"

def izquierda():
    alexander.direction = "left"

def derecha():
    alexander.direction = "right"

# def stoplapiz():
#     alexander.penup() = "lapizup"

# def golapiz():
#     alexander.pendown() = "lapizdown"
    
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


# Texto xd
#
# texto = turtle.Turtle()
# texto.speed(0)
# texto.color("black")
# texto.penup()
# texto.hideturtle()
# texto.goto(0,0)
# texto.write("He")

# This dont work
#
# X = input(f"Ingrese un numero: \n")
# Y = input(f"Ingrese otro numero: \n")
# alexander.goto(X,Y)

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
    
    # if(alexander.isdown()):
    #     ventana.onkeypress(stoplapiz,"M")
    # else:
    #     ventana.onkeypress(golapiz,"M")

    movimiento()

    ventana.update()


turtle.done