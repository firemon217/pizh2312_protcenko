from random import randint
from config import GRID_WIDTH, GRID_HEIGHT, GRID_SIZE, APPLE_COLOR
from game import GameObject
import pygame

class Apple(GameObject):
    def __init__(self):
        super().__init__((0, 0), APPLE_COLOR)
        self.randomize_position([])

    def randomize_position(self, exclude_positions) -> None:
        while True:
            x = randint(0, GRID_WIDTH - 1) * GRID_SIZE
            y = randint(0, GRID_HEIGHT - 1) * GRID_SIZE
            pos = (x, y)
            if pos not in exclude_positions:
                self.position = pos
                break

    def draw(self, surface: pygame.Surface) -> None:
        self.draw_cell(surface, self.position)