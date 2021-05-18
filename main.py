import random
from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

p1 = Paddle((350, 0))
p2 = Paddle((-350, 0))

ball = Ball()

score = Score()

screen.listen()
screen.onkeypress(p1.move_up, 'Up')
screen.onkeypress(p1.move_down, 'Down')
screen.onkeypress(p2.move_up, 'e')
screen.onkeypress(p2.move_down, 'd')

game_on = True
while game_on:
    ball.move(ball.move_speed)
    if ball.xcor() > 388:
        time.sleep(0.5)
        score.l_point()
        ball.move_speed = 0.3
        ball.home()
        ball.setheading(random.randint(-70, 70))
    elif ball.xcor() < -389:
        time.sleep(0.5)
        score.r_point()
        ball.move_speed = 0.3
        ball.home()
        ball.setheading(random.randint(120, 250))
    elif ball.ycor() > 289 or ball.ycor() < -288:
        head_direction = ball.heading()
        new_head_direction = head_direction * -1
        ball.setheading(new_head_direction)
        ball.move_speed += 0.01
    else:
        if ball.distance(p2) < 50 and ball.xcor() < -320:
            ball.setheading(random.randint(-70, 70))
            ball.move_speed += 0.01
        elif ball.distance(p1) < 50 and ball.xcor() > 320:
            ball.setheading(random.randint(120, 250))
            ball.move_speed += 0.01

    screen.update()

screen.exitonclick()
