
import random


class Location(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        return Location(self.x + dx, self.y + dy)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def euclidean_distance_from(self, other):
        x_dist = self.x - other.get_x()
        y_dist = self.y - other.get_y()
        return (x_dist ** 2 + y_dist **2)**0.5

    def manhattan_distance_from(self, other):
        x_dist = self.x - other.get_x()
        y_dist = self.y - other.get_y()
        return abs(x_dist) + abs(y_dist)

    def __str__(self):
        return f'<{self.x}, {self.y}>'


class Drunk(object):
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        if self.name is not None:
            return self.name
        return 'Anonymous'


def usual_take_step():
    return random.choice([[-1, 0], [1, 0], [0, -1], [0, 1]])


def north_take_step():
    step_choices = [(0.0, 1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)]
    return random.choice(step_choices)


