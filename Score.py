import turtle

class Score (turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()
        self.high_score = 0

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        highsocre = self.get_high_score()
        self.write(f"Score: {self.score}  High Score: {highsocre}", align="center", font=("Arial", 24, "normal"))

    def update_high_score(self, s):
        with open("highscores.txt", "w") as h_text:
            h_text.write(str(s))

    def get_high_score(self):
        with open("highscores.txt") as h_text:
            hs = h_text.read()

        return hs