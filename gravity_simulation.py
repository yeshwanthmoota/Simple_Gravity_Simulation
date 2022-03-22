

# program to demonstrate projectile motion of a horizontally launched body from a certain height

import pygame
import os
import sys

WIDTH = 800
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
INITIAL_POS = (0 + 100, HEIGHT*0.75)
BALL_RADIUS = 20
GRAVITY = 0.5 # px/frame^2
BALL_VEL_X = 10 # px/frame
INITIAL_Y_VEL = -10

pygame.init()

gameDisplay = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Gravity Simulation")


FPS = 60


GRAY = (180,180,180)
BLACK = (0,0,0)
YELLOW = (255,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN= (0,255,0)


class Ball:
    def __init__(self, pos):
        self.x = pos[0] # x position
        self.y = pos[1] # y position
        self.vel_x = BALL_VEL_X # initial x velocity
        self.vel_y = -10 # initial y velocity
    def motion_simulation(self, jump, key_pressed): # changes the x and y positions of the ball according to gravity
        if key_pressed[pygame.K_a]:
            self.x -= self.vel_x
        if key_pressed[pygame.K_d]:
            self.x += self.vel_x
        if jump:
            self.vel_y = INITIAL_Y_VEL
        self.y += self.vel_y
        self.vel_y += GRAVITY
    def draw_ball(self):
        pygame.draw.circle(gameDisplay,RED, (self.x, self.y), BALL_RADIUS, 0)



def draw_display(ball):
    gameDisplay.fill(BLACK)
    ball.draw_ball()
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    running = True


    ball = Ball(INITIAL_POS)

    while running:
        clock.tick(FPS)
        jump = False
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump = True

        draw_display(ball)
        ball.motion_simulation(jump, key_pressed)
    pygame.quit()


if __name__=='__main__':
    main()