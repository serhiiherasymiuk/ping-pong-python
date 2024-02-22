import pygame

class Ball:
    def __init__(self, x, y, radius, color, velocity):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def check_collision_with_walls(self, width, height):
        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.velocity = (-self.velocity[0], self.velocity[1])
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.velocity = (self.velocity[0], -self.velocity[1])
