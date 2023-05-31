from distutils.command.config import config
from manimlib import *

class trochoids(Scene):
    def construct(self):
        dot = Dot([-3, -2, 0])
        dot2 = Dot([3, 2, 0])
        vec = Arrow(start=[-3, -2, 0],end=[-3, -1.5, 0],buff=0,stroke_color="#000000")
        vec2 = Arrow(start=[3, 2, 0],end=[3, 1.5, 0],buff=0,stroke_color="#000000")
        dot.set_color("#000000")
        dot2.set_color("#000000")
        self.add(dot,dot2)
        self.add(vec,vec2)
