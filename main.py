from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

# Create a screen for the game with a specified width and height
screen = Screen()
screen.setup(width=600, height=600)  # Set the dimensions of the screen
screen.bgcolor("black")              # Set the background color of the screen
screen.title("My Snake Game")        # Set the title of the screen
screen.tracer(0)                     # Turn off screen updates for manual control

# Create instances of game objects
snake = Snake()                      # Initialize the snake
food = Food()                        # Initialize the food
score = ScoreBoard()                 # Initialize the score board

# Listen for keyboard input to control the snake
screen.listen()
screen.onkey(snake.up, "Up")         # Bind the 'Up' key to move the snake up
screen.onkey(snake.down, "Down")     # Bind the 'Down' key to move the snake down
screen.onkey(snake.left, "Left")     # Bind the 'Left' key to move the snake left
screen.onkey(snake.right, "Right")   # Bind the 'Right' key to move the snake right
screen.onkey(snake.pause, "p")       # Bind the 'p' key to pause the game

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()                 # Update the screen to reflect changes
    time.sleep(0.1)                # Pause the loop to control the game's speed

    # Check if the snake has collided with the food
    if snake.snake_head.distance(food) < 15:
        snake.add_segment()         # Add a new segment to the snake
        score.increase_score()      # Increase the score
        food.refresh()             # Move the food to a new location

    # Check if the snake has collided with the wall
    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280) or\
       (snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280):
        score.reset()               # Reset the score
        snake.reset()               # Reset the snake
        continue                    # Continue to the next iteration of the loop

    # Check if the snake has collided with itself
    for seg in snake.snake_body[1:]:  # Exclude the head of the snake
        if snake.snake_head.distance(seg) < 9:
            score.reset()           # Reset the score
            snake.reset()           # Reset the snake
            continue                # Continue to the next iteration of the loop

    # Move the snake
    snake.move()

# Exit the game when the user clicks on the screen
screen.exitonclick()
