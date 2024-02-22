import pygame


class Scoreboard:
    def __init__(self, x, y, font_size, font_color):
        self.x = x
        self.y = y
        self.font_size = font_size
        self.font_color = font_color
        self.score = 0
        self.font = pygame.font.Font(None, self.font_size)

    def increase_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, self.font_color)
        screen.blit(score_text, (self.x, self.y))
