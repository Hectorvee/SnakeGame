from turtle import Turtle

font = ("Courier", 15, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class

        # Read the high score from the file
        with open("score.txt") as score_file:
            content = score_file.readline()
            self.high_score = content.strip()  # Read the high score from the file and strip any extra whitespace

        self.score = 0  # Initialize the current score to 0
        self.hideturtle()  # Hide the turtle cursor
        self.pencolor("White")  # Set the pen color to white
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(0, 270)  # Position the turtle at the top center of the screen
        self.write(f"Score: {self.score} High score: {self.high_score}", False, align="center", font=font)  # Display the initial score and high score

    def update_score(self):
        """Update the displayed score on the screen."""
        self.clear()  # Clear the previous score display
        self.write(f"Score: {self.score} High score: {self.high_score}", False, align="center", font=font)  # Write the updated score and high score

    def reset(self):
        """Reset the score and update the high score if necessary."""
        # Update the high score if the current score is higher
        if self.score > int(self.high_score):
            with open("score.txt", "w") as score_file:
                score_file.write(str(self.score))  # Write the new high score to the file
                self.high_score = str(self.score)  # Update the high score attribute

        self.score = 0  # Reset the current score to 0
        self.update_score()  # Update the score display

    def increase_score(self):
        """Increase the current score by 1 and update the display."""
        self.score += 1  # Increment the score
        self.update_score()  # Update the score display
