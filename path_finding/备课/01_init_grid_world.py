import pygame

WIDTH = 800
HEIGHT = WIDTH

COLS = 50
ROWS = COLS

SPOT_WIDTH = WIDTH//COLS
SPOT_HEIGHT = HEIGHT//ROWS


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


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('grid world')

def draw():
    win.fill(WHITE)
    for i in range(COLS):
        pygame.draw.line(win, GREY, (i*SPOT_WIDTH, 0), (i*SPOT_WIDTH, HEIGHT))
    for j in range(ROWS):
        pygame.draw.line(win, GREY, (0, j*SPOT_HEIGHT), (WIDTH, j*SPOT_HEIGHT))
    pygame.display.update()


if __name__ == '__main__':
    run = True

    while run:
        draw()
