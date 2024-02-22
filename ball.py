import random

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Constants
BALL_RADIUS = 10
BALL_SPEED = 5


class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.radius = BALL_RADIUS
        self.speed_x = BALL_SPEED * random.choice([1, -1])
        self.speed_y = BALL_SPEED * random.choice([1, -1])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)
