from turtle import Turtle
import time


class Snake:

    def __init__(self):
        self.snake_body = []
        self.snake_body_num = 3
        self.x_cor = 0
        self.y_cor = 0
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        for i in range(self.snake_body_num):
            self.add_segment()
    
    def add_segment(self):
        body = Turtle(shape="square")
        body.penup()
        body.color("white")
        body.goto(self.x_cor, self.y_cor)
        self.snake_body.append(body)
        self.x_cor -= 20

    def extend(self):
        self.add_segment()
    
    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_head.forward(10)
    
    def up(self):
        if self.snake_head.heading() == 0 or self.snake_head.heading() == 180:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() == 0 or self.snake_head.heading() == 180:
            self.snake_head.setheading(270)
    
    def left(self):
        if self.snake_head.heading() == 90 or self.snake_head.heading() == 270:
            self.snake_head.setheading(180)
    
    def right(self):
        if self.snake_head.heading() == 90 or self.snake_head.heading() == 270:
            self.snake_head.setheading(0)
    
    def pause(self):
        t = Turtle()
        t.pencolor("White")
        t.penup()
        t.hideturtle()
        t.speed("fastest")
        t.write(f"Pause", False, align="center", font=("Courier", 15, "bold"))
        time.sleep(5)
        t.undo()

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body = []
        self.snake_body_num = 3
        self.x_cor = 0
        self.y_cor = 0
        self.create_snake()
        self.snake_head = self.snake_body[0]











