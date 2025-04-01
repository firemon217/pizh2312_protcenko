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