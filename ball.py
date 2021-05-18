from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.move_speed = 0.3
        self.shape("circle")
        self.color("white")
        self.setheading(45)

    def move(self, move_speed):
        self.forward(move_speed)
