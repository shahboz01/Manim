from manim import *
class T_labelExample(Scene):
    def construct(self):
        t = Text("""Некоторые математические
                     функции и их графики""", color=GRAY_B, font_size=30, slant=ITALIC)
        self.play(Write(t))
        self.wait(2)

        plane2 = Axes(x_range=[-3, 3], y_range=[-3, 3],
        x_length=6, y_length=6, tips=False,
        axis_config={"font_size": 24}).add_coordinates()
        tex = MathTex("r = 1-sin(nt)", color=YELLOW_B)
        self.play(FadeTransform(t, tex))
        self.wait()
        self.play(tex.animate.shift(RIGHT*3, UP*3))
        self.wait()
        self.play(Create(plane2))
        for n in range(3, 10):
            var = Variable(n, Text("n"), color=BLUE).shift(RIGHT*3, UP*2)
            self.play(Write(var))
            self.wait()
            graph3 = ParametricFunction(lambda t1: plane2.polar_to_point(1-np.sin(n*t1), t1), t_range=[0, 10], color=BLUE)
            self.play(Create(graph3), run_time=3)
            self.remove(graph3, var)
            self.wait()
        self.wait()
        text = Text("Теперь смотрим на более сложные функции", color=GREEN_B, font_size=30, slant=ITALIC)
        self.play(FadeTransform(plane2, text))
        self.wait(3)
        self.remove(text, tex)
        self.wait(2)