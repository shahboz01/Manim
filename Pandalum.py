from manim import *
from manim_physics import *
# use a SpaceScene to utilize all specific rigid-mechanics methods
class TwoObjectsFalling(SpaceScene):
    def construct(self):
        circle = Circle(radius=0.5).shift(UP)
        circle.set_fill(RED, 1)
        circle.shift(DOWN + RIGHT)
        circle1 = circle.copy().set_color(BLUE)
        circle1.shift(UP*2)

        text = Text("Manim Physics", color=GOLD, font_size=60)
        text1 = Text("EasyLearning", color=YELLOW_B, font_size=60)
        text2 = Text("Код в описание к видео", color=GREEN_B,
                     font_size=50,line_spacing=-1.5,slant=ITALIC)

        rect = Square().shift(UP)
        rect.rotate(PI / 4)
        rect.set_fill(YELLOW_A, 1)
        rect.shift(UP * 2)
        rect.scale(0.5)

        ground = Line([-4, -3.5, 0], [4, -3.5, 0])
        wall1 = Line([-4, -3.5, 0], [-4, 2, 0])
        wall2 = Line([4, -3.5, 0], [4, 2, 0])
        walls = VGroup(ground, wall1, wall2)
        self.add(walls)

        self.play(Write(text))
        self.wait()
        self.play(FadeOut(text))
        self.make_static_body(walls)  # фигуры будут стоять на месте
        #self.wait(3)
        self.play(Write(text1))
        self.make_rigid_body(text1)
        self.wait(2)
        self.play(
            DrawBorderThenFill(circle),
            DrawBorderThenFill(circle1),
            DrawBorderThenFill(rect)
        )
        self.wait(2)
        self.make_rigid_body(rect, circle, circle1)  # фигуры будут падать
        self.play(Write(text2))
        self.wait(2)
        self.make_rigid_body(text2)
        self.wait(2)
        Scene.clear(self)
        self.wait()
#--------------------------------------------------------------------
class TexFalling(SpaceScene):
    def construct(self):
        ground = Line(LEFT * 4, RIGHT * 4, color=ORANGE).shift(DOWN)
        self.add(ground)
        self.make_static_body(ground)
        forms = [
            r"e^{i\pi}+1=0",
            r"\cos(x+y)=\cos x \cos y - \sin x \sin y",
            r"\displaystyle \int_{-\infty }^{\infty }e^{-x^{2}}\,dx={\sqrt {\pi }}",
        ]
        cols = [GREEN_D, BLUE, YELLOW]
        for f, col in zip(forms, cols):
            text = MathTex(f, color=col)
            text.shift(UP*2)
            self.add(text)
            self.make_rigid_body(text[0])
            self.wait(3)
        Scene.clear(self)
        self.wait()
class ElectricFieldExample(Scene):
    def construct(self):
        charge1 = Charge(-1, LEFT + DOWN)
        charge2 = Charge(2, RIGHT + DOWN)
        charge3 = Charge(-1, UP)

        def rebuild(field):
            """Funkce která přestaví elektrické pole."""
            field.become(ElectricField(charge1, charge2, charge3))

        field = ElectricField(charge1, charge2, charge3)

        self.add(field, charge1, charge2, charge3)

        self.play(Write(field), FadeIn(charge1), FadeIn(charge2), FadeIn(charge3))

        field.add_updater(rebuild)

        self.play(
            charge1.animate.shift(LEFT),
            charge2.animate.shift(RIGHT),
            charge3.animate.shift(DOWN * 0.5),
            run_time=2,
        )
class PendulumExample(SpaceScene):
    def construct(self):
        pends = VGroup(*[Pendulum(i) for i in np.linspace(1,5,7)])
        self.add(pends)
        for p in pends:
            self.make_rigid_body(p.bobs)
            p.start_swinging()
        self.wait(10)
class AllScenes(SpaceScene):
    def construct(self):
        TwoObjectsFalling.construct(self)
        TexFalling.construct(self)
        ElectricFieldExample.construct(self)

        
