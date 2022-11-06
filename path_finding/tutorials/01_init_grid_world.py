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


def draw():
    win.fill(WHITE)
    for i in range(ROWS):
        pygame.draw.line(win, GREY, (0, i*spot_height), (WIDTH, i*spot_height))
    for j in range(COLS):
        pygame.draw.line(win, GREY, (j*spot_width, 0), (j * spot_width, HEIGHT))
    pygame.display.update()


if __name__ == '__main__':
    run = True
    while run:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
