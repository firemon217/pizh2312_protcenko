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

