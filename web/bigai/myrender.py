import gym
from gym.envs.classic_control import rendering
import math
from pyglet.gl import *
import pyglet

class Attr(object):
    def enable(self):
        raise NotImplementedError
    def disable(self):
        pass


class Color(Attr):
    def __init__(self, vec4):
        self.vec4 = vec4
    def enable(self):
        glColor4f(*self.vec4)
p
class Geom(object):
    def __init__(self):
        self._color=Color((0, 0, 0, 1.0))
        self.attrs = [self._color]
    def render(self):
        for attr in reversed(self.attrs):
            attr.enable()
        self.render1()
        for attr in self.attrs:
            attr.disable()
    def render1(self):
        raise NotImplementedError
    def add_attr(self, attr):
        self.attrs.append(attr)
    def set_color(self, r, g, b, alpha=1):
        self._color.vec4 = (r, g, b, alpha)


class FilledPolygon(Geom):
    def __init__(self, v):
        Geom.__init__(self)
        self.v = v
    def render1(self):
        if   len(self.v) == 4 : glBegin(GL_QUADS)
        elif len(self.v)  > 4 : glBegin(GL_POLYGON)
        else: glBegin(GL_TRIANGLES)
        for p in self.v:
            glVertex3f(p[0], p[1],0)  # draw each vertex
        glEnd()

        color = (self._color.vec4[0] * 0.5, self._color.vec4[1] * 0.5, self._color.vec4[2] * 0.5, self._color.vec4[3] * 0.5)
        glColor4f(*color)
        glBegin(GL_LINE_LOOP)
        for p in self.v:
            glVertex3f(p[0], p[1],0)  # draw each vertex
        glEnd()


class MyEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'videos.frames_per_second': 2
    }

    def __init__(self):
        self.viewer = rendering.Viewer(800, 600)

    # def render(self, mode='human', close=False):
    #     line1 = rendering.Line((100, 300), (500, 300))
    #     line2 = rendering.Line((100, 200), (500, 200))
    #     line1.set_color(0, 0, 0)
    #     line2.set_color(0, 0, 0)
    #     self.viewer.add_geom(line1)
    #     self.viewer.add_geom(line2)
    #     return self.viewer.render(return_rgb_array=mode == 'rgb_array')

    def make_agent(self):
        radius = 10
        res = 30
        WORLD_WIDTH = 10
        visual_distance = 100
        points = []
        for i in range(res):
            ang = 2*math.pi*i/res
            points.append([math.cos(ang)*radius, math.sin(ang)*radius])
        for i in range(9):
            ang = 2 * math.pi * (i - 4) / res
            points.append((math.cos(ang) * visual_distance + radius, math.sin(ang) * visual_distance))
        return points


    # def render(self, mode='human', close=False):
    #     circle = rendering.make_circle(30)
    #     circle_transform = rendering.Transform(translation=(100, 100))
    #     circle.add_attr(circle_transform)
    #     self.viewer.add_geom(circle)
    #     return self.viewer.render(return_rgb_array=mode == 'rgb_array')

    def render(self, mode='human'):
        agent_points = self.make_agent()
        agent = FilledPolygon(agent_points)
        trans = rendering.Transform(translation=(200, 200))
        agent.add_attr(trans)
        self.viewer.add_geom(agent)
        return self.viewer.render(return_rgb_array=mode == 'rgb_array')

if __name__ == '__main__':
    env = MyEnv()
    while True:
        env.render()
