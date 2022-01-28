from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.title('Pong')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)


#Instantiate the turtle objects
right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
score_board = ScoreBoard()

# Listen to keystrokes on the Keyboard.
screen.listen()
screen.onkey(key='Up', fun=right_paddle.move_up)
screen.onkey(key='Down', fun=right_paddle.move_down)
screen.onkey(key='w', fun=left_paddle.move_up)
screen.onkey(key='s', fun=left_paddle.move_down)


# Flag For the While loop.
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with the wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when the ball goes out of bounds.
    if ball.xcor() > 350:
        # Right paddle Misses
        ball.reset_game()
        score_board.l_point()


    if ball.xcor() < -350:
        # left paddle misses
        ball.reset_game()
        score_board.r_point()


screen.exitonclick()