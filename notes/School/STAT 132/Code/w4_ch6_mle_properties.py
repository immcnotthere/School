"""STAT 132 week 4: MLE properties (Lecture 6, Reading04 chapter 6).

Run:  ~/.local/share/stat132-venv/bin/python w4_ch6_mle_properties.py
Every block prints GIVEN -> WHAT CHANGES -> RESULT; figures land in .
Python port of the R code in Reading04; the numbers match the reading.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

FIGS = Path(__file__).parent  # pictures sit next to the script, Obsidian finds them by name


def section(title):
    print(f"\n=== {title} ===")


# ---------------------------------------------------------------- invariance
def mle_exponential_rate(x):
    """GIVEN a sample of waits. CHANGES: n / sum(x). RESULT: lambda_hat (rate per minute)."""
    return len(x) / sum(x)


def invariance(g, theta_hat):
    """Invariance: the MLE of g(theta) is g(theta_hat). No new maximization."""
    return g(theta_hat)


section("Ex 1.1 / 6.1.1  average wait, Exponential(lambda)")
waits = [2, 4, 1, 3, 5]
lam_hat = mle_exponential_rate(waits)
print(f"given waits      {waits}")
print(f"lambda_hat       n/sum = {len(waits)}/{sum(waits)} = {lam_hat:.4f} per minute")
print(f"mean = 1/lambda  -> MLE {invariance(lambda l: 1 / l, lam_hat):.4f} minutes (= x_bar)")

section("Ex 1.2 / 6.1.2  variance of waits")
print(f"var = 1/lambda^2 -> MLE {invariance(lambda l: 1 / l**2, lam_hat):.4f} square minutes (= x_bar^2)")
print(f"compare: usual sample variance s^2 = {np.var(waits, ddof=1):.4f}  (different rule, no model)")

section("Ex 1.3 / 6.1.3  median of U(0, theta)")
u = [2, 7, 4, 9]
theta_hat = max(u)
print(f"given sample     {u}")
print(f"theta_hat = max  {theta_hat}")
print(f"median = theta/2 -> MLE {invariance(lambda t: t / 2, theta_hat)}")
print(f"compare: sample median = {np.median(u)}  (different rule)")

# ---------------------------------------------------------------- consistency
section("6.2.1  consistency: P(|M_n - 10| > 1) = 0.9^n")
for n in (5, 20, 50, 200):
    print(f"n = {n:4d}  exact {0.9 ** n:.4f}")

rng = np.random.default_rng(132)
print("simulation check (5000 samples each):")
for n in (5, 20, 50):
    m = rng.uniform(0, 10, size=(5000, n)).max(axis=1)
    print(f"n = {n:4d}  simulated {np.mean(np.abs(m - 10) > 1):.4f}")

# ---------------------------------------------------------------- bias
section("Ex 1.4 / 6.4  bias of theta_hat = max, theta = 10")
theta = 10
print(f"{'n':>5} {'E[M_n] formula':>15} {'E[M_n] sim':>11} {'bias':>8} {'(n+1)/n * M_n sim':>18}")
for n in (5, 20, 100):
    m = rng.uniform(0, theta, size=(20000, n)).max(axis=1)
    exact = n * theta / (n + 1)
    print(f"{n:5d} {exact:15.2f} {m.mean():11.2f} {exact - theta:8.2f} {((n + 1) / n * m).mean():18.2f}")

# ---------------------------------------------------------------- figure 6.1
rng = np.random.default_rng(132)
fig, axes = plt.subplots(1, 3, figsize=(12, 3.6))
for ax, n in zip(axes, (5, 20, 100)):
    maxima = rng.uniform(0, theta, size=(5000, n)).max(axis=1)
    ax.hist(maxima, bins=np.arange(0, 10.25, 0.25), density=True, color="skyblue", edgecolor="white")
    ax.axvline(theta, color="firebrick", lw=2, ls="--", label="true endpoint")
    ax.axvline(n * theta / (n + 1), color="steelblue", lw=2, label="E[max]")
    ax.set(xlim=(0, 10.5), xlabel="Estimated endpoint", ylabel="Density", title=f"Sample size = {n}")
axes[0].legend(loc="upper left", fontsize=8)
fig.tight_layout()
fig.savefig(FIGS / "w4-fig6.1-uniform-max.png", dpi=110)
print("\nsaved w4-fig6.1-uniform-max.png")
