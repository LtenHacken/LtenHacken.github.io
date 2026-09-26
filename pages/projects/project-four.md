---
layout: default
title: Sheared Melt Experiment (Tsinghua)
permalink: /projects/project-four/
---

<script>
  window.MathJax = { tex: { inlineMath: [['$', '$']] } };
</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
  .experiment-figure {
    margin: 1.5rem auto;
    max-width: 800px;
  }

  .experiment-figure img,
  .experiment-figure video {
    display: block;
    width: 100%;
  }

  .experiment-figure figcaption {
    margin-top: 0.65rem;
    color: #606c71;
    font-size: 0.9rem;
    text-align: center;
  }

  .experiment-pair {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.5rem;
    align-items: start;
  }

  .experiment-pair.media {
    max-width: 1000px;
    margin: 0 auto;
  }

  .experiment-pair figure {
    margin: 0;
    min-width: 0;
  }

  .experiment-pair img,
  .experiment-pair video {
    display: block;
    width: 100%;
    height: auto;
  }

  .experiment-pair video {
    aspect-ratio: 366 / 404;
    object-fit: cover;
  }

  .experiment-label {
    margin: 0.5rem 0 0;
    text-align: center;
  }

  @media (max-width: 600px) {
    .experiment-pair {
      gap: 0.75rem;
    }
  }
</style>

<article class="project-page" markdown="1">

# Sheared Melt Experiment (Tsinghua)

My [thesis simulations]({{ '/projects/project-two/' | relative_url }}) showed that convection rolls can lock themselves beneath a melting interface. Does the same happen with real ice and water? To find out, I designed and built a rotating ice–water cell. I also ran a 3D "numerical twin" of it and compared the two.

## Setup

Water fills the gap between two concentric cylinders, 90 mm and 180 mm across and 180 mm tall. The bottom plate is kept at $-3\,^\circ$C, so ice grows upward from it. The top plate is kept at $+2\,^\circ$C. Water is densest near $4\,^\circ$C, so this upside-down arrangement still leaves an unstable, convecting layer above the ice. Shear comes from rotating the bottom plate and sidewalls on a turntable while the top plate stays still. A side camera films the interface through the transparent outer wall.

<div class="experiment-pair">
  <figure>
    <img src="{{ '/assets/images/projects/thesis_experiment/setup-schematic.png' | relative_url }}" alt="Schematic of the rotating cell with temperature-controlled plates, camera and illumination">
    <p class="experiment-label"><strong>Schematic</strong></p>
  </figure>
  <figure>
    <img src="{{ '/assets/images/projects/thesis_experiment/setup-photo.jpg' | relative_url }}" alt="Photograph of the insulated experimental apparatus on its rotating table">
    <p class="experiment-label"><strong>Realised apparatus</strong></p>
  </figure>
</div>

## Experiment and numerical twin

Each run lasted at least 48 hours, until the ice level became steady, at two rotation rates: 0.1 and 1 rpm. With $Ra \approx 2.3\times10^7$, these correspond to Richardson numbers of $Ri \approx 305$ and $Ri \approx 3$, two decades apart. The twin reproduces the annular geometry and the relative wall motion in a lattice Boltzmann simulation with the real properties of water and ice. It does not include the Coriolis force of the rotating frame.

<div class="experiment-pair media">
  <figure>
    <video src="{{ '/assets/images/projects/thesis_experiment/experiment.mp4' | relative_url }}?v=2" autoplay muted loop playsinline aria-label="Camera footage of ice growing at the bottom of the rotating annular cell"></video>
    <p class="experiment-label"><strong>Experiment</strong></p>
  </figure>
  <figure>
    <video src="{{ '/assets/images/projects/thesis_experiment/simulation.mp4' | relative_url }}?v=3" autoplay muted loop playsinline aria-label="Simulated temperature and flow arrows in the annular numerical twin"></video>
    <p class="experiment-label"><strong>Numerical twin</strong></p>
  </figure>
</div>

## Measured ice interface

After the final state was reached, the cell was spun once at 10 rpm while filming. Each frame then shows a different angle, so edge detection gives the full ice height $h(\varphi)$ around the annulus. Both rotation rates show a single crest and trough per revolution, which matches what the narrow geometry predicts. At 1 rpm the ice is **thicker and smoother**: the mean height rises from 0.108 to 0.148, and the roughness drops by about 40%.

<figure class="experiment-figure">
  <img src="{{ '/assets/images/projects/thesis_experiment/interface-profiles.svg' | relative_url }}" alt="Measured ice height around the annulus at 0.1 and 1 rpm">
  <figcaption>Ice height $h/H$ around the annulus at 0.1 and 1 rpm. Dotted lines mark the mean height and dashed lines the extrema.</figcaption>
</figure>

## Comparison and lessons

The twin disagrees in an informative way. It ends up with **thinner** ice at 1 rpm and no crest per revolution. Instead, the rotating lid drives a radial secondary circulation that carries warm water down at the outer wall. In the real, rotating experiment, the Coriolis force is expected to reverse this circulation. That is a candidate explanation for the opposite trend, and a clear test for future work.

<figure class="experiment-figure">
  <img src="{{ '/assets/images/projects/thesis_experiment/twin-interface.svg' | relative_url }}" alt="Interface height maps, time evolution and azimuthal and radial profiles from the numerical twin">
  <figcaption>Numerical twin at 0.1 and 1 rpm. (a,b) Interface height maps. (c) Mean height over time. (d,e) Azimuthal and radial profiles.</figcaption>
</figure>

The experiment was a first attempt, and it taught me what a decisive test needs. The main problems were imperfect insulation from the room and the fact that the flow itself could not be measured. Future versions need better thermal isolation, repeat runs under matched room conditions, velocity measurements (PIV or PTV), and a Coriolis force in the twin.

[← Return to all projects]({{ '/#projects' | relative_url }})

</article>
