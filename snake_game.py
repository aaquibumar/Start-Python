import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the game window
window_width = 800
window_height = 600

# Set the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Create the game window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Set the game clock
clock = pygame.time.Clock()

# Set the size of the snake and the speed of movement
snake_block_size = 20
snake_speed = 15

# Set the font style and size
font_style = pygame.font.SysFont(None, 50)

# Function to display the score on the game window
def display_score(score):
    score_text = font_style.render(f"Score: {score}", True, black)
    game_window.blit(score_text, [window_width // 3, window_height // 3])

# Function to draw the snake on the game window
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, green, [x[0], x[1], snake_block_size, snake_block_size])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = window_width // 2
    y1 = window_height // 2

    # Initial movement of the snake
    x1_change = 0
    y1_change = 0

    # Create the snake's body as a list
    snake_list = []
    length_of_snake = 1

    # Set the position of the food randomly
    foodx = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0

    while not game_over:
        while game_close:
            # Display game over message and the final score
            game_window.fill(white)
            display_score(length_of_snake - 1)
            pygame.display.update()

            # Ask the player to play again or quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Control the movement of the snake using arrow keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # Check if the snake hits the boundaries of the game window
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change
        game_window.fill(white)

        # Draw the food on the game window
        pygame.draw.rect(game_window, red, [foodx, foody, snake_block_size, snake_block_size])

        # Create a list to hold the positions of the snake's head and body
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Remove the tail of the snake when it moves
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake collides with itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake on the game window
        draw_snake(snake_block_size, snake_list)

        # Update the game window
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0
            length_of_snake += 1

        # Set the speed of the game
        clock.tick(snake_speed)

    # Quit the game
    pygame.quit()
    quit()

# Start the game loop
game_loop()
