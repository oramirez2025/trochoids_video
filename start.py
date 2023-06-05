from email import utils
from manimlib import *

class trochoids(Scene):
    def construct(self):
        dot = Dot([-3, -2, 0])
        dot2 = Dot([3, 2, 0])
        vec = Arrow(start=[-3, -2, 0],end=[-3, -1.5, 0],buff=0,stroke_color="#000000")
        vec2 = Arrow(start=[3, 2, 0],end=[3, 1.5, 0],buff=0,stroke_color="#000000")
        label = Tex("Start").next_to(dot, LEFT)
        label2 = Tex("Goal").next_to(dot2, RIGHT)
        label.set_color("#000000")
        label2.set_color("#000000")
        dot.set_color("#000000")
        dot2.set_color("#000000")
        self.add(dot,dot2)
        self.wait()
        self.play(ShowCreation(vec),ShowCreation(vec2))
        self.wait()
        self.play(ShowCreation(label),ShowCreation(label2))
        self.play(Uncreate(vec),Uncreate(vec2))

        dubins = ArcBetweenPoints(start=dot.get_center(), end=dot2.get_center(), angle=-math.pi / 2, radius=0.5, stroke_color="#000000")
        self.play(ShowCreation(dubins))
        grid = NumberPlane(x_range=(-10, 10, 1), y_range=(-10, 10, 1),background_line_style={"stroke_width": 1,"stroke_opacity": 0.0})

        def wind_field(x, y):
            return np.array([5.0, 7.0, 0.0])  # Define the constant wind vector [vx, vy, vz]

        vector_field = VectorField(wind_field, coordinate_system=grid)
        self.play(Uncreate(label),Uncreate(label2),)
        self.play(ShowCreation(vector_field))

        dot3 = Dot([5, 1, 0])
        new_dubins = ArcBetweenPoints(start=dot.get_center(), end=dot3.get_center(), angle=-math.pi / 2, radius=0.5, stroke_color="#000000")
        self.play(ReplacementTransform(dubins,new_dubins))


