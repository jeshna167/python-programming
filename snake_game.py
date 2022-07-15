import turtle
import time
import random
delay=0.12
old_fruit=[]
score1=0
screen=turtle.Screen()
screen.title("Snake Game")
screen.setup(width=700,height=700)
screen.tracer(0)
turtle.bgcolor("purple")

snake=turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0,0)
snake.direction="stop"

food= turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(90,90)

turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("black")
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.hideturtle()
turtle.penup()

score=turtle.Turtle()
score.color("white")
score.hideturtle()
score.penup()
score.goto(0,300)
score.write(f'score : {score1}',align="center",font=("arial",25,"bold"))

def snake_go_up():
    print("pressed up")
    snake.direction="up"

def snake_go_left():
    print("pressed left")
    snake.direction="left"

def snake_go_right():
    print("pressed right")
    snake.direction="right"

def snake_go_down():
    print("pressed down")
    snake.direction="down"

def snake_move():
    if snake.direction=="up":
        y=snake.ycor()
        snake.sety(y+20)

    if snake.direction=="down":
        y=snake.ycor()
        snake.sety(y-20)

    if snake.direction=="left":
        x=snake.xcor()
        snake.setx(x-20)

    if snake.direction=="right":
        x=snake.xcor()
        snake.setx(x+20)
screen.listen()
screen.onkeypress(snake_go_up,"Up")
screen.onkeypress(snake_go_down,"Down")
screen.onkeypress(snake_go_left,"Left")
screen.onkeypress(snake_go_right,"Right")



while True:
    screen.update()
    if snake.distance(food)<20:
        x=random.randint(-270,270)
        y=random.randint(-240,240)
        food.goto(x,y)
        score.clear()
        score1=score1+1
        score.write(f'score : {score1}',align="center",font=("arial",25,"bold"))

        new_food=turtle.Turtle()
        new_food.shape("square")
        new_food.color("black")
        new_food.penup()
        old_fruit.append(new_food)
    
    for i in range(len(old_fruit)-1,0,-1):
        a=old_fruit[i-1].xcor()
        b=old_fruit[i-1].ycor()
        old_fruit[i].goto(a,b)
    
    if len(old_fruit)>0:
        a=snake.xcor()
        b=snake.ycor()
        old_fruit[0].goto(a,b)

    snake_move()
    if snake.xcor()>280 or snake.xcor()<-280 or snake.ycor()>240 or snake.ycor()<-340:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('pink')
        score.goto(0,0)
        score.write(f"GAME OVER!!! your score is {score1}",align="center",font=("arial",25,"bold"))
    time.sleep(delay)