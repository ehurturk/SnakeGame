import turtle


class GameOver(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 170)

    def display(self, text):
        self.write(text, align="center", font = ("Arial", 21, "normal"))
