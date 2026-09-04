"""Generate the polarity comparison shown on the Vicsek project page."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import cKDTree


PARTICLES = 400
BOX_SIZE = 15.0
INTERACTION_RADIUS = 1.0
SPEED = 0.03
STEPS = 400
SEED = 8
SWEEP_STEPS = 600
SAMPLE_STEPS = 300
REALIZATIONS = 3


def simulate(
    noise_width: float,
    positions: np.ndarray,
    headings: np.ndarray,
    steps: int = STEPS,
    seed_offset: int = 0,
) -> np.ndarray:
    """Return the normalized mean velocity for one Vicsek-model run."""
    # Reuse the same random-number stream across noise levels during a sweep.
    # Scaling identical draws by eta reduces sampling noise in the comparison.
    rng = np.random.default_rng(SEED + seed_offset)
    positions = positions.copy()
    headings = headings.copy()
    polarity = np.empty(steps + 1)

    for step in range(steps + 1):
        polarity[step] = np.hypot(np.cos(headings).mean(), np.sin(headings).mean())
        if step == steps:
            break

        neighbours = cKDTree(positions, boxsize=BOX_SIZE).query_ball_point(
            positions, INTERACTION_RADIUS
        )
        mean_heading = np.array(
            [
                np.arctan2(np.sin(headings[index]).sum(), np.cos(headings[index]).sum())
                for index in neighbours
            ]
        )
        headings = mean_heading + rng.uniform(-noise_width / 2, noise_width / 2, PARTICLES)
        positions = (positions + SPEED * np.column_stack((np.cos(headings), np.sin(headings)))) % BOX_SIZE

    return polarity


def main() -> None:
    initial_rng = np.random.default_rng(SEED)
    positions = initial_rng.uniform(0, BOX_SIZE, size=(PARTICLES, 2))
    headings = initial_rng.uniform(-np.pi, np.pi, size=PARTICLES)

    ordered = simulate(0.2, positions, headings)
    disordered = simulate(3.5, positions, headings)

    plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
    figure, axis = plt.subplots(figsize=(8, 4.6))
    time = np.arange(STEPS + 1)
    axis.plot(time, ordered, color="#1565c0", linewidth=2.2, label=r"Ordered, $\eta=0.2$")
    axis.plot(time, disordered, color="#d95f40", linewidth=2.0, label=r"Disordered, $\eta=3.5$")
    axis.set(xlabel="Time step", ylabel=r"Polarity $\Phi$", xlim=(0, STEPS), ylim=(0, 1.02))
    axis.grid(alpha=0.2)
    axis.legend(frameon=False, loc="center right")
    figure.tight_layout()

    destination = Path(__file__).resolve().parents[1] / "assets/images/projects/vicsek/vicsek-polarity.svg"
    figure.savefig(destination, format="svg", metadata={"Date": None})
    plt.close(figure)

    noise_values = np.linspace(0, 2 * np.pi, 41)
    steady_polarity = np.empty_like(noise_values)
    for index, noise_width in enumerate(noise_values):
        realization_means = []
        for realization in range(REALIZATIONS):
            realization_rng = np.random.default_rng(SEED + 1000 * (realization + 1))
            realization_positions = realization_rng.uniform(0, BOX_SIZE, size=(PARTICLES, 2))
            realization_headings = realization_rng.uniform(-np.pi, np.pi, size=PARTICLES)
            history = simulate(
                noise_width,
                realization_positions,
                realization_headings,
                steps=SWEEP_STEPS,
                seed_offset=1000 * (realization + 1),
            )
            realization_means.append(history[-SAMPLE_STEPS:].mean())
        steady_polarity[index] = np.mean(realization_means)

    figure, axis = plt.subplots(figsize=(8, 4.6))
    axis.plot(noise_values / np.pi, steady_polarity, color="#1565c0", linewidth=2.2)
    axis.set(
        xlabel=r"Noise width $\eta/\pi$",
        ylabel=r"Steady-state polarity $\langle\Phi\rangle$",
        xlim=(0, 2),
        ylim=(0, 1.02),
    )
    axis.set_xticks([0, 0.5, 1, 1.5, 2], ["0", "0.5", "1", "1.5", "2"])
    axis.grid(alpha=0.2)
    axis.text(0.08, 0.1, "ordered", color="#1565c0", transform=axis.transAxes)
    axis.text(0.82, 0.1, "disordered", color="#606c71", transform=axis.transAxes)
    figure.tight_layout()

    destination = Path(__file__).resolve().parents[1] / "assets/images/projects/vicsek/vicsek-noise-sweep.svg"
    figure.savefig(destination, format="svg", metadata={"Date": None})
    plt.close(figure)


if __name__ == "__main__":
    main()
