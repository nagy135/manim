from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle2 = Circle()
        square = Square()
        square2 = Square()

        square.flip(DL)
        square2.flip(LEFT)
        square.rotate(-3 * TAU / 8)
        square2.rotate(-1 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)
        circle2.set_fill(BLUE, opacity=0.9)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(Transform(square, circle2))
        self.play(FadeOut(square))
        self.play(Create(square2))
        self.play(Transform(square2, circle2))
        self.play(Transform(square2, circle))
        self.play(FadeOut(square2))
        self.play(FadeIn(square))
