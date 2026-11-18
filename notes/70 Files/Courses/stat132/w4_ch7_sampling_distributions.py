"""STAT 132 week 4: sampling distributions (Lecture 7, Reading04 chapter 7).

Run:  ~/.local/share/stat132-venv/bin/python w4_ch7_sampling_distributions.py
Every block prints GIVEN -> WHAT CHANGES -> RESULT; figures land in .
R function -> Python: pbinom(k, n, p, lower.tail=FALSE) = binom.sf(k, n, p);
pnorm(q, mean, sd) = norm.cdf(q, mean, sd); dbinom = binom.pmf; dnorm = norm.pdf.
"""
from math import sqrt
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, norm

FIGS = Path(__file__).parent  # pictures sit next to the script, Obsidian finds them by name


def section(title):
    print(f"\n=== {title} ===")


# ---------------------------------------------------------------- 7.1 the 4-step picture
def sampling_distribution(draw_sample, statistic, reps, rng):
    """The reading's 4 steps as code: fix the model, draw a sample, compute T, repeat."""
    return np.array([statistic(draw_sample(rng)) for _ in range(reps)])


# ---------------------------------------------------------------- 7.2 barcode scanner
section("7.2.1  P(p_hat >= 14/16) when p = 0.75")
n, p = 16, 0.75
print(f"given n={n}, p={p}; K = sum of X_i ~ Bin(16, 0.75); p_hat = K/16")
print(f"P(K >= 14) = P(K > 13) = {binom.sf(13, n, p):.6f}   (R: pbinom(13, 16, 0.75, lower.tail=FALSE) = 0.197111)")

section("7.2.2 / 7.3  center, spread, standard error of p_hat")
print(f"E[p_hat] = p = {p}")
print(f"Var(p_hat) = p(1-p)/n = {p * (1 - p) / n:.5f}")
print(f"SE(p_hat) = sqrt(p(1-p)/n) = {sqrt(p * (1 - p) / n):.4f}   (reading: 0.108)")
ph = 14 / 16
print(f"estimated SE using p_hat = 0.875: {sqrt(ph * (1 - ph) / n):.4f}   (reading: 0.083)")
print("sqrt(n) rule: n x4 -> SE /2")
for m in (16, 64, 256):
    print(f"  n = {m:3d}  SE = {sqrt(p * (1 - p) / m):.4f}")

# ---------------------------------------------------------------- 7.4 dispensers
section("7.4  difference of two sample means, sigma_A = 2 (n=16), sigma_B = 3 (n=25)")
var_d = 2**2 / 16 + 3**2 / 25
print(f"Var(D) = 4/16 + 9/25 = {var_d:.2f};  SE(D) = {sqrt(var_d):.3f}   (reading: 0.61, 0.781)")
print(f"P(D < 0 | Delta = 1) = {norm.cdf(0, 1, sqrt(var_d)):.7f}   (R: pnorm(0, 1, sqrt(0.61)) = 0.1002077)")
print(f"samples x4:  P(D < 0) = {norm.cdf(0, 1, sqrt(var_d / 4)):.4f}   (reading: 0.0052)")

rng = np.random.default_rng(132)
sim = sampling_distribution(
    lambda r: (r.normal(51, 2, 16), r.normal(50, 3, 25)),
    lambda s: s[0].mean() - s[1].mean(), 20000, rng)
print(f"simulation (20000 pairs, Delta=1): mean {sim.mean():.3f}, sd {sim.std():.3f}, P(D<0) {np.mean(sim < 0):.4f}")

xs = np.linspace(-2, 4, 500)
fig, ax = plt.subplots(figsize=(7, 4))
for scale, col, ls, lab in ((1, "gray", "-", "A: 16, B: 25"), (4, "darkorange", "--", "A: 64, B: 100"),
                            (16, "steelblue", ":", "A: 256, B: 400")):
    ax.plot(xs, norm.pdf(xs, 1, sqrt(var_d / scale)), color=col, ls=ls, lw=2, label=lab)
ax.axvline(0, color="firebrick", ls="--")
ax.set(ylim=(0, 2.2), xlabel="Estimated difference (milliliters)", ylabel="Density",
       title="Comparing two dispenser means")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(FIGS / "w4-fig7.1-dispensers.png", dpi=110)

# ---------------------------------------------------------------- 7.5 display minimum
section("7.5  earliest activation time, X ~ U(a, b=20), a_hat = W_n = min")
delays = [7.1, 10.4, 5.8, 13.2, 18.6, 9.5, 15.3]
print(f"given delays {delays}  ->  a_hat = min = {min(delays)}")
a, b, n = 4, 20, 7
e_w = a + (b - a) / (n + 1)
var_w = n * (b - a) ** 2 / ((n + 1) ** 2 * (n + 2))
print(f"if a = 4: E[W_7] = 4 + 16/8 = {e_w}, bias = {e_w - a}, SE = {sqrt(var_w):.3f}   (reading: 6, 2, 1.764)")
print(f"P(W_7 > 6) = (14/16)^7 = {(14 / 16) ** 7:.3f};  n = 28: {(14 / 16) ** 28:.3f}   (reading: 0.393, 0.024)")
w = rng.uniform(a, b, size=(20000, n)).min(axis=1)
print(f"simulation: mean {w.mean():.3f}, sd {w.std():.3f}, P(W>6) {np.mean(w > 6):.3f}")

# ---------------------------------------------------------------- 7.7 figure 7.2 (Reading) / Lecture 7 grid
def proportion_grid(sample_sizes, probabilities, fname, title):
    grid = np.linspace(-0.2, 1.2, 600)
    fig, axes = plt.subplots(len(sample_sizes), len(probabilities),
                             figsize=(3.4 * len(probabilities), 2.6 * len(sample_sizes)))
    for i, n in enumerate(sample_sizes):
        for j, p in enumerate(probabilities):
            ax = axes[i, j]
            exact = binom.pmf(np.arange(n + 1), n, p)
            approx = norm.pdf(grid, p, sqrt(p * (1 - p) / n)) / n  # density x spacing 1/n
            ax.plot(grid, approx, color="steelblue", lw=2)
            ax.plot(np.arange(n + 1) / n, exact, "o", color="firebrick", ms=3)
            ax.set_title(f"n = {n}, p = {p}", fontsize=9)
            ax.set_ylim(0, max(exact.max(), approx.max()) * 1.1)
    fig.suptitle(title)
    fig.supxlabel("Sample proportion")
    fig.supylabel("Probability mass")
    fig.tight_layout()
    fig.savefig(FIGS / fname, dpi=100)


proportion_grid((8, 24, 60), (0.2, 0.6, 0.9), "w4-fig7.2-proportion-grid.png",
                "Reading04 Fig 7.2: exact (red) vs normal approx (blue)")
proportion_grid((5, 10, 30, 50), (0.1, 0.3, 0.5), "w4-lec7-proportion-grid.png",
                "Lecture 7 section 1.4: exact (red) vs CLT approx (blue)")

# ---------------------------------------------------------------- 7.8 figure 7.3
section("7.8  10,000 simulated scanner trials, n = 24, p = 0.6")
rng = np.random.default_rng(132)
props = rng.binomial(1, 0.6, size=(10000, 24)).mean(axis=1)
print(f"mean {props.mean():.4f} (theory 0.6), sd {props.std():.4f} (theory {sqrt(0.6 * 0.4 / 24):.4f})")
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(props, bins=(np.arange(-0.5, 25.5, 1)) / 24, color="skyblue", edgecolor="white")
ax.axvline(0.6, color="firebrick", lw=2, ls="--")
ax.set(xlim=(0, 1), xlabel="Sample proportion", ylabel="Number of simulated samples",
       title="One first-pass rate from each scanner trial")
fig.tight_layout()
fig.savefig(FIGS / "w4-fig7.3-simulated-proportions.png", dpi=110)

# ---------------------------------------------------------------- Lecture 7 Ex 1.2, 1.3
section("Lec 7 Ex 1.2  mu_hat = X_bar ~ N(mu, sigma^2/n), check mu=5, sigma=2, n=10")
xb = rng.normal(5, 2, size=(20000, 10)).mean(axis=1)
print(f"simulated mean {xb.mean():.3f} (5), variance {xb.var():.3f} (sigma^2/n = {4 / 10})")

section("Lec 7 Ex 1.3  theta_hat = max of U(0, theta): CDF (t/theta)^n, mean n*theta/(n+1); theta=10, n=5")
mx = rng.uniform(0, 10, size=(20000, 5)).max(axis=1)
print(f"P(max <= 8): exact (8/10)^5 = {0.8 ** 5:.4f}, simulated {np.mean(mx <= 8):.4f}")
print(f"mean: exact {5 * 10 / 6:.3f}, simulated {mx.mean():.3f}")
print("\nsaved w4-fig7.1-dispensers.png, w4-fig7.2-proportion-grid.png, "
      "w4-lec7-proportion-grid.png, w4-fig7.3-simulated-proportions.png")
