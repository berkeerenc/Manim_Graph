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

