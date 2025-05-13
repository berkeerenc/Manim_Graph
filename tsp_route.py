from manim import *

class TSPRoute(Scene):
    def construct(self):
        # Düğüm pozisyonları
        positions = {
            "a": LEFT * 4 + UP * 2,
            "b": LEFT * 1 + UP * 2,
            "c": RIGHT * 2 + UP * 2,
            "d": LEFT * 4,
            "e": ORIGIN,
            "f": RIGHT * 3,
            "g": RIGHT * 4 + DOWN * 2,
            "h": LEFT * 2 + DOWN * 2,
        }

        # Düğüm nesneleri
        node_mobs = {}
        for name, pos in positions.items():
            circle = Circle(radius=0.3, color=BLUE).move_to(pos)
            label = Text(name, font_size=24).move_to(pos)
            self.play(Create(circle), Write(label), run_time=0.3)
            node_mobs[name] = circle

        self.wait(0.5)

        # TSP yaklaşık tur rotası
        route = ["a", "b", "c", "b", "h", "b", "a", "d", "e", "f", "e", "g", "e", "a"]

        # Ok çizimi
        def draw_arrow(start, end):
            return Arrow(
                start=positions[start],
                end=positions[end],
                buff=0.4,
                color=RED,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.2
            )

        for i in range(len(route) - 1):
            start = route[i]
            end = route[i + 1]
            arrow = draw_arrow(start, end)
            self.play(Create(arrow), run_time=0.4)

        self.wait(2)
