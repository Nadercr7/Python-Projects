import curses  # Import the curses module for terminal manipulation
import random  # Import random module for generating random food locations

# Initialize the game screen
screen = curses.initscr()  # Initialize the screen with curses
curses.curs_set(0)  # Hide the cursor for a better visual experience
screen_height, screen_width = screen.getmaxyx()  # Get the dimensions of the screen (height, width)
window = curses.newwin(screen_height, screen_width, 0, 0)  # Create a window with full screen dimensions
window.keypad(1)  # Enable the keypad to capture special keys like arrow keys
window.timeout(100)  # Set the refresh rate (in milliseconds) for the window to control the game speed

# Initial snake position and food placement
snk_x = screen_width // 4  # Set the snake's initial x-coordinate (1/4th of the screen width)
snk_y = screen_height // 2  # Set the snake's initial y-coordinate (middle of the screen height)
snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]  # Initialize the snake with 3 segments
food = [screen_height // 2, screen_width // 2]  # Place the food at the center of the screen
window.addch(food[0], food[1], curses.ACS_DIAMOND)  # Display the food as a diamond character

# Initial settings for the game
key = curses.KEY_RIGHT  # The snake initially moves to the right
score = 0  # Start the score at 0
speed = 100  # Set an initial speed (unused directly in this version)
paused = False  # The game is not paused at the start

# Function to display the score on the screen
def display_score(score):
    score_text = f'Score: {score}'  # Format the score as a string
    window.addstr(0, 2, score_text)  # Display the score at the top left of the screen

# Function to handle game over
def game_over():
    window.clear()  # Clear the screen
    window.addstr(screen_height // 2, screen_width // 2 - 5, "GAME OVER")  # Display 'GAME OVER' in the center
    window.addstr(screen_height // 2 + 1, screen_width // 2 - 5, f"Final Score: {score}")  # Show final score
    window.refresh()  # Refresh the screen to display the messages
    curses.napms(2000)  # Pause for 2 seconds to let the player see the game over message
    curses.endwin()  # End the curses window session and return terminal to normal
    quit()  # Exit the game

# Main game loop (runs until the game is over or the player quits)
while True:
    if not paused:
        # Increase speed as score increases by reducing timeout value, capped to a minimum of 10ms
        window.timeout(100 - (min(90, score * 2)))

        # Handle key press for movement or pause
        next_key = window.getch()  # Capture the next key press
        if next_key == ord('p'):  # If 'p' is pressed, pause the game
            paused = True
            continue  # Skip the rest of the loop while paused
        key = key if next_key == -1 else next_key  # If no key is pressed, continue moving in the current direction

        # Check for collisions with the walls or self
        if (snake[0][0] in [0, screen_height] or  # Check if the snake's head hits the top/bottom wall
            snake[0][1] in [0, screen_width] or  # Check if the snake's head hits the left/right wall
            snake[0] in snake[1:]):  # Check if the snake collides with itself
            game_over()  # End the game if any of these conditions are true

        # Calculate the new head position based on the current direction
        new_head = [snake[0][0], snake[0][1]]  # Copy the current head position
        if key == curses.KEY_DOWN:
            new_head[0] += 1  # Move the head down
        if key == curses.KEY_UP:
            new_head[0] -= 1  # Move the head up
        if key == curses.KEY_RIGHT:
            new_head[1] += 1  # Move the head to the right
        if key == curses.KEY_LEFT:
            new_head[1] -= 1  # Move the head to the left

        # Insert the new head at the front of the snake (snake moves in the new direction)
        snake.insert(0, new_head)

        # Check if the snake has eaten the food
        if snake[0] == food:  # If the snake's head is on the food's position
            score += 1  # Increase the score by 1
            food = None  # Remove the current food
            # Generate a new food position that doesn't overlap with the snake
            while food is None:
                new_food = [random.randint(1, screen_height - 1), random.randint(1, screen_width - 1)]
                food = new_food if new_food not in snake else None  # Ensure new food isn't on the snake
            window.addch(food[0], food[1], curses.ACS_DIAMOND)  # Display the new food on the screen
        else:
            # Move the snake forward by removing the last segment (tail)
            tail = snake.pop()  # Remove the last part of the snake
            window.addch(tail[0], tail[1], ' ')  # Clear the space where the tail was

        # Draw the snake's new head on the screen
        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)  # Display the snake as blocks
        display_score(score)  # Update the score on the screen

    else:
        # If the game is paused, show the pause message
        window.addstr(screen_height // 2, screen_width // 2 - 5, "PAUSED")  # Display 'PAUSED' in the center
        window.refresh()  # Refresh the screen to show the pause message
        next_key = window.getch()  # Wait for the next key press
        if next_key == ord('p'):  # Resume the game when 'p' is pressed again
            paused = False  # Unpause the game
            window.clear()  # Clear the screen to remove the pause message
            # Redraw the snake and food after unpausing
            for segment in snake:
                window.addch(segment[0], segment[1], curses.ACS_CKBOARD)  # Draw each part of the snake
            window.addch(food[0], food[1], curses.ACS_DIAMOND)  # Redraw the food
            display_score(score)  # Redisplay the score
