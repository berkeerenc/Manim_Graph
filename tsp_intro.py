from manim import *

class TSPIntro(Scene):
    def construct(self):
        # Başlık
        title = Text("Traveling Salesman Problem", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Tanım 1
        line1 = Text("A traveling salesman is supposed to visit a number of cities", font_size=28).next_to(title, DOWN, buff=0.7)
        line2 = Text("(nodes in a graph) and minimize the total travel length", font_size=28).next_to(line1, DOWN, aligned_edge=LEFT)
        self.play(Write(line1))
        self.play(Write(line2))
        self.wait(0.5)

        # Tanım 2 – NP-hard
        line3 = Text("This is NP-hard but can often be solved approximately.", font_size=28).next_to(line2, DOWN, buff=0.6)
        self.play(Write(line3))
        self.wait(0.5)

        # 🔺 Üçgen eşitsizliği metni
        line4 = Text("For graphs with triangle inequality:", font_size=28).next_to(line3, DOWN, buff=0.6)
        self.play(Write(line4))

        # 🔺 Üçgen eşitsizliği formülü
        triangle_eq = MathTex(r"d(u,v) + d(v,w) \ge d(u,w) \quad \forall u,v,w \in V", font_size=38)
        triangle_eq.next_to(line4, DOWN, buff=0.4)
        self.play(Write(triangle_eq))
        self.wait(1.5)

        # Son cümle
        line5 = Text("...we can construct an MST and traverse it using BFS.", font_size=28).next_to(triangle_eq, DOWN, buff=0.8)
        self.play(Write(line5))
        self.wait(2)
