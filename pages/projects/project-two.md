---
layout: default
title: Effective Viscosity in a Sheared Melt Layer (Thesis)
permalink: /projects/project-two/
---

<script>
  window.MathJax = { tex: { inlineMath: [['$', '$']] } };
</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
  .thesis-figure {
    margin: 1.5rem auto;
    max-width: 800px;
  }

  .thesis-figure img {
    display: block;
    width: 100%;
  }

  .thesis-figure img.thesis-animation {
    aspect-ratio: 800 / 310;
    object-fit: cover;
  }

  .thesis-figure figcaption {
    margin-top: 0.65rem;
    color: #606c71;
    font-size: 0.9rem;
    text-align: center;
  }
</style>

<article class="project-page" markdown="1">

# Effective Viscosity in a Sheared Melt Layer (Thesis)

What happens when ice melts above a layer of water that is heated **and** sheared from below? For my thesis, I used simulations to study this. Convection carves the melting boundary into a wavy landscape. That landscape then traps the convection, and the whole system starts to behave like a strange, history-dependent material, even though the water itself is an ordinary fluid.

## Setup

A two-dimensional liquid layer sits between a hot bottom wall moving at speed $U_w$ and a cold solid that is free to melt and refreeze. Buoyancy drives convection rolls, while the moving wall drags the fluid sideways. The balance between the two is set by the Richardson number

$$
Ri = \frac{Ra}{Pr\,Re_w^2},
$$

where the Rayleigh number $Ra$ measures thermal driving and the wall Reynolds number $Re_w = U_wH/\nu$ measures shear. The flow is simulated with a lattice Boltzmann method, and melting is handled with an enthalpy-based phase-change model.

<figure class="thesis-figure">
  <img class="thesis-animation" src="{{ '/assets/images/projects/thesis/melting.gif' | relative_url }}" alt="Animated temperature field of convection rolls beneath a melting interface">
  <figcaption>Temperature field $\theta$ beneath the melting interface (black line). Warm plumes carve troughs and cold downwellings leave crests.</figcaption>
</figure>

## Three regimes

Depending on how strong the shear is, the system settles into one of three states:

- **Pinned** (weak shear): the rolls deform the interface, and the corrugations lock the rolls in place. The mean flow almost vanishes.
- **Flowing** (moderate shear): the rolls break free and travel downstream beneath a nearly flat interface.
- **Suppressed** (strong shear): convection dies out and the flow becomes a plain linear shear profile.

<figure class="thesis-figure">
  <img src="{{ '/assets/images/projects/thesis/regimes.svg' | relative_url }}" alt="Temperature fields and mean velocity profiles for pinned, flowing and suppressed regimes">
  <figcaption>(a,d) Pinned, (b,e) flowing and (c,f) suppressed states. Left: temperature with the interface in black. Right: mean streamwise velocity, with the dashed line marking the layer average.</figcaption>
</figure>

## Unpinning and memory

When the wall speed is slowly increased, each warm plume is pushed further along under its crest until it slips past. At that point the lock fails, the rolls are swept away and the interface flattens.

<figure class="thesis-figure">
  <img src="{{ '/assets/images/projects/thesis/unpinning.svg' | relative_url }}" alt="Three temperature snapshots showing a plume slipping past an interface crest">
  <figcaption>(a) A roll locked beneath a crest, (b) the plume slips past the crest, (c) the rolls are advected and the interface flattens.</figcaption>
</figure>

Unpinning does not happen at the same point where pinning forms. A pinned state grown from rest forms only for $Ri \gtrsim 50$, but once established it survives down to $Ri \approx 5$. Ramping the shear back down follows a different path, so the interval $5 \lesssim Ri \lesssim 50$ is **hysteretic**. The interface also remembers which pattern it had: after re-pinning it keeps two large cells instead of the original four, which carry about 25% less convective heat.

<figure class="thesis-figure">
  <img src="{{ '/assets/images/projects/thesis/hysteresis.svg' | relative_url }}" alt="Hysteresis of interface shape, mean flow, melt height and heat transport between accelerating and decelerating ramps">
  <figcaption>Accelerating (solid) versus decelerating (dashed) ramps at $Ra=10^6$. (a) Interface height during deceleration. (b–e) Mean flow response, melt height, interface roughness and Nusselt number.</figcaption>
</figure>

## An effective material

Finally, the whole solid–liquid column is treated as one material, and its wall shear stress $\tau_w$ is measured against its mean deformation rate $\dot\gamma$. A Newtonian fluid would give a straight line. Instead there are two separate branches:

- **Pinned:** a large stress produces almost no flow, giving an apparent viscosity **60–150 times** the viscosity of the liquid itself.
- **Flowing:** after unpinning, the stress reverses sign, giving a small **negative** effective viscosity.

Reference runs show that the negative branch also appears in sheared convection without melting. The interface does not create it. Instead, it creates the stiff pinned state and acts as a history-dependent switch between the two branches.

<figure class="thesis-figure">
  <img src="{{ '/assets/images/projects/thesis/flow-curve.png' | relative_url }}" alt="Flow curves of wall shear stress against deformation rate showing a stiff pinned branch and a negative-stress flowing branch">
  <figcaption>Flow curves for several Stefan numbers on (a) accelerating and (b) decelerating ramps. Insets zoom in on the stiff pinned branch.</figcaption>
</figure>

[← Return to all projects]({{ '/#projects' | relative_url }})

</article>
