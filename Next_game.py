import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
import random

pygame.init()

# Задаємо розмір вікна та кольори
screen_width, screen_height = 800, 600
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Створюємо вікно та задаємо його заголовок
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('My Game')

# Створюємо білу кулю та задаємо її початкові координати
ball = pygame.Surface((20, 20))
ball.fill(white)
ball_rect = ball.get_rect(center=(screen_width // 2, screen_height // 2))

# Задаємо швидкість руху білої кулі
ball_speed = 5

# Функція для створення червоної кулі
def create_enemy():
    enemy = pygame.Surface((20, 20))
    enemy.fill(red)
    enemy_rect = enemy.get_rect(center=(screen_width + 20, random.randint(0, screen_height)))
    enemy_speed = random.randint(2, 4)
    return [enemy, enemy_rect, enemy_speed]

# Функція для створення зеленої кулі
def create_bonus():
    bonus = pygame.Surface((25, 25))
    bonus.fill(green)
    bonus_rect = bonus.get_rect(center=(random.randint(0, screen_width), -20))
    bonus_speed = random.randint(1, 3)
    return [bonus, bonus_rect, bonus_speed]

# Задаємо таймери для створення червоних та зелених куль
CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)

# Списки для зберігання червоних та зелених куль
enemies = []
bonuses = []

# Основний цикл гри
running = True
clock = pygame.time.Clock()
while running:
    # Обробка подій
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        elif event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

    # Рух білої кулі за допомогою клавіш "up","left","down","right"
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_UP]:
        ball_rect.move_ip(0, -ball_speed)
    if pressed_keys[K_DOWN]:
        ball_rect.move_ip(0, ball_speed)
    if pressed_keys[K_LEFT]:
        ball_rect.move_ip(-ball_speed, 0)
