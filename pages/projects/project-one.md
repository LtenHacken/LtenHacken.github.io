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

  .vicsek-statistics-plot {
    margin: 1.5rem auto;
    max-width: 800px;
  }

  .vicsek-statistics-plot img {
    display: block;
    width: 100%;
  }

  .vicsek-statistics-plot figcaption {
    margin-top: 0.65rem;
    color: #606c71;
    font-size: 0.9rem;
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
    <img src="{{ '/assets/images/projects/vicsek/vicsek-disordered.gif' | relative_url }}" alt="Disordered Vicsek-model simulation at angular noise width 3.5">
    <p class="vicsek-example-label"><strong>Disordered, $\eta=3.5$</strong></p>
  </figure>
  <figure>
    <img src="{{ '/assets/images/projects/vicsek/vicsek-ordered.gif' | relative_url }}" alt="Ordered Vicsek-model simulation at angular noise width 0.2">
    <p class="vicsek-example-label"><strong>Ordered, $\eta=0.2$</strong></p>
  </figure>
</div>

## Statistics

A natural measure of collective order is the **polarity**, or normalized average velocity,

$$
\Phi(t)=\frac{1}{Nv}\left|\sum_{i=1}^{N}\mathbf{v}_i(t)\right|
=\frac{1}{N}\left|\sum_{i=1}^{N}e^{\mathrm{i}\theta_i(t)}\right|.
$$

It ranges from $0$ for particles moving in unrelated directions to $1$ when every particle moves in the same direction. At low noise, local alignment spreads through the system and the polarity grows toward an ordered state. At high noise, the headings remain incoherent and the polarity stays close to zero.

<figure class="vicsek-statistics-plot">
  <img src="{{ '/assets/images/projects/vicsek/vicsek-polarity.svg' | relative_url }}" alt="Polarity over 400 time steps for ordered and disordered Vicsek-model simulations">
  <figcaption>One realization for each noise level, using the same initial condition with N = 400, L = 15, R = 1, and v = 0.03.</figcaption>
</figure>

The polarity also distinguishes the two phases of the model. In the **ordered phase** at low noise, alignment dominates the random perturbations and $\Phi$ remains close to one. In the **disordered phase** at high noise, the perturbations overwhelm local alignment, headings become nearly random, and $\Phi$ approaches zero.

To see the change between these regimes, the noise width $\eta$ is swept from $0$ to $2\pi$. For each value, three independent simulations run for 600 steps. The polarity is averaged over the final 300 steps of each run and then across the three simulations. The decline is smooth because this is a finite system; a sharp phase transition is defined in the large-system limit.

<figure class="vicsek-statistics-plot">
  <img src="{{ '/assets/images/projects/vicsek/vicsek-noise-sweep.svg' | relative_url }}" alt="Steady-state Vicsek-model polarity decreasing as angular noise increases from zero to two pi">
  <figcaption>Average of three simulations at each noise level, using N = 400, L = 15, R = 1, and v = 0.03.</figcaption>
</figure>

[← Return to all projects]({{ '/#projects' | relative_url }})

</article>
