from turtle import Screen
from turtle import Turtle
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

food = Food()
snake = Snake()
score = Scoreboard()

screen.onkey(snake.up, key='Up')
screen.onkey(snake.down, key='Down')
screen.onkey(snake.left, key='Left')
screen.onkey(snake.right, key='Right')
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
       if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
    # Detect collision with tail
    # if head collides with any segment in the tail:
        #trigger game_over




screen.exitonclick()
