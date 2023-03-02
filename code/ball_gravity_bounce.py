import pygame
import sys

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

DEF_FRAME = 60

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

pygame.init()
pygame.display.set_caption("ball_gravity_bounce")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pos_x = 200
pos_y = SCREEN_HEIGHT - 20
v_x = 0
v_y = 0
g = 1000
jump = False
clock = pygame.time.Clock()

while True:
    
    clock.tick(DEF_FRAME)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if not jump:
        if key_event[pygame.K_LEFT]:
            if v_x > -300:
                v_x -=10
        if key_event[pygame.K_RIGHT]:
            if v_x < 300:
                v_x += 10
        if key_event[pygame.K_DOWN]:
            v_x = 0
        if key_event[pygame.K_UP]:
            v_y = 1000
            jump = True
        if not key_event[pygame.K_LEFT] and not key_event[pygame.K_RIGHT]:#friction
            if v_x > 0:
                v_x -= 5
            if v_x < 0:
                v_x += 5
    
    if jump:
        pos_y -= v_y / 60
        v_y -= g / 60
        if pos_y > SCREEN_HEIGHT - 20:
            pos_y = SCREEN_HEIGHT - 20
            #print(v_y)
            if abs(v_y) < 160:
                v_y = 0
                jump = False
            else:
                v_y *= -0.8
            #jump = False
    
    pos_x += v_x / 60

    if pos_x < 20: 
        pos_x = 20
        v_x *= -1

    if pos_x > SCREEN_WIDTH - 20:
        pos_x = SCREEN_WIDTH - 20
        v_x *= -1
    
    screen.fill(black)
    pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
    pygame.display.update()
    
