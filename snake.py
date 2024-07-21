import turtle as t

import time
import random

def create_snake(pos):
    snake_body = t.Turtle()
    snake_body.shape("square")
    snake_body.color("gold")
    snake_body.penup()
    snake_body.goto(pos)
    snakes.append(snake_body)


def up():
    snakes[0].setheading(90)

def down():
    if snakes[0].heading() != 90:
        snakes[0].setheading(270)

def right():
    if snakes[0].heading() != 180:
        snakes[0].setheading(0)

def left():
    snakes[0].setheading(180)

def rand_pos():
    rand_x = random.randint(-250,250)
    rand_y = random.randint(-250,250)
    return rand_x,rand_y

#먹이
food = t.Turtle()
food.shape("circle")
food.color("snow")
food.penup()
food.speed(0)
food.goto(rand_pos())


def score_update():
    global score
    score = score + 1
    score_pen.clear()
    score_pen.write(f"점수 : {score}", font=("", 15, "bold"))


t.setup(600,600)
t.bgcolor("skyblue")
t.title("snake game")
t.tracer(0)

#초기점수는 0
score = 0

#처음 snake 위치
start_pos=[(0,0),(-20,0),(-40,0)]

#snake 만들기
snakes = []
for pos in start_pos:
    create_snake(pos)

#점수 표시
score_pen = t.Turtle()
score_pen.ht()
score_pen.up()
score_pen.goto(-270,250)
score_pen.write(f"점수 : {score}", font = ("",15,"bold"))

t.listen()
t.onkeypress(up,"Up")
t.onkeypress(down,"Down")
t.onkeypress(right,"Right")
t.onkeypress(left,"Left")


game_on = True
while game_on:
    t.update()
    time.sleep(0.1)
    for i in range(len(snakes)-1, 0, -1):
        snakes[i].goto(snakes[i-1].pos())
    snakes[0].forward(10)

    if snakes[0].distance(food) < 15:
        score_update()
        food.goto(rand_pos())
        ## snakes의 마지막 위치 -1
        create_snake(snakes[-1].pos())
        score_update()


    if snakes[0].xcor() > 280 or snakes[0].xcor() < -280 or snakes[0].ycor() > 280 or snakes[0].ycor() < -280:
        game_on = False
        score_pen.goto(0,0)
        score_pen.write("Game Over", False, "center",("",30,"bold"))


t.mainloop()

