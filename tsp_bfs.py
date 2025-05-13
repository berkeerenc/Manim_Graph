from manim import *

class TSPBFS(Scene):
    def construct(self):
        # Düğüm konumları
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

        # BFS geçiş sırası (örnek rota)
        bfs_path = ["a", "b", "e", "f", "h", "g", "c", "d"]

        # Kenarları tutacağımız yapı (çizim + ok opsiyonu)
        def draw_edge(start, end):
            line = Line(positions[start], positions[end], color=RED, stroke_width=4)
            return line

        # Ziyaret animasyonu
        for i in range(len(bfs_path) - 1):
            start = bfs_path[i]
            end = bfs_path[i + 1]
            edge = draw_edge(start, end)
            self.play(Create(edge), run_time=0.5)
            self.play(node_mobs[end].animate.set_fill(RED), run_time=0.2)

        self.wait(2)
