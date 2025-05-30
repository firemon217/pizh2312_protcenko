from abc import ABC, abstractmethod
import pygame

class GameObject(ABC):
    def __init__(self, position, color):
        self.position = position
        self.body_color = color

    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None:
        pass

    def draw_cell(self, surface: pygame.Surface, pos, color=None) -> None:
        rect = pygame.Rect(pos[0], pos[1], 20, 20)
        pygame.draw.rect(surface, color or self.body_color, rect)