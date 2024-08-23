from turtle import Turtle
import time


class Snake:
    def __init__(self):
        self.snake_body = []  # List to hold the segments of the snake
        self.snake_body_num = 3  # Initial number of segments in the snake
        self.x_cor = 0  # X-coordinate for positioning snake segments
        self.y_cor = 0  # Y-coordinate for positioning snake segments
        self.create_snake()  # Create the initial snake
        self.snake_head = self.snake_body[0]  # The head of the snake is the first segment

    def create_snake(self):
        """Create the initial snake body with segments."""
        for i in range(self.snake_body_num):
            self.add_segment()  # Add a segment to the snake body

    def add_segment(self):
        """Add a new segment to the snake body."""
        body = Turtle(shape="square")  # Create a new turtle segment
        body.penup()  # Lift the pen to avoid drawing lines
        body.color("white")  # Set the color of the segment
        body.goto(self.x_cor, self.y_cor)  # Position the segment
        self.snake_body.append(body)  # Add the segment to the snake body list
        self.x_cor -= 20  # Move the X-coordinate for the next segment

    def extend(self):
        """Add a new segment to extend the snake."""
        self.add_segment()  # Use the add_segment method to extend the snake

    def move(self):
        """Move the snake forward by updating the position of each segment."""
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            # Move each segment to the position of the previous segment
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_head.forward(10)  # Move the head of the snake forward by 10 units

    def up(self):
        """Change the direction of the snake to up."""
        if self.snake_head.heading() == 0 or self.snake_head.heading() == 180:
            # Only allow changing to up if moving horizontally
            self.snake_head.setheading(90)

    def down(self):
        """Change the direction of the snake to down."""
        if self.snake_head.heading() == 0 or self.snake_head.heading() == 180:
            # Only allow changing to down if moving horizontally
            self.snake_head.setheading(270)

    def left(self):
        """Change the direction of the snake to left."""
        if self.snake_head.heading() == 90 or self.snake_head.heading() == 270:
            # Only allow changing to left if moving vertically
            self.snake_head.setheading(180)

    def right(self):
        """Change the direction of the snake to right."""
        if self.snake_head.heading() == 90 or self.snake_head.heading() == 270:
            # Only allow changing to right if moving vertically
            self.snake_head.setheading(0)

    def pause(self):
        """Display a pause message on the screen."""
        t = Turtle()
        t.pencolor("White")  # Set the text color
        t.penup()  # Lift the pen to avoid drawing lines
        t.hideturtle()  # Hide the turtle cursor
        t.speed("fastest")  # Set the speed to fastest
        t.write("Pause", False, align="center", font=("Courier", 15, "bold"))
        time.sleep(5)  # Pause the game for 5 seconds
        t.undo()  # Remove the pause message

    def reset(self):
        """Reset the snake to its initial state."""
        for seg in self.snake_body:
            seg.goto(1000, 1000)  # Move segments out of view
        self.snake_body = []  # Clear the snake body list
        self.snake_body_num = 3  # Reset the number of segments
        self.x_cor = 0  # Reset the X-coordinate
        self.y_cor = 0  # Reset the Y-coordinate
        self.create_snake()  # Create a new snake
        self.snake_head = self.snake_body[0]  # Set the new head of the snake
