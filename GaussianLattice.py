from manim import *

class GaussianLattice(MovingCameraScene):
    def construct(self):
        axes = Axes (
            # [start, end (exclusive), step (spacing)]
            x_range=[-5,6,1],
            y_range=[-5,6,1],
            x_length=7,
            y_length=7,
            axis_config={"include_numbers": True}
        )

        re_text = Text("Re").scale(0.5)
        im_text = Text("Im").scale(0.5)

        re_label = re_text.next_to(axes.x_axis.get_end(), RIGHT)
        im_label = im_text.next_to(axes.y_axis.get_end(), UP)

        self.play(Create(axes), Write(re_label), Write(im_label))
        self.wait(1)

        # Group dots to animate all at once
        dots = VGroup()

        for a in range(-5,6):
            for b in range(-5,6):
                # c2p converts (a,b) to the pixel space
                dot = Dot(point=axes.c2p(a,b), radius=0.05, color=WHITE)
                dots.add(dot)
        
        self.play(FadeIn(dots, lag_ratio=0.01))
        self.wait(2)

        vector = Arrow (
            start=axes.c2p(0,0),
            end=axes.c2p(3,2),
            buff=0,
            color = YELLOW
        )

        label = MathTex("3+2i").next_to(vector.get_end(), RIGHT + UP)

        self.play(GrowArrow(vector), Write(label))
        self.wait(2)
        self.play(FadeOut(vector), FadeOut(label))
        self.wait(1)

        frame = self.camera.frame
        self.play(frame.animate.set(width=2.5).move_to(axes.c2p(3.5,3.5)))
        self.wait(1)

    #circles = VGroup()
    #    for a in range(-5,6):
    #        for b in range(-5,6):
    #            center = axes.c2p(a,b)
    #            circle = Circle(radius=0.707, color=WHITE, stroke_opacity=0.4).move_to(center)
    #            circles.add(circle)
    #    
    #    self.play(FadeIn(circles, lag_ratio=0.02))
    #    self.wait(2)
    
        zdot = Dot(point=axes.c2p(3.5, 3.5), radius=0.05, color=YELLOW)
        alpha_dot = Dot(axes.c2p(4,4), radius=0.05, color=WHITE)
        z_char = MathTex(r"z").scale(0.3)
        z_label = z_char.next_to(zdot, DOWN + RIGHT, buff=0.05)
        self.play(FadeIn(zdot, lag_ratio=0.01), Write(z_label))

        alpha = MathTex(r"\alpha").scale(0.3)
        alpha_label = alpha.next_to(alpha_dot, UP + RIGHT, buff=0.05)
        self.play(Write(alpha_label))
        self.wait(1)

        bottom_left = axes.c2p(3,3)
        bottom_right = axes.c2p(4,3)
        top_right = axes.c2p(4,4)

        leg1 = Line(bottom_left, bottom_right, color=WHITE)
        leg2 = Line(bottom_right, top_right)
        hypotenus = Line(bottom_left, top_right, color=RED)

        triangle = VGroup(leg1, leg2, hypotenus)

        self.play(Create(triangle))
        self.wait(1)

        hyp_label = MathTex(r"\sqrt{2}").scale(0.3).move_to(hypotenus.get_center() + 0.2 * (UP + LEFT))
        leg1_label = MathTex("1").scale(0.3).next_to(leg1, DOWN, buff=0.1)

        self.play(Write(hyp_label), Write(leg1_label))
        self.wait(1)










