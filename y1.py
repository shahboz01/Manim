import math
from manim import *
class T_labelExample(Scene):
    def construct(self):
        tex1 = MathTex("x^2 + (\\frac{5y}{4}-\\sqrt{\\abs{x}})^2 = 1")
        self.play(Write(tex1))
        self.wait()
        self.play(tex1.animate.shift(LEFT*5, UP).scale(0.5))
        graph = ImplicitFunction(
            lambda x, y: (x**2+(5*y/4-math.sqrt(math.fabs(x)))**2) - 1,
            color=RED
        )
        axes = Axes(x_range=[-3, 3], y_range=[-3, 3],
        x_length=6, y_length=6, tips=False,
        axis_config={"font_size": 24}).add_coordinates()
        self.add(axes)
        self.play(Create(graph), run_time=3)
        group = VGroup(axes, graph)
        self.play(group.animate.shift(LEFT*5, UP*3).scale(0.5))
        self.wait()

        tex2 = MathTex("r = \\sqrt{\\abs{cos(8t)}} - 2,4 + 0,6")
        self.play(Write(tex2))
        self.wait()
        self.play(tex2.animate.shift(LEFT*2, UP).scale(0.5))
        plane = Axes(x_range=[-3, 3], y_range=[-3, 3],
        x_length=6, y_length=6, tips=False,
        axis_config={"font_size": 24}).add_coordinates()
        graph1 = ParametricFunction(lambda t:
        plane.polar_to_point(np.sqrt(np.abs(np.cos(8*t)))-2.4+0.6, t), t_range=[0, 10], color=YELLOW)
        self.add(plane)
        self.wait()
        self.play(Create(graph1), run_time=7)
        group2 = VGroup(plane, graph1)
        self.play(group2.animate.shift(LEFT*2, UP*3).scale(0.5))
        self.wait()

        tex3 = MathTex("y^2 = x^2 - x^4")
        self.play(Write(tex3))
        self.wait()
        self.play(tex3.animate.shift(RIGHT, UP).scale(0.5))
        graph2 = ImplicitFunction(
            lambda x, y: y**2-x**2+x**4,
            color=GREEN
        )
        axes1 = Axes(x_range=[-3, 3], y_range=[-3, 3],
        x_length=6, y_length=6, tips=False,
        axis_config={"font_size": 24}).add_coordinates()
        self.add(axes1)
        self.play(Create(graph2), run_time=3)
        group1 = VGroup(axes1, graph2)
        self.play(group1.animate.shift(RIGHT, UP*3).scale(0.5))
        self.wait()

        tex9 = MathTex("r = sin(7t) + cos(7t) + sin(3t)")
        self.play(Write(tex9))
        self.wait()
        self.play(tex9.animate.shift(RIGHT*4, UP).scale(0.5))
        plane3 = Axes(x_range=[-3, 3], y_range=[-3, 3],
        x_length=6, y_length=6, tips=False,
        axis_config={"font_size": 24}).add_coordinates()
        graph3 = ParametricFunction(lambda t:
        plane3.polar_to_point(np.sin(7*t)+np.cos(7*t) + np.sin(3*t), t), t_range=[1, 10], color=BLUE_B)
        self.add(plane3)
        self.wait()
        self.play(Create(graph3), run_time=7)
        group3 = VGroup(plane3, graph3)
        self.play(group3.animate.shift(RIGHT*4, UP*3).scale(0.5))
        self.wait(2)


        text = Text("А вот вам такая задача,", color=YELLOW_B, font_size=26, slant=ITALIC)
        text1 = Text("""Составьте слово из графиков следующих функций
                        и напишите это слово в коментариях:)""", color=YELLOW_B, font_size=26, slant=ITALIC)
        self.play(Write(text))
        self.wait(3)
        self.remove(text)
        self.play(Write(text1))
        self.wait(4)

        tex4 = MathTex("y = \\frac{1}{x}", color=DARK_BROWN)
        self.play(FadeTransform(text1, tex4))
        self.play(tex4.animate.shift(LEFT*6))
        tex5 = MathTex("x^2 + y^2 = 9", color=DARK_BROWN)
        self.play(Write(tex5))
        self.play(tex5.animate.shift(LEFT*3.5))
        tex6 = MathTex("y = \\abs{-2x}", color=DARK_BROWN)
        self.play(Write(tex6))
        self.play(tex6.animate.shift(RIGHT*3.2))
        tex7 = MathTex("x = -3\\abs{sin(y)}", color=DARK_BROWN)
        self.play(Write(tex7))
        self.wait(2)
        t = Text("""Всем удачи!
                            До новых встреч.""", color=GREEN_B, font_size=30, slant=ITALIC).shift(DOWN*2)
        self.play(Write(t))
        self.wait(2)
        self.remove(t)
        self.wait(2)