
# ✨ Traveling Salesman Problem – Visual Explanation with Manim

This project is a visual and animated explanation of the **Traveling Salesman Problem (TSP)**, using [Manim](https://www.manim.community/) — a mathematical animation engine for Python.

> 🔍 It was developed as part of a discrete mathematics course assignment, but designed for a broader educational purpose.

---

## 📌 Problem Statement

A **Traveling Salesman** must visit a set of cities (nodes in a graph) exactly once and return to the starting city, minimizing the total travel cost.

The TSP is:
- **NP-Hard**, meaning no known polynomial-time algorithm can solve all instances.
- However, under **triangle inequality**, we can find an **approximate solution** within a guaranteed bound.

---

## 🎬 Animation Content

The explanation is broken into 5 animated scenes:

| Scene | Title                        | Description |
|-------|------------------------------|-------------|
| 1️⃣    | Problem Introduction         | TSP definition, triangle inequality, and the challenge |
| 2️⃣    | Graph Construction & MST     | Visualizing the weighted graph and its minimum spanning tree |
| 3️⃣    | BFS Traversal of MST         | Visiting all nodes using BFS (as approximation base) |
| 4️⃣    | Approximate TSP Tour         | A near-optimal cycle constructed by walking the MST |
| 5️⃣    | Theoretical Bound Conclusion | Explaining why `cost(P*) ≤ 2 · cost(T)` holds |

---

## 🧠 Key Concept

> If the distances satisfy **triangle inequality**,  
> then `cost(P*) ≤ 2 × cost(MST)`  
> where `P*` is the approximated tour path.

---

## 📂 Project Structure

```
📁 TSP_Manim_Project/
├── tsp_intro.py          # Scene 1
├── tsp_graph.py          # Scene 2
├── tsp_bfs.py            # Scene 3
├── tsp_route.py          # Scene 4
├── tsp_conclusion.py     # Scene 5
├── videos/
│   ├── TSPIntro.mp4
│   ├── TSPGraph.mp4
│   ├── TSPBFS.mp4
│   ├── TSPRoute.mp4
│   └── TSPConclusion.mp4
└── TSP_Full.mp4          # Combined full video (optional)
```

---

## ⚙️ Requirements

- Python 3.10+
- Manim Community Edition (`pip install manim`)
- ffmpeg (for combining videos if needed)
- LaTeX (MikTeX or TeXLive) for rendering math formulas

---

## 🚀 How to Run a Scene

Each scene is a standalone Manim script.

Example:
```bash
manim -pql tsp_intro.py TSPIntro
```

For all scenes:
```bash
manim -pql tsp_graph.py TSPGraph
manim -pql tsp_bfs.py TSPBFS
manim -pql tsp_route.py TSPRoute
manim -pql tsp_conclusion.py TSPConclusion
```

---

## 🔗 Optional: Combine All Videos

Using `ffmpeg`, create a `file_list.txt`:

```
file 'TSPIntro.mp4'
file 'TSPGraph.mp4'
file 'TSPBFS.mp4'
file 'TSPRoute.mp4'
file 'TSPConclusion.mp4'
```

Then run:
```bash
ffmpeg -f concat -safe 0 -i file_list.txt -c copy TSP_Full.mp4
```

---

## 📷 Preview

*(Optional: Add screenshots or GIFs from your rendered scenes here)*

---

## 🧑‍💻 Author

- 💡 **Berke Erenç**  
- 🏫 Akdeniz University – Computer Engineering  
- 🎓 Project for CSE 222 Discrete Mathematics II

---

## 📜 License

This project is open for educational use. Attribution is appreciated.
