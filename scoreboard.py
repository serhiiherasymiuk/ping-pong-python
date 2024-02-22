import pygame

WHITE = (255, 255, 255)


class Scoreboard:
    def __init__(self):
        self.player_score = 0
        self.opponent_score = 0
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        score_text = f"Player: {self.player_score}  Opponent: {self.opponent_score}"
        text = self.font.render(score_text, True, WHITE)
        screen.blit(text, (10, 10))
