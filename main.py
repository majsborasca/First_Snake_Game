from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game Deluxe")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.Up, key="Up")
screen.onkey(fun=snake.Down, key="Down")
screen.onkey(fun=snake.Left, key="Left")
screen.onkey(fun=snake.Right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reseting()
        snake.reseting()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reseting()
            snake.reseting()


screen.exitonclick()

