'''
simple display with moving ball
'''
import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Moving Ball")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 200
pos_y = 200

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pos_x -= 10

    if key_event[pygame.K_RIGHT]:
        pos_x += 10

    if key_event[pygame.K_UP]:
        pos_y -= 10

    if key_event[pygame.K_DOWN]:
        pos_y += 10

    if pos_x > SCREEN_WIDTH:
        pos_x = SCREEN_WIDTH
    
    if pos_x < 0 :
        pos_x = 0
    
    if pos_y > SCREEN_HEIGHT:
        pos_y = SCREEN_HEIGHT
    
    if pos_y < 0 :
        pos_y = 0

    screen.fill(black)
    pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
    pygame.display.update()
