import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load('Images/outer-space.png'))
playerImg = pygame.image.load('Images/spaceship.png')
ufoImg = pygame.image.load("Images/ufo.png")
bulletImg = pygame.image.load("Images/bullet.png")
x_player = 362
y_player = 516
x_enemy = random.randint(1, 735)
y_enemy = -64
x_change = 0
y_change = 0
x_change_enemy = 2
y_change_enemy = 0.5
x_bullet = x_player
y_bullet = y_player
y_change_bullet = -5
bullet_state = 0
score_val = 0
font = pygame.font.Font("Font Used/Marlboro.ttf", 32)


def score():
    scores = font.render("Score: " + str(score_val), True, (255, 255, 255))
    screen.blit(scores, (10, 10))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(ufoImg, (x, y))


def bullet(x, y):
    global bullet_state
    screen.blit(bulletImg, (x + 16, y + 10))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                x_change = -3
            if event.key == pygame.K_RIGHT:
                x_change = 3
            if event.key == pygame.K_UP:
                y_change = -3
            if event.key == pygame.K_DOWN:
                y_change = 3
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('Sounds/laser.wav')
                bullet_sound.play()
                bullet(x_bullet, y_bullet)
                bullet_state = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

    x_player += x_change
    y_player += y_change
    x_enemy += x_change_enemy
    y_enemy += y_change_enemy
    if y_bullet > -32 and bullet_state == 1:
        y_bullet += y_change_bullet
    else:
        x_bullet = x_player
        y_bullet = y_player
        bullet_state = 0

    if 0 >= x_enemy or x_enemy >= 736:
        x_change_enemy = -x_change_enemy

    distance_e_b = math.sqrt(pow(x_enemy - x_bullet, 2) + pow(y_enemy - y_bullet, 2))
    if distance_e_b <= 20:
        mixer.Sound('Sounds/kill.wav').play()
        x_bullet = x_player
        y_bullet = y_player
        bullet_state = 0
        score_val += 1
        x_enemy = random.randint(1, 735)
        y_enemy = -64
        if x_change_enemy < 0:
            x_change_enemy -= 0.4
        else:
            x_change_enemy += 0.4
        print(score)
    distance_e_p = math.sqrt(pow(x_enemy - x_player, 2) + pow(y_enemy - y_player, 2))
    if distance_e_p <= 30 or y_enemy > 550:
        running = False

    if x_player <= 0:
        x_player = 5
    elif x_player >= 736:
        x_player = 731
    screen.blit(pygame.image.load("Images/space.jpeg"), (0, 0))
    bullet(x_bullet, y_bullet)
    player(x_player, y_player)
    enemy(x_enemy, y_enemy)
    score()
    pygame.display.update()
