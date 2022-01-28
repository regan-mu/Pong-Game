from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        """Initialize the ScoreBoard Class."""
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        """Update the score board each time a player misses."""
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align='center', font=('Courier', 20, 'normal'))
        self.goto(100, 250)
        self.write(self.r_score, align='center', font=('Courier', 20, 'normal'))

    def l_point(self):
        """Left player points aggregation"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Right player points aggregation"""
        self.r_score += 1
        self.update_scoreboard()
