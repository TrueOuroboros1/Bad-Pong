
# A simple Pong game with pygame. No pause menus, no game over screen, no sound, no fancy not-pong mechanics. Not even a way to keep score. 
# It's literally just Pong. As simple a version of Pong I could make while feeling like I did something. 
# Now, if we ignore the lack of the things mentioned in line 2, then that means I finally finished a personal project. WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

#Left-Side Player controls their paddle with "w" and "s", and Right-Side Player controls their paddle with the "up" and "down" arrow keys.

#imports
import pygame
import numpy
import sys
import os

#Inputs
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_w,
    K_s,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#Initialize all pygame modules
pygame.init()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    
#Size is in pixels
screen_width = 800
screen_height = 800

#Create context
context = pygame.display.set_mode([screen_width, screen_height])

#The ball
ball = Ball()
ball_pos = [(screen_width-ball.surf.get_width())/2, (screen_width-ball.surf.get_height())/2]
ball_vel = numpy.array((-0.1, 0.1))

#Player's "Paddle" 
paddle = pygame.Surface((20, 100))
paddle.fill((255, 255, 255))
rect = paddle.get_rect()
paddle_pos_y = 250 - (paddle.get_height()/2)

#Other player's paddle(I know I should make a Paddle class but I don't wanna)
paddle2 = pygame.Surface((20, 100))
paddle2.fill((255, 255, 255))
rect = paddle2.get_rect()
paddle2_pos_y = 250 - (paddle2.get_height()/2)

#Colliders
ball_collider = pygame.Rect(ball.surf.get_rect())
paddle1_collider = pygame.Rect(paddle.get_rect())
paddle2_collider = pygame.Rect(paddle2.get_rect())

#Gameplay loop
running = True
while running:
    #Way to stop program, otherwise user can only force end task
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #Clicking escape key pauses game(still need to make it pause and make the pause screen)
            if event.type == K_ESCAPE:
                pass
        #Clicking the "X" on the window exits the game
        if event.type == QUIT:
            running = False

    #Background with black color
    context.fill((0, 0, 0))

    #Take player input and update paddle y positions
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP] and paddle2_pos_y > 0:
        paddle2_pos_y -= 0.4
    if pressed_keys[K_DOWN] and paddle2_pos_y < (screen_height - paddle2.get_height()):
        paddle2_pos_y += 0.4

    if pressed_keys[K_w] and paddle_pos_y > 0:
        paddle_pos_y -= 0.4
    if pressed_keys[K_s] and paddle_pos_y < (screen_height - paddle.get_height()):
        paddle_pos_y += 0.4
        

    #Update paddle positions and put them on top of the current context
    paddle_pos = (20, paddle_pos_y)
    paddle2_pos = (screen_width-40, paddle2_pos_y)
    context.blit(paddle, paddle_pos)
    context.blit(paddle2, paddle2_pos)
    
    #Check for collisions
    paddle1_collider.topleft = paddle_pos
    paddle2_collider.topleft = paddle2_pos
    ball_collider.topleft = ball_pos
    collide_left = paddle1_collider.colliderect(ball_collider)
    collide_right = paddle2_collider.colliderect(ball_collider)
    
    #Update ball velocity vector
    if collide_left or collide_right:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[0] < 0 or ball_pos[0] > (context.get_width() - ball.surf.get_width()):
        exit()
    if ball_pos[1] < 0 or ball_pos[1] > (context.get_height() - ball.surf.get_height()):
        ball_vel[1] = -ball_vel[1]
        

    #Update ball position and put it on top of the current context
    ball_pos[0] += ball_vel[0]
    ball_pos[1] -= ball_vel[1]
    context.blit(ball.surf, ball_pos)

    #Render
    pygame.display.flip()

#Uninitialize all pygame modules
pygame.quit()
