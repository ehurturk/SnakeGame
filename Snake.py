import turtle


class Snake():
    def __init__(self, shape, color):
        self.snakes = []
        self.init_snakes(3, shape, color)

    def init_snakes(self, number, shape, color):
        for i in range(0, number):
            snake = turtle.Turtle(shape)
            if i == 0:
                snake.color("orange")
            else:
                snake.color(color)
            snake.penup()
            self.snakes.append(snake)

        for j in range(1, len(self.snakes)):
            self.snakes[j].goto(self.snakes[j - 1].xcor() - 20, 0)

    def turn_left(self):
        if not self.snakes[0].heading() == 0:
            self.snakes[0].setheading(180)

    def turn_right(self):
        if not self.snakes[0].heading() == 180:
            self.snakes[0].setheading(0)

    def turn_up(self):
        if not self.snakes[0].heading() == 270:
            self.snakes[0].setheading(90)

    def turn_down(self):
        if not self.snakes[0].heading() == 90:
            self.snakes[0].setheading(270)

    def move_snakes(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            new_coord = (self.snakes[i - 1].xcor(), self.snakes[i - 1].ycor())
            self.snakes[i].goto(new_coord)

        self.snakes[0].forward(20)

    def position(self, object1, offset = (0, 0)):
        posX = round(object1.xcor() + offset[0], 2)
        posY = round(object1.ycor() + offset[1], 2)
        pos = (posX, posY)
        return pos

    def check_food_collision(self, food):
        if self.position(self.snakes[0]) == self.position(food) and self.position(self.snakes[0]) == self.position(food):
            self.add_segment()
            food.randomize_food()
            return True

    def add_segment(self):
        segment = turtle.Turtle("square")
        segment.color("white")
        segment.penup()
        self.snakes.append(segment)
        segment.goto(round(self.snakes[self.snakes.index(segment)-1].xcor(), 2) - 20, round(self.snakes[self.snakes.index(segment)-1].ycor(), 2))

    def check_wall_collusion(self, w, h):
        if self.snakes[0].xcor() >= 290 or self.snakes[0].xcor() <= -290 or self.snakes[0].ycor() >= 290 or self.snakes[0].ycor() <= -290:
            return True
        else:
            return False

    def check_tail_collusion(self):
        possible_offsets = [(0, 20), (0, -20), (20, 0), (-20, 0)]
        for snake in range(1, len(self.snakes)):
            for offset in possible_offsets:
                if self.position(self.snakes[0], offset) == self.position(self.snakes[snake], offset):
                    return True

