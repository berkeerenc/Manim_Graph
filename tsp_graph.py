from manim import *

class TSPGraph(Scene):
    def construct(self):
        nodes = {
            "a": LEFT * 4 + UP * 2,
            "b": LEFT * 1 + UP * 2,
            "c": RIGHT * 2 + UP * 2,
            "d": LEFT * 4,
            "e": ORIGIN,
            "f": RIGHT * 3,
            "g": RIGHT * 4 + DOWN * 2,
            "h": LEFT * 2 + DOWN * 2,
        }

        node_mobs = {}

        for label, pos in nodes.items():
            circle = Circle(radius=0.3, color=BLUE).move_to(pos)
            text = Text(label, font_size=24).move_to(pos)
            self.play(Create(circle), Write(text), run_time=0.3)
            node_mobs[label] = circle

        self.wait(1)

        edges = [
            ("a", "b", 2),
            ("a", "d", 3),
            ("b", "c", 4),
            ("b", "e", 2),
            ("c", "f", 3),
            ("d", "e", 3),
            ("e", "f", 1),
            ("e", "g", 5),
            ("e", "h", 2),
            ("h", "g", 4)
        ]

        edge_lines = []

        for start, end, weight in edges:
            line = Line(nodes[start], nodes[end], color=GRAY)
            weight_text = Text(str(weight), font_size=20).move_to(
                (nodes[start] + nodes[end]) / 2 + UP * 0.3
            )
            self.play(Create(line), Write(weight_text), run_time=0.3)
            edge_lines.append(((start, end), line))

        self.wait(1)

        # MST kenarları
        mst_edges = [("e", "f"), ("b", "e"), ("e", "h"), ("a", "b"),
                     ("h", "g"), ("c", "f"), ("a", "d")]

        self.play(*[
            edge.animate.set_color(GREEN).set_stroke(width=6)
            for (start, end), edge in edge_lines
            if (start, end) in mst_edges or (end, start) in mst_edges
        ])

        self.wait(2)
