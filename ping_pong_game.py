import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
BALL_SIZE = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
FPS = 60

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Set up the clock
clock = pygame.time.Clock()

# Set up the ball
ball_x = WIDTH / 2
ball_y = HEIGHT / 2
ball_dx = 5
ball_dy = 5

# Set up the paddles
paddle1_y = HEIGHT / 2
paddle2_y = HEIGHT / 2

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_y -= 5
    if keys[pygame.K_s]:
        paddle1_y += 5
    if keys[pygame.K_UP]:
        paddle2_y -= 5
    if keys[pygame.K_DOWN]:
        paddle2_y += 5

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce the ball off the walls
    if ball_y < 0 or ball_y > HEIGHT - BALL_SIZE:
        ball_dy *= -1

    # Bounce the ball off the paddles
    if ball_x < PADDLE_WIDTH and paddle1_y - PADDLE_HEIGHT / 2 < ball_y < paddle1_y + PADDLE_HEIGHT / 2:
        ball_dx *= -1
    if ball_x > WIDTH - PADDLE_WIDTH - BALL_SIZE and paddle2_y - PADDLE_HEIGHT / 2 < ball_y < paddle2_y + PADDLE_HEIGHT / 2:
        ball_dx *= -1

    # Score points
    if ball_x < 0:
        print("Player 2 scores!")
        ball_x = WIDTH / 2
        ball_y = HEIGHT / 2
        ball_dx *= -1
    if ball_x > WIDTH - BALL_SIZE:
        print("Player 1 scores!")
        ball_x = WIDTH / 2
        ball_y = HEIGHT / 2
        ball_dx *= -1

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, paddle1_y - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, paddle2_y - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)