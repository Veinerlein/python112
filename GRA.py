import pygame
import random

# ініціалізуємо Pygame
pygame.init()

# встановлюємо розмір екрану
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# кольори
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# створюємо кульку
ball_size = 20
ball = pygame.Surface((ball_size, ball_size))
ball_color = WHITE
ball.fill(ball_color)
ball_rect = ball.get_rect()

# початкова швидкість кульки
ball_speed_x = 5
ball_speed_y = 5

# головний цикл гри
game_over = False
clock = pygame.time.Clock()

while not game_over:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # переміщення кульки
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    # відбивання кульки від країв екрану
    if ball_rect.left < 0 or ball_rect.right > screen_width:
        ball_speed_x = -ball_speed_x
        # зміна кольору кульки
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if ball_rect.top < 0 or ball_rect.bottom > screen_height:
        ball_speed_y = -ball_speed_y
        # зміна кольору кульки
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # оновлення кольору кульки
    ball.fill(ball_color)

    # очищення екрану
    screen.fill(BLACK)

    # малювання кульки
    screen.blit(ball, ball_rect)

    # оновлення екрану
    pygame.display.flip()

    # обмеження швидкості кадрів
    clock.tick(60)

# закриваємо Pygame
pygame.quit()