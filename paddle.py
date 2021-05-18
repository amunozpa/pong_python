from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)
        self.shape("square")
        # self.move_up()
        # self.move_down()

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
