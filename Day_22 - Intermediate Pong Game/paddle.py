from turtle import Turtle

MAX_UP = 260
MAX_DOWN = -240


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        if self.ycor() < MAX_UP:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > MAX_DOWN:
            new_y = self.ycor() + -20
            self.goto(self.xcor(), new_y)
