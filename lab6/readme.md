# Лабораторная по ООП №6
## Практическая работа 

#### apple
~~~python
import pygame
from random import randint
from game_object import GameObject

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Цвет яблока
APPLE_COLOR = (255, 125, 0)

class Apple(GameObject):
    """Яблоко"""

    def __init__(self) -> None:
        """Инициализирует яблоко на игры поле."""
        super().__init__(None, APPLE_COLOR)
        self.randomize_position()

    def randomize_position(self) -> None:
        """Установка случайное положение яблоко на игры поле."""
        self.position = (randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                         randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, surface: pygame.Surface) -> None:
        """Отрисовывает яблоко на игры поверхности."""
        self.draw_cell(surface, self.position)


~~~

#### main
~~~python
ifrom random import randint
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

~~~

#### snake
~~~python
import pygame
from game_object import GameObject
from typing import Optional, Tuple, List

# Константы экрана и сетки
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480  # Размеры окна
GRID_SIZE = 20  # Размер одной клетки
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE  # Количество клеток по горизонтали
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE  # Количество клеток по вертикали
SNAKE_COLOR = (0, 255, 125)  # Цвет змейки


class Snake(GameObject):
    """
    Класс, представляющий змейку в игре.
    """

    def __init__(self) -> None:
        """
        Инициализирует змейку в центре экрана.
        """
        super().__init__((GRID_WIDTH // 2 * GRID_SIZE, GRID_HEIGHT // 2 * GRID_SIZE), SNAKE_COLOR)
        self.length: int = 1
        self.positions: List[Tuple[int, int]] = [self.position]
        self.direction: Tuple[int, int] = (1, 0)
        self.next_direction: Optional[Tuple[int, int]] = None

    def update_direction(self, new_direction: Tuple[int, int]) -> None:
        """
        Обновляет направление движения змейки, если оно не противоположное текущему.
        """
        if new_direction != (-self.direction[0], -self.direction[1]):
            self.next_direction = new_direction

    def move(self) -> None:
        """
        Перемещает змейку на одну клетку в текущем направлении.
        Если змейка сталкивается с собой, игра сбрасывается.
        """
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

        cur_head = self.positions[0]  # Текущая голова змейки
        x, y = self.direction
        
        # Рассчитываем новую позицию головы с учётом границ экрана
        new_head = ((cur_head[0] + x * GRID_SIZE) % SCREEN_WIDTH,
                    (cur_head[1] + y * GRID_SIZE) % SCREEN_HEIGHT)

        # Проверяем столкновение с телом
        if len(self.positions) > 2 and new_head in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new_head)  # Добавляем новую голову
            if len(self.positions) > self.length:
                self.positions.pop()  # Удаляем последний сегмент, если змейка не растёт

    def get_head_position(self) -> Tuple[int, int]:
        """
        Возвращает текущие координаты головы змейки.
        
        :return: Кортеж с координатами (x, y).
        """
        return self.positions[0]

    def reset(self) -> None:
        """
        Сбрасывает змейку в начальное состояние после столкновения с собой.
        """
        self.length = 1
        self.positions = [(GRID_WIDTH // 2 * GRID_SIZE, GRID_HEIGHT // 2 * GRID_SIZE)]
        self.direction = (1, 0)
        self.next_direction = None

    def draw(self, surface: pygame.Surface) -> None:
        """
        Отображает змейку на игровом поле.
        Голова выделяется отдельным цветом.
        
        :param surface: Поверхность Pygame, на которой рисуется змейка.
        """
        for position in self.positions[:-1]:
            self.draw_cell(surface, position)  # Отрисовка тела змейки
        
        self.draw_cell(surface, self.positions[0], SNAKE_COLOR)  # Отрисовка головы


~~~

#### game_object
~~~python
import pygame
from typing import Optional, Tuple

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
BORDER_COLOR = (0, 0, 0)

class GameObject:
    """Экран обьекта"""

    def __init__(self, position: Optional[Tuple[int, int]] = None,
                 body_color: Optional[Tuple[int, int, int]] = None) -> None:
        """Инициализация объект на игры поле."""
        self.position = position or (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = body_color or (255, 255, 255)

    def draw(self, surface: pygame.Surface) -> None:
        """Абстрактный метод для отрисовки объект на экран."""
        pass

    def draw_cell(self, surface: pygame.Surface, position: Tuple[int, int],
                  color: Optional[Tuple[int, int, int]] = None) -> None:
        """Отрисовывает ячейка на экран."""
        rect = rect = pygame.Rect(position[0], position[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, color or self.body_color, rect)
        pygame.draw.rect(surface, BORDER_COLOR, rect, 1)


~~~