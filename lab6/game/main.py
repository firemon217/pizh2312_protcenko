from random import randint
import pygame
from apple import Apple
from snake import Snake

# Инициализация PyGame:
pygame.init()

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()

def handle_keys(snake: Snake) -> None:
    """
    Обрабатывает нажатия клавиш для управления змейкой.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.update_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.update_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.update_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.update_direction(RIGHT)
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit

if __name__ == '__main__':
    """
    Главный игровой цикл:
    - Создаёт экземпляры змейки и яблока.
    - Обрабатывает ввод с клавиатуры.
    - Обновляет положение змейки.
    - Проверяет, съела ли змейка яблоко.
    - Перерисовывает экран.
    """
    snake = Snake()
    apple = Apple()
    print(f'Начальная длина змейки: {snake.length}')

    while True:
        clock.tick(SPEED)

        handle_keys(snake)
        snake.move()

        # Проверка, съела ли змейка яблоко
        if snake.get_head_position() == apple.position:
            snake.length += 1  # Увеличение длины змейки
            apple.randomize_position()
            print(f'Новое яблоко на позиции: {apple.position}')
            
            # Гарантия, что яблоко не появится внутри змейки
            while apple.position in snake.positions:
                apple.randomize_position()

        # Отрисовка игрового экрана
        screen.fill(BOARD_BACKGROUND_COLOR)
        snake.draw(screen)
        apple.draw(screen)

        pygame.display.update()