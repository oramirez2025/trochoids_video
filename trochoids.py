from manimlib import *

class trochoids(Scene):
    def construct(self):
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        self.add(dot,dot2)