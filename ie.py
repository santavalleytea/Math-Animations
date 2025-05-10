from manim import *

class TrigWaves(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-2.0, 2.0, 1],
            x_length=7,
            y_length=3,
            axis_config={"include_tip": False}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        sine = axes.plot(lambda x: np.sin(x), color=BLUE)
        cosine = axes.plot(lambda x: np.cos(x), color=RED)

        sine_label = axes.get_graph_label(sine, label="\\sin x", x_val=PI/2, direction=UP)
        cosine_label = axes.get_graph_label(cosine, label="\\cos x", x_val=0.5, direction=UP)

        self.play(Create(axes), Write(axes_labels))
        self.play(Create(sine), FadeIn(sine_label))
        self.wait(1)
        self.play(Create(cosine), FadeIn(cosine_label))
        self.wait(2)
