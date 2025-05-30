import pygame
from snake import Snake
from apple import Apple
from config import SCREEN_WIDTH, SCREEN_HEIGHT, SPEED, UP, DOWN, LEFT, RIGHT, BOARD_BACKGROUND_COLOR

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Змейка')

snake = Snake()
apple = Apple()

def handle_input() -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); raise SystemExit
            elif event.key == pygame.K_UP:
                snake.update_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.update_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.update_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.update_direction(RIGHT)

while True:
    clock.tick(SPEED)
    handle_input()
    snake.move()

    if snake.get_head_position() == apple.position:
        snake.length += 1
        apple.randomize_position(snake.positions)

    screen.fill(BOARD_BACKGROUND_COLOR)
    snake.draw(screen)
    apple.draw(screen)
    pygame.display.update()