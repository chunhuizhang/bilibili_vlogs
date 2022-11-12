import pygame
from pygame.locals import *
from queue import PriorityQueue

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


class Spot:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.x = c * spot_width
        self.y = r * spot_height
        self.color = WHITE
        self.is_start = False
        self.is_barrier = False
        self.is_end = False

    def make_start(self):
        self.color = ORANGE
        self.is_start = True

    def make_end(self):
        self.color = TURQUOISE
        self.is_end = True

    def make_barrier(self):
        self.color = BLACK
        self.is_barrier = True

    def make_open(self):
        self.color = GREEN

    def make_path(self):
        self.color = PURPLE

    def make_closed(self):
        self.color = RED


    def update_neighbors(self):
        self.neighbors = []
        if self.c > 0 and not grid_world[self.r][self.c - 1].is_barrier:
            self.neighbors.append(grid_world[self.r][self.c - 1])
        if self.c < COLS - 1 and not grid_world[self.r][self.c + 1].is_barrier:
            self.neighbors.append(grid_world[self.r][self.c + 1])
        if self.r > 0 and not grid_world[self.r-1][self.c].is_barrier:
            self.neighbors.append(grid_world[self.r-1][self.c])
        if self.r < ROWS - 1 and not grid_world[self.r+1][self.c].is_barrier:
            self.neighbors.append(grid_world[self.r+1][self.c])


    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, spot_width, spot_height))

    def __lt__(self, other):
        return False


grid_world = []


def make_grid_world():
    for r in range(ROWS):
        grid_world.append([])
        for c in range(COLS):
            grid_world[r].append(Spot(r, c))


def draw():
    win.fill(WHITE)

    for r in range(ROWS):
        for c in range(COLS):
            spot = grid_world[r][c]
            spot.draw(win)

    for i in range(ROWS):
        pygame.draw.line(win, GREY, (0, i*spot_height), (WIDTH, i*spot_height))
    for j in range(COLS):
        pygame.draw.line(win, GREY, (j*spot_width, 0), (j * spot_width, HEIGHT))

    pygame.display.update()


def map_pos_to_spot(pos):
    x, y = pos
    r, c = y//spot_height, x//spot_width
    return r, c

# 曼哈顿距离
def h(spot1, spot2):
    x1, y1 = spot1.c, spot1.r
    x2, y2 = spot2.c, spot2.r
    return abs(x1-x2) + abs(y1-y2)


def reconstruct_path(path_from, current):
    while current in path_from:
        current = path_from[current]
        current.make_path()
        draw()

def algo(start, end):
    pq = PriorityQueue()
    pq.put((float('inf'), start))

    f_score = {spot: float('inf') for row in grid_world for spot in row}
    g_score = {spot: float('inf') for row in grid_world for spot in row}

    g_score[start] = 0
    f_score[start] = h(start, end)

    # f = g + h
    # f(current) = g(current) + h(current)
    # f(current) 经过 current 节点的预估路径
    # g(current)：走到 current 需要经过的距离
    # h(current)：预估的一个距离

    path_from = {}

    while not pq.empty():
        current = pq.get()[1]

        if current == end:
            reconstruct_path(path_from, end)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            tmp_g_score = g_score[current] + 1

            if tmp_g_score < g_score[neighbor]:
                neighbor.make_open()
                path_from[neighbor] = current
                g_score[neighbor] = tmp_g_score
                f_score[neighbor] = tmp_g_score + h(neighbor, end)
                pq.put((f_score[neighbor], neighbor))
        draw()

        if current != start:
            current.make_closed()

    return False



if __name__ == '__main__':
    run = True
    make_grid_world()
    start = None
    end = None
    while run:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            left, center, right = pygame.mouse.get_pressed()
            # if left:
            #     print('left')
            # if center:
            #     print('center')
            # if right:    for r in range(ROWS):
            #         for c in range(COLS):
            #             spot = grid_world[r][c]
            #             spot.draw(win)
            #     print('right')
            if left:
                pos = pygame.mouse.get_pos()
                r, c = map_pos_to_spot(pos)
                spot = grid_world[r][c]
                if not start:
                    start = spot
                    start.make_start()
                elif not end:
                    end = spot
                    end.make_end()
                else:
                    spot.make_barrier()

            if event.type == KEYDOWN:
                if event.key == K_SPACE and start and end:
                    for row in grid_world:
                        for spot in row:
                            spot.update_neighbors()
                    algo(start, end)

