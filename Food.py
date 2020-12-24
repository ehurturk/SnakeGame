import turtle, random


class Food (turtle.Turtle):
    def __init__(self, shape, color):
        super().__init__(shape)
        self.color(color)
        self.penup()

    def randomize_food(self):
        xcord = random.randint(-270, 270)
        while not xcord % 20 == 0:
            xcord = random.randint(-270, 270)
        ycord = random.randint(-270, 270)
        while not ycord % 20 == 0:
            ycord = random.randint(-270, 270)
        new_cord = (xcord, ycord)
        self.goto(new_cord)




