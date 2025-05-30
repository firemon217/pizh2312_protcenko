# config.py

# Размеры экрана
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Размер одной клетки на поле
GRID_SIZE = 20

# Количество клеток по горизонтали и вертикали
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Цвета (RGB)
BORDER_COLOR = (0, 0, 0)
BOARD_BACKGROUND_COLOR = (0, 0, 0)
APPLE_COLOR = (255, 125, 0)
SNAKE_COLOR = (0, 255, 125)

# Скорость игры (FPS или таймер движения)
SPEED = 20

# Направления движения змейки (векторные сдвиги по сетке)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
