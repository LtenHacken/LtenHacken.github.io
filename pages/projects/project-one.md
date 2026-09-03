---
layout: default
title: Collective Motion with the Vicsek Model
permalink: /projects/project-one/
---

<script>
  window.MathJax = { tex: { inlineMath: [['$', '$']] } };
</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
  .vicsek-example {
    display: grid;
    grid-template-columns: minmax(240px, 0.8fr) repeat(2, minmax(220px, 1fr));
    gap: 1.5rem;
    align-items: start;
    margin: 1.5rem 0;
  }

  .vicsek-example figure {
    margin: 0;
  }

  .vicsek-example img {
    display: block;
    width: 100%;
  }

  .vicsek-example-label {
    margin: 0.5rem 0 0;
    text-align: center;
  }

  @media (max-width: 900px) {
    .vicsek-example {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .vicsek-example-text {
      grid-column: 1 / -1;
    }
  }
</style>

<article class="project-page" markdown="1">

# Collective Motion with the Vicsek Model

The Vicsek model is a minimal model of collective motion: self-propelled particles move at constant speed while aligning their direction with nearby particles. In this project, I use numerical simulations to explore how local interactions and angular noise produce large-scale ordered motion.

## Model

Particle $i$ has position $\mathbf{x}_i$ and heading $\theta_i$. Its neighbors are all particles within the interaction radius $R$, measured using periodic boundary conditions:

$$
\mathcal{N}_i(t) = \left\{j : \left|\mathbf{x}_j(t)-\mathbf{x}_i(t)\right|_{\mathrm{pbc}} \leq R\right\}.
$$

At each time step, every particle adopts the average heading of its neighbors plus independent angular noise $\xi_i$:

$$
\theta_i(t+1) = \arg\!\left(\sum_{j\in\mathcal{N}_i(t)} e^{\mathrm{i}\theta_j(t)}\right) + \xi_i(t),
\qquad
\xi_i \sim \mathcal{U}\!\left(-\frac{\eta}{2},\frac{\eta}{2}\right).
$$

The particles then move a fixed distance $v$ along their new headings:

$$
\mathbf{x}_i(t+1) = \mathbf{x}_i(t) + v
\begin{pmatrix}
\cos\theta_i(t+1) \\
\sin\theta_i(t+1)
\end{pmatrix}
\pmod L.
$$

Lengths and times are normalized by setting $R=1$ and $\Delta t=1$. Thus, $v$ is the distance traveled per update and $L$ is the box length in interaction-radius units.

## Examples

<div class="vicsek-example">
  <div class="vicsek-example-text" markdown="1">
The main parameters are particle number $N$, box size $L$, speed $v$, and noise width $\eta$. Together, $N$ and $L$ set the density $\rho=N/L^2$ and the typical number of interacting neighbors. The speed $v$ controls how far particles move between alignment updates. The noise $\eta$ sets the width of the random angular perturbation: small $\eta$ preserves alignment, while large $\eta$ disorders it.
  </div>
  <figure>
    <img src="{{ '/assets/images/projects/vicsek-disordered.gif' | relative_url }}" alt="Disordered Vicsek-model simulation at angular noise width 3.5">
    <p class="vicsek-example-label"><strong>Disordered, $\eta=3.5$</strong></p>
  </figure>
  <figure>
    <img src="{{ '/assets/images/projects/vicsek-ordered.gif' | relative_url }}" alt="Ordered Vicsek-model simulation at angular noise width 0.2">
    <p class="vicsek-example-label"><strong>Ordered, $\eta=0.2$</strong></p>
  </figure>
</div>

[← Return to all projects]({{ '/#projects' | relative_url }})

</article>
