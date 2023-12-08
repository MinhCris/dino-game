import pygame
import random

pygame.init()

width , height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space INvaders")

BLACK = (0,0,0)
WHITE = (255,255,255)

player_size = 50
player_x = width //2 - player_size//2
player_y = height -2 * player_size
player_speed = 5

enemy_size = 50
enemy_x = random.randint(0,width-enemy_size)
enemy_y = 0
enemy_speed =3

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x >0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed
        
    enemy_y += enemy_speed
    if enemy_y> height:
        enemy_x = random.randint(0, width-enemy_size)
        enemy_x =0
        
    if (player_x + player_size > enemy_x and player_x < enemy_x + enemy_size) and \
        (player_y + player_size > enemy_y and player_y < enemy_y + enemy_size):
            running=False
            
    pygame.draw.rect(screen, WHITE, (player_x,player_y,player_size,player_size))
    
    pygame.d 