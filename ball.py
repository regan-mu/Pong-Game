from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        """Initializing the Ball class"""
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.width(20)
        self.penup()
        self.x_move = 20
        self.y_move = 20
        self.move_speed = 0.2

    def reset_game(self):
        "Reset the ball to the starting position and change the direction when a players missed."
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()



    def move(self):
        """Progress the ball forward in the chosen direction"""
        next_x = self.xcor() + self.x_move
        next_y = self.ycor() + self.y_move
        self.goto(next_x, next_y)

    def bounce_y(self):
        """Bounce the ball along the y-axis"""
        self.y_move *= -1

    def bounce_x(self):
        """Bounce the ball along the x-axis and increase the speed each time the ball hits the paddle"""
        self.x_move *= -1
        self.move_speed *= 0.95
