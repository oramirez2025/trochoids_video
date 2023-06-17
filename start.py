from manimlib import *
import pandas as pd
import setuptools

def ur_update_rect_rotation(rect, dotted_line):
    corners = rect.get_anchors()
    edges = [
        Line(corners[i], corners[(i + 1) % 4])
        for i in range(4)
    ]

    # Get the angle of an edge (e.g., bottom-left to top-right)
    edge = edges[2]
    angle = edge.get_angle()
    rect.rotate(dotted_line.get_angle() - angle, about_point=corners[2])

def ul_update_rect_rotation(rect, dotted_line):
    corners = rect.get_anchors()
    edges = [
        Line(corners[i], corners[(i + 1) % 4])
        for i in range(4)
    ]

    # Get the angle of an edge (e.g., bottom-left to top-right)
    edge = edges[2]
    angle = edge.get_angle()
    rect.rotate(dotted_line.get_angle() - angle, about_point=corners[3])

def ll_update_rect_rotation(rect, dotted_line):
    corners = rect.get_anchors()
    edges = [
        Line(corners[i], corners[(i + 1) % 4])
        for i in range(4)
    ]

    # Get the angle of an edge (e.g., bottom-left to top-right)
    edge = edges[2]
    angle = edge.get_angle()
    rect.rotate(dotted_line.get_angle() - angle, about_point=corners[0])

def lr_update_rect_rotation(rect, dotted_line):
    corners = rect.get_anchors()
    edges = [
        Line(corners[i], corners[(i + 1) % 4])
        for i in range(4)
    ]

    # Get the angle of an edge (e.g., bottom-left to top-right)
    edge = edges[2]
    angle = edge.get_angle()
    rect.rotate(dotted_line.get_angle() - angle, about_point=corners[1])

class trochoids(Scene):
    def construct(self):
        data = pd.read_csv('data/Fig1_RAL_Dubins_CSV/LSR.csv')
        x_vals = data.iloc[:,0].tolist()
        y_vals = data.iloc[:,1].tolist()
        points = [np.array([x,y,0.0]) for (x,y) in zip(x_vals,y_vals)]
        dubins = Line().set_points_smoothly(points).set_color("#3FA9F5")
        dubins.scale(0.1)
        dubins.z_index = 0

        data2 = pd.read_csv('data/Fig1_RAL_Trochoid_CSV/LSR.csv')
        x_vals2 = data2.iloc[:,0].tolist()
        y_vals2 = data2.iloc[:,1].tolist()
        points2 = [np.array([x,y,0.0]) for (x,y) in zip(x_vals2,y_vals2)]
        trochoid = Line().set_points_smoothly(points2).set_color("#3FA9F5")
        trochoid.rotate(-PI/5.04,about_point=trochoid.get_points()[0])
        trochoid.scale(0.1)
        trochoid.shift([-11.258346,-16.2646337,0.0])
        dubins.rotate(PI/6,about_point=trochoid.get_points()[0])
        trochoid.rotate(PI/20.5,about_point=trochoid.get_points()[0])

        data3 = pd.read_csv('data/Fig1_RAL_Trochoid_CSV/LSL.csv')
        x_vals3 = data3.iloc[:,0].tolist()
        y_vals3 = data3.iloc[:,1].tolist()
        points3 = [np.array([x,y,0.0]) for (x,y) in zip(x_vals3,y_vals3)]
        trochoid2 = Line().set_points_smoothly(points3).set_color("#7bc943")
        trochoid2.rotate(-PI/5.04,about_point=trochoid2.get_points()[0])
        trochoid2.scale(0.1)
        trochoid2.shift([-11.258346,-25.9470197,0.0])
        trochoid2.rotate(PI/20.5,about_point=trochoid2.get_points()[0])

        data4 = pd.read_csv('data/Fig1_RAL_Trochoid_CSV/RSL.csv') #RSR and RSL are the same graph? 
        x_vals4 = data4.iloc[:,0].tolist()
        y_vals4 = data4.iloc[:,1].tolist()
        points4 = [np.array([x,y,0.0]) for (x,y) in zip(x_vals4,y_vals4)]
        trochoid3 = Line().set_points_smoothly(points4).set_color("#ff1d25")
        trochoid3.rotate(-PI/5.04,about_point=trochoid3.get_points()[0])
        trochoid3.scale(0.1)
        trochoid3.shift([-11.107606,-17.1911637,0.0])
        trochoid3.rotate(PI/20.5,about_point=trochoid3.get_points()[0])
        trochoid3_temp = copy.deepcopy(trochoid3)

        data5 = pd.read_csv('data/Fig1_RAL_Trochoid_CSV/RSR.csv')
        x_vals5 = data5.iloc[:,0].tolist()
        y_vals5 = data5.iloc[:,1].tolist()
        points5 = [np.array([x,y,0.0]) for (x,y) in zip(x_vals5,y_vals5)]
        trochoid4 = Line().set_points_smoothly(points5).set_color("#ff931e") 
        trochoid4.rotate(-PI/5.04,about_point=trochoid4.get_points()[0])
        trochoid4.scale(0.1)
        trochoid4.shift([-(11.107606),-(7.3216472),0.0])
        trochoid4.rotate(PI/20.5,about_point=trochoid4.get_points()[0])

        start = Dot().move_to(dubins.get_points()[0])
        start.z_index = 5
        start.set_color("#000000")
        start.set_stroke(width=1)
        slabel = Tex("Start", color=BLACK)
        slabel.next_to(start, direction=np.array([-1., 1., 0.]), buff=0.25)
        slabel.scale(1.0)

        goal = Dot().move_to(dubins.get_points()[-1])
        goal.set_color("#000000")
        goal.z_index = 1
        goal.set_stroke(width=1)
        glabel = Tex("Goal", color=BLACK).next_to(goal, direction=np.array([-1., 1., 0.]), buff=0.25)
        glabel.scale(1.0)


        self.camera.frame.set_width(dubins.get_width()*4)
        
        self.camera.frame.move_to(dubins.get_center())
        self.camera.frame.set_z
        
        
        #Frame 1
        #Create start and goal 
        (x0,y0,z0) = dubins.get_points()[0]
        (x1,y1,z1) = dubins.get_points()[-1]

        svec = Arrow(start=[x0,y0,0],end=[x0+0.5,y0-0.28,0],buff=0,stroke_color="#000000",stroke_width=3)
        gvec = Arrow(start=[x1,y1,0],end=[x1+0.5,y1-0.15,0],buff=0,stroke_color="#000000",stroke_width=3)
        self.play(ShowCreation(start),ShowCreation(svec))
        self.play(Write(slabel))
        self.play(ShowCreation(goal), ShowCreation(gvec))
        self.play(Write(glabel))
        self.wait()
        self.play(ShowCreation(dubins))
        self.wait()
        
        #Frame 2
        grid = NumberPlane(x_range=(-5, 5, 1), y_range=(-5, 5, 1),background_line_style={"stroke_width": 0.3,"stroke_opacity": 0.0})

        def wind_field(x, y):
            return np.array([5.0, 2.0, 0.0])  # Define the constant wind vector [vx, vy, vz]

        vector_field = VectorField(wind_field, coordinate_system=grid, opacity=0.2,step_multiple=0.6,length_func=lambda norm: 2/norm)
        vector_field.move_to(dubins.get_center())
        vector_field.set_color("#7b8f92")
        # vector_field.scale(1/25)
        vector_field.set_width(40)
        vector_field.set_height(25)
        self.play(ShowCreation(vector_field))

        #Frame 3
        moved = Dot().move_to(trochoid.get_points()[-1])
        moved.set_stroke(width=1)
        moved.set_color("#000000")
        mlabel = Tex("Moved","\\,","Goal").next_to(moved, UP, buff=0.3)
        mlabel.set_color("#000000")
        (x2,y2,z2) = trochoid.get_points()[-1]
        mvec = Arrow(start=[x2,y2,0.0],end=[x2+0.5,y2-0.2,0.0],buff=0,stroke_color="#000000",stroke_width=3)
        mvec.set_color("#000000")
        mlabel.scale(1.0)
        self.play(TransformFromCopy(goal,moved, run_time=3),TransformFromCopy(gvec, mvec,run_time=3),Transform(dubins,trochoid,run_time=3), FadeOut(glabel)) # 
        self.play(self.camera.frame.animate.move_to(trochoid.get_center()), Uncreate(goal), Uncreate(gvec), run_time=2)
        self.play(ShowCreation(trochoid2))
        self.play(ShowCreation(trochoid4))
        self.play(ShowCreation(trochoid3))
        self.wait()

        #Frame 4 (Show rotation) 
        self.play(FadeOut(slabel),Uncreate(trochoid2),Uncreate(trochoid4),Uncreate(trochoid3),Uncreate(dubins))
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
        sgrid.rotate(0.246505956437)

        ur_background = Rectangle(
            width=sgrid.get_width()*.4,
            height=sgrid.get_height()*.4,
            fill_color='#7bc943',
            fill_opacity=0.15,
            stroke_width=0,  # Remove the border
        )
        ur_background_goal = ur_background.copy()
        ur_background.move_to(sgrid.get_center()+[sgrid.get_width()*.2,sgrid.get_height()*.2,0])
        ur_background.rotate(sgrid.get_axes()[0].get_angle(), about_point=ur_background.get_corner(DL))

        ul_background = Rectangle(
            width=sgrid.get_width()*.4,
            height=sgrid.get_height()*.4,
            fill_color='#ff931e',
            fill_opacity=0.15,
            stroke_width=0,  # Remove the border
        )
        ul_background_goal = ul_background.copy()
        ul_background.move_to(sgrid.get_center()+[-sgrid.get_width()*.2,sgrid.get_height()*.2,0])
        ul_background.rotate(sgrid.get_axes()[0].get_angle(), about_point=ul_background.get_corner(DR))

        ll_background = Rectangle(
            width=sgrid.get_width()*.4,
            height=sgrid.get_height()*.4,
            fill_color='#ff1d25',
            fill_opacity=0.15,
            stroke_width=0,  # Remove the border
        )
        ll_background_goal = ll_background.copy()
        ll_background.move_to(sgrid.get_center()+[-sgrid.get_width()*.2,-sgrid.get_height()*.2,0])
        ll_background.rotate(sgrid.get_axes()[0].get_angle(), about_point=ll_background.get_corner(UR))

        lr_background = Rectangle(
            width=sgrid.get_width()*.4,
            height=sgrid.get_height()*.4,
            fill_color='#3FA9F5',
            fill_opacity=0.15,
            stroke_width=0,  # Remove the border
        )
        lr_background_goal = lr_background.copy()
        lr_background.move_to(sgrid.get_center()+[sgrid.get_width()*.2,-sgrid.get_height()*.2,0])
        lr_background.rotate(sgrid.get_axes()[0].get_angle(), about_point=lr_background.get_corner(UL))



        ggrid.set_height(2).set_width(2).set_fill(WHITE, opacity=0.5)
        ggrid.set_stroke(BLACK, opacity=0.8, width=1).move_to(moved)
        ggrid.rotate(0.246505956437)

        dotted_line = DashedLine(start, moved, dash_length=0.1, color=BLACK)
        (x2,y2,z2) = moved.get_center()
        arrow_line = Arrow([x2+.4,y2,0.0],[x2-15,y2,0.0]).set_color(BLACK)
        start_line = Line([x2,y2-.25,0.0],[x2,y2+.25,0.0]).set_color(BLACK)

        dotted_line2 = DashedLine([x2,y2,0.0],[x2+2,y2,0.0], dash_length=0.1, color=BLACK)
        dotr1 = Dot([x2-7.41,y2,0.0]).set_color("#fe801f")
        dotr2 = Dot([x2-8.133,y2,0.0]).set_color("#fe801f")
        dotr3 = Dot([x2-(12.944),y2,0.0]).set_color("#fe801f")
        dotr4 = Dot([x2-13.667,y2,0.0]).set_color("#fe801f")

        ur_background_goal.move_to(ggrid.get_center()+[ggrid.get_width()*.2,ggrid.get_height()*.2,0])
        ur_background_goal_pivot = ur_background_goal.get_corner(DL)
        ur_background_goal.rotate(ggrid.get_axes()[0].get_angle(), about_point=ur_background_goal_pivot)
        
        ul_background_goal.move_to(ggrid.get_center()+[-ggrid.get_width()*.2,ggrid.get_height()*.2,0])
        ul_background_goal_pivot = ul_background_goal.get_corner(DR)
        ul_background_goal.rotate(ggrid.get_axes()[0].get_angle(), about_point=ul_background_goal_pivot)

        ll_background_goal.move_to(ggrid.get_center()+[-ggrid.get_width()*.2,-ggrid.get_height()*.2,0])
        ll_background_goal_pivot = ll_background_goal.get_corner(UR)
        ll_background_goal.rotate(ggrid.get_axes()[0].get_angle(), about_point=ll_background_goal_pivot)

        lr_background_goal.move_to(ggrid.get_center()+[ggrid.get_width()*.2,-ggrid.get_height()*.2,0])
        lr_background_goal_pivot = lr_background_goal.get_corner(UL)
        lr_background_goal.rotate(ggrid.get_axes()[0].get_angle(), about_point=lr_background_goal_pivot)
        
        
        self.play(ShowCreation(dotted_line2), ShowCreation(arrow_line), ShowCreation(start_line), run_time=3)
        self.wait()
        self.play(ShowCreation(dotted_line),run_time=2)
        self.wait()
        self.play(ShowCreation(sgrid), 
                    ShowCreation(ggrid),
                    ShowCreation(ur_background),
                    ShowCreation(ul_background),
                    ShowCreation(ll_background),
                    ShowCreation(lr_background),
                    ShowCreation(ur_background_goal),
                    ShowCreation(ul_background_goal),
                    ShowCreation(ll_background_goal),
                    ShowCreation(lr_background_goal), run_time=3)
        

        def update_rotation(number_plane):
            number_plane.rotate(dotted_line.get_angle() - number_plane.get_axes()[0].get_angle())

        goal_shift = dotr1.get_center() - ur_background_goal_pivot
        self.play(ggrid.animate.move_to(dotr1), 
                    ur_background_goal.animate.shift(goal_shift),
                    ul_background_goal.animate.shift(goal_shift),
                    ll_background_goal.animate.shift(goal_shift),
                    lr_background_goal.animate.shift(goal_shift),
                    UpdateFromFunc(ur_background, lambda obj: ur_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ul_background, lambda obj: ul_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ll_background, lambda obj: ll_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(lr_background, lambda obj: lr_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ur_background_goal, lambda obj: ur_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ul_background_goal, lambda obj: ul_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ll_background_goal, lambda obj: ll_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(lr_background_goal, lambda obj: lr_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ggrid, update_rotation),
                    UpdateFromFunc(sgrid,update_rotation), 
                    moved.animate.move_to(dotr1), 
                    mvec.animate.shift(dotr1.get_center() - mvec.get_start()),
                    Transform(dotted_line,DashedLine(start,dotr1,dash_length=0.1,color=BLACK)),
                    run_time=3)
        dotted_liner1 = DashedLine(start, dotr1, dash_length=0.1, color="#fe801f")
        self.play(ShowCreation(dotr1), ShowCreation(dotted_liner1))
        self.wait()

        a44_label = Tex("a_{44}", color=BLACK).set_color_by_tex("4", '#3FA9F5')
        a44_label.move_to((dotr1.get_center()+ur_background_goal_pivot)/2.0 + [0.0,0.5,0.0]) 
        self.play(Write(a44_label))

        goal_shift = dotr2.get_center() - dotr1.get_center()
        self.play(ggrid.animate.move_to(dotr2),
                    ur_background_goal.animate.shift(goal_shift),
                    ul_background_goal.animate.shift(goal_shift),
                    ll_background_goal.animate.shift(goal_shift),
                    lr_background_goal.animate.shift(goal_shift), 
                    UpdateFromFunc(ur_background, lambda obj: ur_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ul_background, lambda obj: ul_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ll_background, lambda obj: ll_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(lr_background, lambda obj: lr_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ur_background_goal, lambda obj: ur_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ul_background_goal, lambda obj: ul_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ll_background_goal, lambda obj: ll_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(lr_background_goal, lambda obj: lr_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ggrid, update_rotation),
                    UpdateFromFunc(sgrid,update_rotation), 
                    moved.animate.move_to(dotr2), 
                    mvec.animate.shift(dotr2.get_center() - mvec.get_start()),
                    Transform(dotted_line,DashedLine(start,dotr2,dash_length=0.1,color=BLACK)),
                    run_time=3)
        dotted_liner2 = DashedLine(start, dotr2, dash_length=0.1, color="#fe801f")
        self.play(ShowCreation(dotr2),ShowCreation(dotted_liner2))
        self.wait()

        a34_label = Tex("a_{34}", color=BLACK).set_color_by_tex("4", '#3FA9F5').set_color_by_tex("3", '#ff1d25')
        a34_label.move_to((dotr1.get_center()+dotr2.get_center())/2.0 + [0.0,0.5,0.0]) 
        self.play(Write(a34_label))

        goal_shift = dotr3.get_center() - dotr2.get_center()
        self.play(ggrid.animate.move_to(dotr3),
                    ur_background_goal.animate.shift(goal_shift),
                    ul_background_goal.animate.shift(goal_shift), 
                    ll_background_goal.animate.shift(goal_shift),
                    lr_background_goal.animate.shift(goal_shift),
                    UpdateFromFunc(ur_background, lambda obj: ur_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ul_background, lambda obj: ul_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ll_background, lambda obj: ll_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(lr_background, lambda obj: lr_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ur_background_goal, lambda obj: ur_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ul_background_goal, lambda obj: ul_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ll_background_goal, lambda obj: ll_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(lr_background_goal, lambda obj: lr_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ggrid, update_rotation),
                    UpdateFromFunc(sgrid,update_rotation), 
                    moved.animate.move_to(dotr3), 
                    mvec.animate.shift(dotr3.get_center() - mvec.get_start()),
                    Transform(dotted_line,DashedLine(start,dotr3,dash_length=0.1,color=BLACK)),
                    run_time=3)
        dotted_liner3 = DashedLine(start, dotr3, dash_length=0.1, color="#fe801f")
        self.play(ShowCreation(dotr3),ShowCreation(dotted_liner3))
        self.wait()

        a33_label = Tex("a_{33}", color=BLACK).set_color_by_tex("3", '#ff1d25')
        a33_label.move_to((dotr3.get_center()+dotr2.get_center())/2.0 + [0.0,0.5,0.0]) 
        self.play(Write(a33_label))

        goal_shift = dotr4.get_center() - dotr3.get_center()
        self.play(ggrid.animate.move_to(dotr4),
                    ur_background_goal.animate.shift(goal_shift),
                    ul_background_goal.animate.shift(goal_shift), 
                    ll_background_goal.animate.shift(goal_shift),
                    lr_background_goal.animate.shift(goal_shift),
                    UpdateFromFunc(ur_background, lambda obj: ur_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ul_background, lambda obj: ul_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ll_background, lambda obj: ll_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(lr_background, lambda obj: lr_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ur_background_goal, lambda obj: ur_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ul_background_goal, lambda obj: ul_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ll_background_goal, lambda obj: ll_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(lr_background_goal, lambda obj: lr_update_rect_rotation(obj, dotted_line)),
                    UpdateFromFunc(ggrid, update_rotation),
                    UpdateFromFunc(sgrid,update_rotation), 
                    moved.animate.move_to(dotr4), 
                    mvec.animate.shift(dotr4.get_center() - mvec.get_start()),
                    Transform(dotted_line,DashedLine(start,dotr4,dash_length=0.1,color=BLACK)),
                    run_time=3)
        dotted_liner4 = DashedLine(start, dotr4, dash_length=0.1, color="#fe801f")
        self.play(ShowCreation(dotr4), ShowCreation(dotted_liner4))
        self.wait()

        a23_label = Tex("a_{23}", color=BLACK).set_color_by_tex("3", '#ff1d25').set_color_by_tex("2", '#ff931e')
        a23_label.move_to((dotr3.get_center()+dotr4.get_center())/2.0 + [0.0,0.5,0.0]) 
        self.play(Write(a23_label)) 

        a22_label = Tex("a_{22}", color=BLACK).set_color_by_tex("2", '#ff931e')
        a22_label.move_to((arrow_line.get_end()+dotr4.get_center())/2.0 + [0.0,0.5,0.0]) 
        self.play(Write(a22_label))

        self.play(Uncreate(sgrid),Uncreate(ggrid),Uncreate(ul_background),Uncreate(ll_background),Uncreate(ur_background),
                  Uncreate(lr_background),Uncreate(ul_background_goal),Uncreate(ll_background_goal),Uncreate(ur_background_goal),
                  Uncreate(lr_background_goal),Uncreate(dotted_line))
        self.play(moved.animate.shift(-(dotr4.get_center() - ur_background_goal_pivot)),mvec.animate.shift(-(dotr4.get_center() - ur_background_goal_pivot)),run_time=5)
        trochoid3_temp.rotate(-PI/9,about_point=trochoid.get_points()[0])
        trochoid3_temp.scale(0.39)
        (xt,yt,zt) = start.get_center()
        (xt2,yt2,zt2) = trochoid3_temp.get_points()[0]
        trochoid3_temp.shift([xt-xt2,yt-yt2,0.0])
        trochoid3_temp.rotate(PI/8,about_point=trochoid3_temp.get_points()[0])
        goal_shift = dotr1.get_center() - ur_background_goal_pivot
        self.play(ShowCreation(trochoid3_temp),moved.animate.shift(goal_shift),mvec.animate.shift(goal_shift),run_time=2)