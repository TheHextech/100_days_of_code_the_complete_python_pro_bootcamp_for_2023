from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT_2 = ("Courier", 30, "normal")
# This control the actual game level and the game over option. When the turtle hits the top edge of the screen
# it moves back to the original position and the player levels up. Every next level the speed increases. If the turtle
# collides a car, it's game over and everything stops.


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align="left", font=FONT)

    def increase_level(self):
        self.current_level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT_2)
