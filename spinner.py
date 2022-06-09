from turtle import *
sc=Screen()
sc.title('Spinner')
turn=0
def spinner():
    clear()
    angle=turn/10
    right(angle)
    forward(100)
    dot(120,"purple")
    back(100)
    right(120)
    forward(100)
    dot(120,"pink")
    back(100)
    right(120)
    forward(100)
    dot(120,"blue")
    back(100)
    right(120)
    update()
def animate():
    spinner()
    ontimer(animate,20)
def flick():
    global turn
    print("flick")
    turn=turn+100
width(15)
tracer(False)
onkey(flick,"a")
listen()
animate()
done()