import pygame
from .constants import LIGHT_WIGHT, WIGHT, ROWS, COLS, CELL_SIZE, HEIGHT, WIDTH, BOARD


class Board:
    def __init__(self):
        self.board = BOARD

    def draw_grid(self, screen):
        row_width = WIDTH // ROWS
        col_height = HEIGHT // COLS
        x = 0
        y = 0
        screen.fill(WIGHT)
        for row in range(ROWS):
            x += row_width
            y += col_height
            pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, WIDTH), 1)
            pygame.draw.line(screen, (0, 0, 0), (0, y), (HEIGHT, y), 1)

    def create_spdr_ant_pos(self, spider, ant):
        self.board[int(spider.body.x)][int(spider.body.y)] = "S"
        spider.draw_spider()
        try:
            self.board[int(ant.pos.x)][int(ant.pos.y)] = "A"
        except:
            print("Ant win")
        ant.draw_ant()

