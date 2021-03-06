import time
import turtle
import keyboard
# import os

# initial screen
screen1 = turtle.Screen()
screen1.title("My Pong")
screen1.bgcolor("black")
screen1.setup(width=800, height=600)
screen1.tracer(0)


# initial hub
hud_start = turtle.Turtle()
hud_start.speed(0)
hud_start.shape("square")
hud_start.color("white")
hud_start.penup()
hud_start.hideturtle()
hud_start.goto(0, 0)
hud_start.write("PRESS ENTER TO START", align="center", font=("Small Fonts", 24, "normal"))

# exit message
exit_message = turtle.Turtle()
exit_message.speed(0)
exit_message.shape("square")
exit_message.color("white")
exit_message.penup()
exit_message.hideturtle()
exit_message.goto(0, -280)
exit_message.write("PRESS ESC TO EXIT", align="center", font=("Small Fonts", 12, "normal"))

while True:
    if keyboard.read_key() == "esc":
        break

    if keyboard.read_key() == "enter":
        hud_start.clear()

        # draw screen
        screen = turtle.Screen()
        screen.title("My Pong")
        screen.bgcolor("black")
        screen.setup(width=800, height=600)
        screen.tracer(0)

        # draw paddle 1
        paddle_1 = turtle.Turtle()
        paddle_1.speed(0)
        paddle_1.shape("square")
        paddle_1.color("white")
        paddle_1.shapesize(stretch_wid=5, stretch_len=1)
        paddle_1.penup()
        paddle_1.goto(-350, 0)

        # draw paddle 2
        paddle_2 = turtle.Turtle()
        paddle_2.speed(0)
        paddle_2.shape("square")
        paddle_2.color("white")
        paddle_2.shapesize(stretch_wid=5, stretch_len=1)
        paddle_2.penup()
        paddle_2.goto(350, 0)

        # draw ball
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("square")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 1
        ball.dy = 1

        # score
        score_1 = 0
        score_2 = 0

        # head-up display
        hud = turtle.Turtle()
        hud.speed(0)
        hud.shape("square")
        hud.color("white")
        hud.penup()
        hud.hideturtle()
        hud.goto(0, 260)
        hud.write("0 : 0", align="center", font=("Small Fonts", 24, "normal"))

        def paddle_1_up():
            y = paddle_1.ycor()
            if y < 250:
                y += 30
            else:
                y = 250
            paddle_1.sety(y)


        def paddle_1_down():
            y = paddle_1.ycor()
            if y > -250:
                y += -30
            else:
                y = -250
            paddle_1.sety(y)


        def paddle_2_up():
            y = paddle_2.ycor()
            if y < 250:
                y += 30
            else:
                y = 250
            paddle_2.sety(y)


        def paddle_2_down():
            y = paddle_2.ycor()
            if y > -250:
                y += -30
            else:
                y = -250
            paddle_2.sety(y)


        # keyboard
        screen.listen()
        screen.onkeypress(paddle_1_up, "w")
        screen.onkeypress(paddle_1_down, "s")
        screen.onkeypress(paddle_2_up, "Up")
        screen.onkeypress(paddle_2_down, "Down")

        while True:
            screen.update()

            if keyboard.is_pressed("esc"):
                break

            # ball movement
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # collision with the upper wall
            if ball.ycor() > 290:
                # os.system("afplay bounce.wav&")
                ball.sety(290)
                ball.dy *= -1

            # collision with lower wall
            if ball.ycor() < -290:
                # os.system("afplay bounce.wav&")
                ball.sety(-290)
                ball.dy *= -1

            # collision with left wall
            if ball.xcor() < -390:
                score_2 += 1
                hud.clear()
                hud.write("{} : {}".format(score_1, score_2), align="center", font=("Small Fonts", 24, "normal"))
                # os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
                ball.goto(0, 0)
                ball.dx *= -1

            # collision with right wall
            if ball.xcor() > 390:
                score_1 += 1
                hud.clear()
                hud.write("{} : {}".format(score_1, score_2), align="center", font=("Small Fonts", 24, "normal"))
                # os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
                ball.goto(0, 0)
                ball.dx *= -1

            # collision with the paddle 1
            if ball.xcor() < -330 and ball.xcor() >= -350 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
                ball.dx *= -1
                # os.system("afplay bounce.wav&")
            # collision with the paddle 2
            if ball.xcor() > 330 and ball.xcor() <= 350 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
                ball.dx *= -1
                # os.system("afplay bounce.wav&")
