import pygame

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong")

# Constants
BALL_RADIUS = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7

# Colors
BLACK = (0, 0, 0)


def play_ping_pong():
    clock = pygame.time.Clock()
    ball = Ball()
    player_paddle = Paddle(20)
    opponent_paddle = Paddle(SCREEN_WIDTH - 30)
    scoreboard = Scoreboard()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_paddle.move_up()
        if keys[pygame.K_s]:
            player_paddle.move_down()

        # AI for opponent paddle
        if ball.speed_x > 0:
            if ball.y < opponent_paddle.y + opponent_paddle.height // 2:
                opponent_paddle.move_up()
            elif ball.y > opponent_paddle.y + opponent_paddle.height // 2:
                opponent_paddle.move_down()

        ball.move()

        # Ball collision with walls
        if ball.y <= 0 or ball.y >= SCREEN_HEIGHT:
            ball.speed_y *= -1

        # Ball collision with paddles
        if (ball.x - BALL_RADIUS <= player_paddle.x + PADDLE_WIDTH and
            player_paddle.y <= ball.y <= player_paddle.y + PADDLE_HEIGHT):
            ball.speed_x *= -1
        elif (ball.x + BALL_RADIUS >= opponent_paddle.x and
              opponent_paddle.y <= ball.y <= opponent_paddle.y + PADDLE_HEIGHT):
            ball.speed_x *= -1
        elif ball.x - BALL_RADIUS < 0:
            scoreboard.opponent_score += 1
            ball = Ball()
        elif ball.x + BALL_RADIUS > SCREEN_WIDTH:
            scoreboard.player_score += 1
            ball = Ball()

        screen.fill(BLACK)
        ball.draw(screen)
        player_paddle.draw(screen)
        opponent_paddle.draw(screen)
        scoreboard.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    play_ping_pong()
