---
layout: default
title: Reconstructing Ocean Waves (Berkeley)
permalink: /projects/project-three/
---

<script>
  window.MathJax = { tex: { inlineMath: [['$', '$']] } };
</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
  .internship-figure {
    margin: 1.5rem auto;
    max-width: 800px;
  }

  .internship-figure.wide {
    max-width: 1100px;
  }

  .internship-figure.narrow {
    max-width: 520px;
  }

  .internship-figure img,
  .internship-figure video {
    display: block;
    width: 100%;
  }

  .internship-figure figcaption {
    margin-top: 0.65rem;
    color: #606c71;
    font-size: 0.9rem;
    text-align: center;
  }
</style>

<article class="project-page" markdown="1">

# Reconstructing Ocean Waves (Berkeley)

Can you reconstruct a whole kilometre of ocean surface, crest by crest, from just a handful of wave probes? During my research internship at UC Berkeley, I built a fast method that does this. It combines a simple wave model with an Ensemble Kalman Filter and runs more than 150 times faster than real time on a single CPU core.

## The problem

Wave-energy converters, ships and offshore platforms all benefit from knowing the exact shape of the waves heading their way. Such a *phase-resolved* estimate needs the surface elevation $\eta(x,t)$ at $N \sim 10^2$–$10^3$ grid points. In practice, a few buoys or unmanned surface vehicles only provide $P \sim O(1)$ point measurements. Interpolating between them is hopeless. The missing information has to come from the physics of how waves travel.

## Method

The method keeps an ensemble of $N_e \approx 100$ guesses of the wave field and repeats two steps.

**Forecast.** Each guess is propagated with linear wave theory. In Fourier space, every mode simply rotates in phase,

$$
\hat\eta_n(t+\Delta t) = \hat\eta_n(t)\, e^{-\mathrm{i}\omega_n \Delta t},
\qquad
\omega_n = \sqrt{g|k_n|} + \tfrac{1}{2}k_n u_s,
$$

where the second term corrects the dispersion relation for the Stokes drift $u_s$ of the waves themselves.

**Analysis.** When the probes report new measurements $\mathbf y$, each guess is nudged toward them using the Kalman gain $\mathbf K$, which is built from the spread of the ensemble:

$$
\mathbf x^{(i)} \leftarrow \mathbf x^{(i)} + \mathbf K\left(\mathbf y + \boldsymbol\nu^{(i)} - \mathbf H\mathbf x^{(i)}\right).
$$

The correlations inside the ensemble spread the correction at a few probes across the whole domain. Covariance localization, adaptive inflation and spectral filtering keep the filter stable. The nonlinear "true" ocean is simulated separately with the HOS-Ocean solver.

## Reconstruction

Starting from pure noise, the ensemble locks onto the true surface within a few wave periods, using only two probes.

<figure class="internship-figure wide">
  <video src="{{ '/assets/images/projects/internship/reconstruction.mp4' | relative_url }}?v=1" autoplay muted loop playsinline aria-label="Animated reconstruction of the wave surface converging to the reference surface over 40 peak periods"></video>
  <figcaption>Reference (black) and reconstructed (red) surfaces from $t = 0$ to $40\,T_p$ in a periodic domain of $10\lambda_p \approx 1$ km with two probes (blue).</figcaption>
</figure>

With four probes, the late-time error is 2–7.5% of the significant wave height $H_s$. It grows with wave steepness $\varepsilon$, because the linear forecast cannot represent nonlinear wave interactions. That model bias, not the sensors or the filter, sets the error floor. The Stokes-drift correction reduces the error by about 26% at the highest steepness.

<figure class="internship-figure narrow">
  <img src="{{ '/assets/images/projects/internship/steepness.png' | relative_url }}" alt="Normalized reconstruction error decreasing over time for three wave steepnesses">
  <figcaption>Normalized MAE (top) and RMSE (bottom) over time for three steepnesses. Shaded bands show the spread over 18 runs.</figcaption>
</figure>

## Moving probes and the open ocean

Probes mounted on vehicles move, and the direction matters. Probes moving **against** the waves meet new crests often and keep the error low. Probes moving **with** the waves at speeds near the wave group velocity see the same crests for longer, so less new information reaches the filter and the error grows. In mixed fleets, a single counter-moving probe is enough to keep the reconstruction accurate.

<figure class="internship-figure">
  <img src="{{ '/assets/images/projects/internship/moving-probes.svg' | relative_url }}" alt="Reconstruction error for probes moving against (top) and with (bottom) the waves at three speeds">
  <figcaption>Error for probes moving against (top) and with (bottom) the waves, at 0.5, 1 and 2 times the peak group velocity. Shaded bands show the spread over 18 runs.</figcaption>
</figure>

Finally, the method was tested in an open domain where waves are generated at one end and absorbed at both ends, so the sea never repeats. It performs just as well there: the late-time error is 6.4% of $H_s$ at the highest steepness, and it runs at about 156 times real time.

<figure class="internship-figure">
  <img src="{{ '/assets/images/projects/internship/open-domain.svg' | relative_url }}" alt="Reconstruction in an open-boundary domain with generation and absorption zones">
  <figcaption>Reconstruction in the open-boundary domain. The generation (blue) and absorption (red) zones are excluded from the error.</figcaption>
</figure>

[← Return to all projects]({{ '/#projects' | relative_url }})

</article>
