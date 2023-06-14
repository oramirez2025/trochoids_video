from manimlib import *
import pandas as pd
import setuptools

class trochoids(Scene):
    def construct(self):
        data = pd.read_csv('data/Fig1_RAL_Dubins_CSV/LSR.csv')
        x_vals = data.iloc[:,0].tolist()
        y_vals = data.iloc[:,1].tolist()
        points = [np.array([x,y,0.0]) for (x,y) in zip(x_vals,y_vals)]
        dubins = VMobject()
        dubins.set_points(points)
        dubins.set_color("#3ea8f4")
        dubins.scale(0.1)
        #dubins.stretch(4,0)
        #dubins.stretch(0.01,1)

        data2 = pd.read_csv('data/Fig1_RAL_Trochoid_CSV/LSR.csv')
        x_vals2 = data2.iloc[:,0].tolist()
        y_vals2 = data2.iloc[:,1].tolist()
        points2 = [np.array([x,y,0.0]) for (x,y) in zip(x_vals2,y_vals2)]
        dubins2 = VMobject()
        dubins2.set_points(points2)
        dubins2.set_color("#ff8a24")
        dubins2.rotate(-PI/5.04,about_point=dubins2.get_points()[0])
        dubins2.scale(0.1)
        dubins2.shift([-11.258346,-16.2646337,0.0])
        dubins.rotate(PI/6,about_point=dubins2.get_points()[0])
        dubins2.rotate(PI/20.5,about_point=dubins2.get_points()[0])

        start = Dot().move_to(dubins.get_points()[0])
        start.set_color("#000000")
        start.set_stroke(width=1)
        slabel = Tex("Start").next_to(start, direction=np.array([-1., 1., 0.]), buff=0.25)
        slabel.set_color("#000000")
        slabel.scale(1.0)

        goal = Dot().move_to(dubins.get_points()[-1])
        goal.set_color("#000000")
        goal.set_stroke(width=1)
        glabel = Tex("Goal").next_to(goal, direction=np.array([-1., 1., 0.]), buff=0.25)
        glabel.set_color("#000000")
        glabel.scale(1.0)


        self.camera.frame.set_width(dubins.get_width()*4)
        
        self.camera.frame.move_to(dubins.get_center())
        self.camera.frame.set_z
        
        
        #Frame 1
        #Create start and goal 
        (x0,y0,z0) = dubins.get_points()[0]
        (x1,y1,z1) = dubins.get_points()[-1]

        svec = Arrow(start=[x0,y0,0],end=[x0+0.5,y0-0.40,0],buff=0,stroke_color="#000000",stroke_width=3)
        gvec = Arrow(start=[x1,y1,0],end=[x1+0.5,y1-0.2,0],buff=0,stroke_color="#000000",stroke_width=3)
        self.play(ShowCreation(start),ShowCreation(svec))
        self.play(ShowCreation(slabel))
        self.play(ShowCreation(goal), ShowCreation(gvec))
        self.play(ShowCreation(glabel))
        self.wait()
        self.play(ShowCreation(dubins))
        self.wait()
        
        #Frame 2
        grid = NumberPlane(x_range=(-15, 15, 1), y_range=(-15, 15, 1),background_line_style={"stroke_width": 0.5,"stroke_opacity": 0.0})

        def wind_field(x, y):
            return np.array([5.0, 2.0, 0.0])  # Define the constant wind vector [vx, vy, vz]

        vector_field = VectorField(wind_field, coordinate_system=grid, opacity=0.25,step_multiple=1,length_func=lambda norm: 2/norm)
        vector_field.move_to(dubins.get_center())
        vector_field.set_color("#7b8f92")
        vector_field.scale(1/80)
        vector_field.set_width(80)
        vector_field.set_height(80)
        self.play(ShowCreation(vector_field))

        #Frame 3
        moved = Dot().move_to(dubins2.get_points()[-1])
        moved.set_stroke(width=1)
        moved.set_color("#000000")
        mlabel = Tex("Moved","\\,","Goal").next_to(moved, UP, buff=0.3)
        mlabel.set_color("#000000")
        (x2,y2,z2) = dubins2.get_points()[-1]
        mvec = Arrow(start=[x2,y2,0.0],end=[x2+0.5,y2-0.2,0.0],buff=0,stroke_color="#000000",stroke_width=3)
        mvec.set_color("#000000")
        mlabel.scale(1.0)
        self.play(ShowCreation(moved),ShowCreation(mlabel),ShowCreation(mvec))
        self.play(ShowCreation(dubins2))
        self.wait()

        #Frame 4 (Show rotation) 
        self.play(Uncreate(dubins),Uncreate(slabel),Uncreate(glabel),Uncreate(mlabel),Uncreate(dubins2),Uncreate(gvec), Uncreate(goal))
        objs = VGroup(vector_field,start,goal,svec,gvec,mvec,moved,dubins)
        self.play(Rotate(objs,-PI/8))


        #Frame 5 (Remove vector field)
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
        ggrid.move_to(moved)
        ggrid.rotate(-PI/4)
        dotted_line = DashedLine(start, moved, dash_length=0.1, color=BLACK)
        (x2,y2,z2) = moved.get_center()
        dotted_line2 = DashedLine(moved,[x2+10,y2,0.0], dash_length=0.1, color=BLACK)
        arrow_line = Arrow([x2,y2,0.0],[x2-17,y2,0.0])
        arrow_line.set_color("#000000")
        dotr1 = Dot([x2-5,y2,0.0])
        dotr1.set_color("#fe801f")
        dotr2 = Dot([x2-8,y2,0.0])
        dotr2.set_color("#fe801f")
        dotr3 = Dot([x2-13,y2,0.0])
        dotr3.set_color("#fe801f")
        dotr4 = Dot([x2-14.5,y2,0.0])
        dotr4.set_color("#fe801f")

        #self.play(Uncreate(goal),Uncreate(gvec))
        self.play(ShowCreation(sgrid), ShowCreation(ggrid),ShowCreation(dotted_line))
        self.play(ShowCreation(arrow_line),ShowCreation(dotted_line2))
        self.play(ShowCreation(dotr1),ShowCreation(dotr2),ShowCreation(dotr3),ShowCreation(dotr4))