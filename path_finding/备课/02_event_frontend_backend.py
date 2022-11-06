import pygame
from pygame.locals import *

WIDTH = 800
HEIGHT = WIDTH

COLS = 50
ROWS = COLS

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# spot
spot_width = WIDTH//COLS
spot_height = HEIGHT // ROWS

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('grid world')

grid_world = []


class Spot:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.x = c * spot_width
        self.y = r * spot_height
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, spot_width, spot_height))


def make_grid():
    for r in range(ROWS):
        grid_world.append([])
        for c in range(COLS):
            grid_world[r].append(Spot(r, c))


def draw():
    win.fill(WHITE)

    for r in range(ROWS):
        for c in range(COLS):
            grid_world[r][c].draw(win)

    for i in range(ROWS):
        pygame.draw.line(win, GREY, (0, i*spot_height), (WIDTH, i*spot_height))
    for j in range(COLS):
        pygame.draw.line(win, GREY, (j*spot_width, 0), (j * spot_width, HEIGHT))

    pygame.display.update()


def map_pressed_pos(pos):
    x, y = pos
    return x//spot_width, y//spot_height


if __name__ == '__main__':
    run = True
    start = None
    end = None
    make_grid()
    while run:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            left, center, right = pygame.mouse.get_pressed()
            if left:
                pos = pygame.mouse.get_pos()
                c, r = map_pressed_pos(pos)
                spot = grid_world[r][c]
                if not start:
                    start = spot
                    start.make_start()
                elif not end:
                    end = spot
                    end.make_end()
