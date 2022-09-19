from turtle import Turtle

font = ("Courier", 15, "bold")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        with open("score.txt") as score_file:
            content = score_file.readline()
            self.high_score = content[0]

        self.score = 0
        self.hideturtle()
        self.pencolor("White")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High score: {self.high_score}", False, align="center", font=font)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", False, align="center", font=font)
    
    def reset(self):
        if self.score > int(self.high_score):
            with open("score.txt", "w") as score_file:
                score_file.write(str(self.score))
                self.high_score = self.score

        self.score = 0
        self.update_score()
    
    def increase_score(self):
        self.score += 1
        self.update_score()


































