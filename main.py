from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create a snake body
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.pause, "p")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    if snake.snake_head.distance(food) < 15:
        snake.add_segment()
        score.increase_score()
        food.refresh()

    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280) or\
        (snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280):
        score.reset()
        snake.reset()
        continue

    for seg in snake.snake_body[1:]:
        if snake.snake_head.distance(seg) < 9:
            score.reset()
            snake.reset()
            continue

    snake.move()

screen.exitonclick()
