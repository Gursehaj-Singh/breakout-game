from turtle import Screen
from paddle import Paddle
from bricks import Bricks
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

bricks = Bricks()
paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkeypress(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")
screen.onkeypress(paddle.go_left, "Left")

game_over = False
while not game_over:
    screen.update()
    ball.move()

    # Detect collision with floor (game over)
    if ball.ycor() < -280:
        game_over = True
        scoreboard.game_over()

    # Detect collision with sides
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with ceiling
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 120 and ball.ycor() < -235:
        ball.bounce_y()

    # Detect collision with brick
    for brick in bricks.all_bricks:
        if ball.distance(brick) < 70 and ball.ycor() > brick.position()[1] - 30:
            ball.bounce_y()
            bricks.remove_brick(brick)

    # Check if no bricks left (winner)
    if not bricks.all_bricks:
        game_over = True
        scoreboard.you_win()


screen.exitonclick()
