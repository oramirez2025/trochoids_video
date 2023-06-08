from email import utils
from tkinter import Grid
from manimlib import *

class trochoids(Scene):
    def construct(self):
        #Frame 1
        #Create start and goal 
        start = Dot([-3, -2, 0])
        goal = Dot([3, 2, 0])
        svec = Arrow(start=[-3, -2, 0],end=[-3, -1.5, 0],buff=0,stroke_color="#000000")
        gvec = Arrow(start=[3, 2, 0],end=[3, 1.5, 0],buff=0,stroke_color="#000000")
        slabel = Tex("Start").next_to(start, LEFT)
        glabel = Tex("Goal").next_to(goal, RIGHT)
        slabel.set_color("#000000")
        glabel.set_color("#000000")
        start.set_color("#000000")
        goal.set_color("#000000")
        self.add(start,goal)
        self.wait()
        self.play(ShowCreation(svec),ShowCreation(gvec))
        self.wait()
        self.play(ShowCreation(slabel),ShowCreation(glabel))

        #Frame 2 
        self.play(Uncreate(svec),Uncreate(gvec))
        dubins = ArcBetweenPoints(start=start.get_center(), end=goal.get_center(), angle=-math.pi / 2, radius=0.5, stroke_color="#000000")
        self.play(ShowCreation(dubins))

        #Frame 3
        grid = NumberPlane(x_range=(-10, 10, 1), y_range=(-10, 10, 1),background_line_style={"stroke_width": 1,"stroke_opacity": 0.0})

        def wind_field(x, y):
            return np.array([5.0, 7.0, 0.0])  # Define the constant wind vector [vx, vy, vz]

        vector_field = VectorField(wind_field, coordinate_system=grid, opacity=0.5)
        self.play(Uncreate(slabel),Uncreate(glabel))
        self.play(ShowCreation(vector_field))

        #Frame 4
        moved = Dot([5, 1, 0])
        moved.set_color("#000000")
        new_dubins = ArcBetweenPoints(start=start.get_center(), end=moved.get_center(), angle=-math.pi / 2, radius=0.5, stroke_color="#000000")
        self.play(ShowCreation(new_dubins))
        self.play(ShowCreation(moved))
        self.wait()

        #Frame 5
        self.play(Uncreate(new_dubins))
        self.play(Uncreate(moved))
        self.play(Uncreate(dubins))
        self.wait()
        svec = Arrow(start=[-3, -2, 0],end=[-3, -1.5, 0],buff=0,stroke_color="#000000")
        gvec = Arrow(start=[3, 2, 0],end=[3, 1.5, 0],buff=0,stroke_color="#000000")
        self.wait()
        self.play(ShowCreation(svec),ShowCreation(gvec))

        #Frame 6 (Show rotation) 
        objs = VGroup(vector_field,start,goal,svec,gvec)
        self.play(Rotate(objs,-PI/4))

        #Frame 7 (Remove vector field)
        self.play(Uncreate(vector_field))
        #Draw mini graphs on to dots 
        sgrid = NumberPlane(x_range=(-1, 1, 1),y_range=(-1, 1, 1),background_line_style={"stroke_width": 1, "stroke_opacity": 0.0},)
        ggrid = NumberPlane(x_range=(-1, 1, 1),y_range=(-1, 1, 1),background_line_style={"stroke_width": 1, "stroke_opacity": 0.0},)

        sgrid.set_height(2)
        sgrid.set_width(2)
        sgrid.set_fill(WHITE, opacity=0.5)
        sgrid.set_stroke(BLACK, opacity=0.8, width=1)
        sgrid.move_to(start)
        sgrid.rotate(-PI/4)

        ggrid.set_height(2)
        ggrid.set_width(2)
        ggrid.set_fill(WHITE, opacity=0.5)
        ggrid.set_stroke(BLACK, opacity=0.8, width=1)
        ggrid.move_to(goal)
        ggrid.rotate(-PI/4)

        self.play(ShowCreation(sgrid), ShowCreation(ggrid))




