import turtle
import math

bob=turtle.Turtle()
#--------------------------------------------------
def OlympicCircle():
    for i in range(circside):
        bob.fd(circ/36)
        bob.lt(360/circside)

def OlympicRings():
    bob.reset()
    bob.pensize(10)
    for i in range(3):
        bob.penup()
        bob.pencolor(topcolors[i])
        bob.goto((i*175)-175,0)
        bob.pendown()
        OlympicCircle()

    for u in range(2):
        bob.penup()
        bob.pencolor(bottomcolors[u])
        bob.goto((u*175)-90,-75)
        bob.pendown()
        OlympicCircle()
#--------------------------------------------------
def TurtleClock():
    bob.reset()
    bob.penup()
    bob.shape('turtle')
    bob.lt(90)
    for i in range(12):
        bob.penup()
        bob.goto(0,0)
        bob.rt(30)
        bob.fd(150)
        bob.pendown()
        bob.fd(20)
        bob.penup()
        bob.fd(30)
        bob.stamp()
#--------------------------------------------------
def drawshape(n):
    bob.reset()
    if(n<=2):
        print('Invalid # of Sides')
    else:
        for i in range(n):
            bob.pendown()
            bob.fd(100)
            bob.rt(angle)
            bob.penup()
#--------------------------------------------------
def drawC():
    bob.pendown()
    bob.pencolor('blue')
    for i in range(25):
        bob.bk((2*math.pi*100)/36)
        bob.lt(180/25)
    bob.penup()

def drawA():
    bob.pencolor('red')
    for i in range(2):
        bob.goto(100,50)
        bob.lt(60)
        bob.pendown()
        bob.fd(300)
        bob.penup()
    bob.reset
    bob.goto(100,50)
    for j in range(2):
        bob.pendown()
        bob.fd(150)
        bob.rt(120)
        bob.pendown()
        
def DrawInitial():
    bob.reset()
    bob.shape('arrow')
    bob.penup()
    bob.pensize(10)
    bob.goto(-100,50)
    drawC()
    drawA()
#--------------------------------------------------
def drawTriangle():
    for a in range(3):
        bob.fd(300)
        bob.lt(120)
        
def drawTriforce():
    bob.reset()
    bob.shape('arrow')
    drawTriangle()
    bob.fd(150)
    bob.lt(60)
    for i in range(3):
        bob.fd(150)
        bob.lt(120)
#--------------------------------------------------
topcolors=['blue','black','red']
bottomcolors=['yellow','green']
circ = (2*math.pi*100)
circside = 25

OlympicRings()
#------------
TurtleClock()
#------------
n=int(input('How many sides does your shape have?'))
angle=(360/n)
drawshape(n)
#------------
DrawInitial()
#------------
drawTriforce()

bob.hideturtle()

    
    
    
