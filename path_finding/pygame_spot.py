
import pygame
from pygame.locals import *
height = 800
width = height
win = pygame.display.set_mode((width, width))

pygame.display.set_caption("grid world")

rows = 50
cols = rows

spot_width = height//rows
spot_height = spot_width

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


def make_grid(win):
    grid_world = []
    for i in range(rows):
        grid_world.append([])
        for j in range(rows):
            spot = Spot(i, j)
            grid_world[i].append(spot)
    return grid_world


def draw_grid(win):
    gap = width//rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))
    for j in range(cols):
        pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, height))


def draw(win, grid_world):
    win.fill(WHITE)

    for i in range(rows):
        for j in range(cols):
            grid_world[i][j].draw(win)
    draw_grid(win)
    pygame.display.update()


def map_clicked_pos(pos):
    x, y = pos
    r = y//spot_width
    c = x//spot_width
    return r, c

if __name__ == '__main__':
    run = True
    start, end = None, None
    grid_world = make_grid(win)
    while run:
        draw(win, grid_world)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            left, center, right = pygame.mouse.get_pressed()
            if left:
                pos = pygame.mouse.get_pos()
                r, c = map_clicked_pos(pos)
                print(r, c, 'clicked')
                spot = grid_world[r][c]
                if not start:
                    start = spot
                    start.make_start()
                elif not end:
                    end = spot
                    end.make_end()

