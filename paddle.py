from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos):
        """Initialize the Paddle class"""
        super().__init__()
        self.shape('square')
        self.x_pos = x_pos
        self.penup()
        self.goto(self.x_pos, 0)
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)


    def move_up(self):
        """Move the paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        """Move the paddle down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)