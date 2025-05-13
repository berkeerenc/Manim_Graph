from manim import *

class TSPConclusion(Scene):
    def construct(self):
        # Başlık
        title = Text("Conclusion", font_size=42).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Matematiksel eşitsizlik
        inequality = MathTex(
            r"cost(T) < cost(P^*) \leq 2 \cdot cost(T)", font_size=48
        )
        self.play(Write(inequality))
        self.wait(1)

        # Açıklama
        explanation = Text(
            "Each edge visited twice → path cost ≤ 2× tree cost", font_size=30
        ).next_to(inequality, DOWN, buff=0.6)
        self.play(Write(explanation))
        self.wait(2)
