import pygame
import random

# Initialize Pygame
pygame.init()


# Set the window size
window_width = 800
window_height = 600

# Create the window
screen = pygame.display.set_mode((window_width, window_height))

# Set the game caption
pygame.display.set_caption("Dodger")

# Set up the clock
clock = pygame.time.Clock()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the player
player_width = 50
player_height = 50
player_x = window_width / 2 - player_width / 2
player_y = window_height - player_height
player_speed = 5

# Set up the falling objects
object_width = 50
object_height = 50
object_x = random.randint(0, window_width - object_width)
object_y = 0
object_speed = 5

# Define the game loop
game_over = False
score = 0

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Move the falling object
    object_y += object_speed

    # Check for collision
    if object_y > player_y - object_height and object_y < player_y + player_height and object_x > player_x - object_width and object_x < player_x + player_width:
        score += 1
        object_x = random.randint(0, window_width - object_width)
        object_y = 0

    # Check if the object has reached the bottom of the screen
    if object_y > window_height:
        object_x = random.randint(0, window_width - object_width)
        object_y = 0

    # Draw the objects
    screen.fill(white)
    pygame.draw.rect(screen, black, [player_x, player_y, player_width, player_height])
    pygame.draw.rect(screen, red, [object_x, object_y, object_width, object_height])

    # Draw the score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), 1, black)
    screen.blit(text, (10, 10))

    # Update the screen
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
