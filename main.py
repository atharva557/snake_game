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
food = Food()
score = ScoreCard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
a=[1,2,3,4,5,6,7,8,9,10]
game_running=True
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        snake.extend()
        food.refresh()
        score.inc_score()
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>280 or snake.head.ycor() <-280:
        score.game_over()
        game_running = False

    for seg in snake.segments:
        if seg == snake.head:
            continue
        elif snake.head.distance(seg)<10:
            score.game_over()
            game_running =False
#screen.bye()
screen.exitonclick()