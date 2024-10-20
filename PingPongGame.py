# Importing the turtle module to use for graphics
import turtle 

# Setting up the game window
wind = turtle.Screen()  # Creates a window for the game
wind.title = "Ping Pong Game"  # Sets the title of the window
wind.bgcolor("black")  # Changes the background color to black
wind.setup(width=800, height=600)  # Sets the window size to 800x600 pixels
wind.tracer(0)  # Disables automatic screen updates to manually control the refresh rate

# Paddle 1 (Red) - Creating the first paddle
madarb1 = turtle.Turtle()  # Creates a turtle object for the first paddle
madarb1.speed(0)  # Animation speed to the maximum
madarb1.shape("square")  # Sets the shape of the paddle to square
madarb1.color("red")  # Changes the paddle color to red
madarb1.shapesize(stretch_wid=5, stretch_len=1)  # Stretches the paddle to be taller
madarb1.penup()  # Lifts the pen to prevent drawing lines when moving
madarb1.goto(-350, 0)  # Places the paddle on the left side of the screen

# Paddle 2 (Blue) - Creating the second paddle
madarb2 = turtle.Turtle()  # Creates a turtle object for the second paddle
madarb2.speed(0)  # Maximum speed
madarb2.shape("square")  # Square-shaped paddle
madarb2.color("blue")  # Blue paddle
madarb2.shapesize(stretch_wid=5, stretch_len=1)  # Stretches the paddle vertically
madarb2.penup()  # Prevents drawing lines while moving
madarb2.goto(350, 0)  # Places the paddle on the right side of the screen

# Ball - Creating the ball object
ball = turtle.Turtle()  # Creates the ball as a turtle object
ball.speed(0)  # Maximum speed for smooth animation
ball.shape("circle")  # The ball is circular
ball.color("white")  # White color for the ball
ball.penup()  # Prevents drawing lines while the ball moves
ball.goto(0, 0)  # Starts the ball at the center of the screen

# Score Setup - Initializing the score and creating a scoreboard
score1 = 0  # Player 1's score
score2 = 0  # Player 2's score
score = turtle.Turtle()  # Score display object
score.speed(0)  # No animation for the score display
score.hideturtle()  # Hides the turtle shape
score.goto(0, 260)  # Positions the score display at the top of the screen
score.penup()  # Prevents drawing lines
score.color("white")  # Sets the score text color to white
score.write("Player 1 : 0   Player 2 : 0", align="center", font=("Courier", 24, "normal"))  # Initial score display

# Functions to move paddles

def madarb1_up():
    y = madarb1.ycor()  # Gets the current y-coordinate of paddle 1
    y += 20  # Moves the paddle 20 pixels up
    madarb1.sety(y)  # Updates the paddle's y-coordinate

def madarb1_down():
    y = madarb1.ycor()  # Gets the current y-coordinate of paddle 1
    y -= 20  # Moves the paddle 20 pixels down
    madarb1.sety(y)  # Updates the paddle's y-coordinate

def madarb2_up():
    y = madarb2.ycor()  # Gets the current y-coordinate of paddle 2
    y += 20  # Moves the paddle 20 pixels up
    madarb2.sety(y)  # Updates the paddle's y-coordinate

def madarb2_down():
    y = madarb2.ycor()  # Gets the current y-coordinate of paddle 2
    y -= 20  # Moves the paddle 20 pixels down
    madarb2.sety(y)  # Updates the paddle's y-coordinate

# Keyboard bindings to control the paddles
wind.listen()  # Listens for keyboard input
wind.onkeypress(madarb1_up, "w")  # Moves paddle 1 up when 'w' is pressed
wind.onkeypress(madarb1_down, "s")  # Moves paddle 1 down when 's' is pressed
wind.onkeypress(madarb2_up, "Up")  # Moves paddle 2 up when the up arrow is pressed
wind.onkeypress(madarb2_down, "Down")  # Moves paddle 2 down when the down arrow is pressed

# Ball movement - Setting the speed of the ball
ball_dx = .15  # Horizontal movement speed of the ball
ball_dy = .15  # Vertical movement speed of the ball

# Main game loop
while True:
    wind.update()  # Manually updates the game screen

    # Move the ball
    ball.setx(ball.xcor() + ball_dx)  # Moves the ball horizontally
    ball.sety(ball.ycor() + ball_dy)  # Moves the ball vertically
    
    # Ball collision with the top and bottom walls
    if ball.ycor() > 290:  # If the ball hits the top wall
        ball.sety(290)  # Prevents the ball from going out of bounds
        ball_dy *= -1  # Reverses the ball's vertical direction
    
    if ball.ycor() < -290:  # If the ball hits the bottom wall
        ball.sety(-290)  # Prevents the ball from going out of bounds
        ball_dy *= -1  # Reverses the ball's vertical direction

    # Ball goes out on the right side (Player 1 scores)
    if ball.xcor() > 390:
        ball.goto(0, 0)  # Resets the ball to the center
        ball_dx *= -1  # Reverses the ball's horizontal direction
        score1 += 1  # Increments Player 1's score
        score.clear()  # Clears the old score
        score.write(f"Player 1: {score1}  Player 2: {score2}", align="center", font=("Courier", 24, "normal"))  # Updates the score display

    # Ball goes out on the left side (Player 2 scores)
    if ball.xcor() < -390:
        ball.goto(0, 0)  # Resets the ball to the center
        ball_dx *= -1  # Reverses the ball's horizontal direction
        score2 += 1  # Increments Player 2's score
        score.clear()  # Clears the old score
        score.write(f"Player 1: {score1}  Player 2: {score2}", align="center", font=("Courier", 24, "normal"))  # Updates the score display

    # Ball and paddle collision detection (Left paddle)
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < madarb1.ycor() + 40 and ball.ycor() > madarb1.ycor() - 40:
        ball.setx(-340)  # Keeps the ball in bounds
        ball_dx *= -1  # Reverses the ball's direction when it hits the paddle
    
    # Ball and paddle collision detection (Right paddle)
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < madarb2.ycor() + 40 and ball.ycor() > madarb2.ycor() - 40:
        ball.setx(340)  # Keeps the ball in bounds
        ball_dx *= -1  # Reverses the ball's direction when it hits the paddle
