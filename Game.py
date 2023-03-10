import pygame
from pygame.constants import QUIT, KEYDOWN, K_r
import random

pygame.init()

screen = width, height = 800, 600
print(screen)
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 123, 21, 4

main_surface = pygame.display.set_mode(screen)
ball = pygame.Surface((20, 20))
color = GREEN # Add color variable
ball.fill(color)
ball_rect = ball.get_rect()
ball_speed = [1, 1]

# Add reflect variable
reflect = False

is_working = True

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

        # Toggle reflect when "r" key is pressed
        if event.type == KEYDOWN:
            if event.key == K_r:
                reflect = not reflect

    ball_rect = ball_rect.move(ball_speed)

    if reflect:
        # Check if ball collides with edges of screen
        if ball_rect.left < 0 or ball_rect.right > width:
            ball_speed[0] = -ball_speed[0]
            # Change ball color after reflection
            color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if ball_rect.top < 0 or ball_rect.bottom > height:
            ball_speed[1] = -ball_speed[1]
            # Change ball color after reflection
            color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    else:
        # Bounce ball off top and bottom of screen
        if ball_rect.bottom >= height or ball_rect.top <= 0:
            ball_speed[1] = -ball_speed[1]

    ball.fill(color) # Update ball color
    main_surface.fill((0, 0, 0))
    main_surface.blit(ball, ball_rect)

    pygame.display.flip()
