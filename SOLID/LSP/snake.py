from typing import List, Tuple, Optional
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, GRID_WIDTH, GRID_HEIGHT, SNAKE_COLOR
from game import GameObject
import pygame

class Snake(GameObject):
    def __init__(self):
        start_pos = (GRID_WIDTH // 2 * GRID_SIZE, GRID_HEIGHT // 2 * GRID_SIZE)
        super().__init__(start_pos, SNAKE_COLOR)
        self.length = 1
        self.positions: List[Tuple[int, int]] = [self.position]
        self.direction = (1, 0)
        self.next_direction: Optional[Tuple[int, int]] = None

    def update_direction(self, new_direction: Tuple[int, int]) -> None:
        if new_direction != (-self.direction[0], -self.direction[1]):
            self.next_direction = new_direction

    def move(self) -> None:
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

        head = self.positions[0]
        dx, dy = self.direction
        new_head = ((head[0] + dx * GRID_SIZE) % SCREEN_WIDTH,
                    (head[1] + dy * GRID_SIZE) % SCREEN_HEIGHT)

        if new_head in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new_head)
            if len(self.positions) > self.length:
                self.positions.pop()

    def get_head_position(self) -> Tuple[int, int]:
        return self.positions[0]

    def reset(self) -> None:
        self.__init__()

    def draw(self, surface: pygame.Surface) -> None:
        for pos in self.positions[1:]:
            self.draw_cell(surface, pos)
        self.draw_cell(surface, self.positions[0], self.body_color)