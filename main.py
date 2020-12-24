import turtle
import time
import Snake
import Food, Score, gameover


def init_screen(width, height):
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.bgcolor("black")
    screen.title("Snake Game")
    return screen


WIDTH = 600
HEIGHT = 600

turtle.tracer(0)
snake = Snake.Snake("square", "white")
screen = init_screen(WIDTH, HEIGHT)
game_over_text = gameover.GameOver()
game_over = False
food = Food.Food("square", "purple")
score = Score.Score()
while not game_over:
    screen.update()
    time.sleep(0.09)

    snake.move_snakes()
    food_collected = snake.check_food_collision(food)
    out_of_bounds = snake.check_wall_collusion(WIDTH, HEIGHT)
    tail_collusion = snake.check_tail_collusion()
    if food_collected:
        score.increase_score()
    if out_of_bounds or tail_collusion:
        game_over = True

    screen.listen()
    screen.onkey(snake.turn_left, "Left")
    screen.onkey(snake.turn_right, "Right")
    screen.onkey(snake.turn_up, "Up")
    screen.onkey(snake.turn_down, "Down")


game_over_text.display("Game Over!")
screen.exitonclick()

