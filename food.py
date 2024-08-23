import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Lift the pen to avoid drawing lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Set the size of the food
        self.color("yellow")  # Set the color of the food to yellow
        self.speed("fastest")  # Set the speed of the turtle to the fastest (to avoid drawing lines)
        self.refresh()  # Place the food in a random location when initialized

    def refresh(self):
        """Move the food to a random location on the screen."""
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate within the screen boundaries
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate within the screen boundaries
        self.goto(random_x, random_y)  # Move the food to the new random coordinates
