
import random


def random_walk(N):
    x, y = 0, 0
    choices = ['N', 'S', 'E', 'W']
    for i in range(N):
        step = random.choice(choices)
        if step == 'N':
            y += 1
        elif step == 'S':
            y -= 1
        elif step == 'E':
            x += 1
        else:
            x -= 1
    return x, y


def random_walk_2(N):
    x, y = 0, 0
    for i in range(N):
        dx, dy = random.choice([[0, 1], [0, -1], [1, 0], [-1, 0]])
        x += dx
        y += dy
    return x, y


def distance_from_home(x, y):
    return abs(x) + abs(y)


if __name__ == '__main__':
    # for i in range(25):
    #     x, y = random_walk_2(10)
    #     print(f'x = {x}, y = {y}, distance from home: {distance_from_home(x, y)}')

    number_of_walks = 50000
    for walk_length in range(1, 31):
        no_transport = 0
        for i in range(number_of_walks):
            x, y = random_walk(walk_length)
            dist = distance_from_home(x, y)
            if dist <= 5:
                no_transport += 1
        no_transport_percentage = float(no_transport)/number_of_walks
        print(f'walk_length: {walk_length}, no_transport_percentage: {no_transport_percentage}')
