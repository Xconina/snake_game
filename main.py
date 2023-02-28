from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# screen setup
screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()


#call snake and food

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True
## restart game function
def restart():
    game_is_on = True
    scoreboard.restart()
    snake.restart()
#listen for keys
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
# screen.onkey(restart, "space")

#movement

while game_is_on:
    #move each segment together
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food)  < 15:
        food.refresh()
        scoreboard.add_point()
        snake.extend()
    # detect collision with wall
    if snake.head.xcor() >290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on= False
        # scoreboard.start_again()
        



    #detect collision with self
    # for part in snake.segments:

    #     if snake.head.xcor()  == snake.part.xcor()  or  snake.head.ycor() == snake.part.ycor():
    #         scoreboard.game_over()
    #         game_is_on = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 7:
            game_is_on= False
            scoreboard.game_over()









screen.exitonclick()