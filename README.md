# Math Animations

This is a collection of mathematical animations built using [Manim](https://www.manim.community/), a Python software created and used by 3Blue1Brown. It focuses on visualizing abstract and complex mathematical concepts like:

- Gaussian integers and lattice geometry
- Euclidean domains and number theory
- Field extensions and algebraic structures

## 📽️ Preview

### Gaussian Integers as a Euclidean Domain

<div align="center">
  <img src="Algebraic%20Number%20Theory/media/GaussianLattice.gif" width="500" alt="Gaussian Integer Triangle Animation" />
</div>

The above is a shortened animation of the Gaussian integer lattice, showing that for every complex number *z*, there exists a Gaussian integer α in **ℤ[i]** that is "close enough" to *z*. The visual demonstrates how the lattice structure of **ℤ[i]** guarantees norm reduction, supporting its Euclidean domain property.

## 🚀 Getting Started

### Requirements

- Python 3.8+
- [Manim Community Edition](https://docs.manim.community/en/stable/installation.html)

### Installation

```bash
git clone https://github.com/santavalleytea/Math-Animations.git
cd Math-Animations
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
