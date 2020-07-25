import turtle

# Initialize Animation Screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Dot Simulation')

# Initialize Ball
ball = turtle.Turtle()
ball.shape('classic')
ball.shapesize(0.5)
ball.color('green')
ball.penup()
ball.speed(0)
ball.goto(0, 200)

# Move ball
ball.dy = 0
gravity = 0.1
bounces = 0
while bounces < 5:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)
    # Bounce
    if ball.ycor() < -300:
        ball.dy *= -1
        bounces += 1

wn.mainloop()
