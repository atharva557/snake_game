from turtle import Screen
from snake import Snake
import time
from food import Food
from score import ScoreCard
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake")
screen.tracer(0)
snake = Snake()
snake.boundery()
food = Food()
score = ScoreCard()
screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")
game_running=True
def exit():
    global game_running
    game_running=False
screen.onkeypress(exit,"e")
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        snake.extend()
        food.refresh()
        score.inc_score()
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor() <-290:
        score.reset()
        snake.reset()
        #game_running = False

    for seg in snake.segments:
        if seg == snake.head:
            continue
        elif snake.head.distance(seg)<10:
            score.reset()
            snake.reset()
            #game_running =False
#screen.bye()
screen.exitonclick()