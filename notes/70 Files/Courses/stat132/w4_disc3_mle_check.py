"""STAT 132 Discussion 3: check each closed-form MLE by brute force.

Run:  ~/.local/share/stat132-venv/bin/python w4_disc3_mle_check.py
Idea: simulate data from a known truth, then (1) apply the formula you derived and
(2) let a computer search for the parameter value with the highest log-likelihood.
If the two agree, the formula is right. If you change a formula, rerun this.
"""
import numpy as np
from scipy.optimize import minimize, minimize_scalar
from scipy.stats import norm

rng = np.random.default_rng(132)
N = 2000


def section(title):
    print(f"\n=== {title} ===")


# Q1  Normal(mu, sigma^2), both unknown
section("Q1  Normal: mu_hat = x_bar, sigma2_hat = (1/n) sum (x - x_bar)^2")
x = rng.normal(3, 2, N)


def neg_loglik_normal(params):
    mu, log_s2 = params
    return -np.sum(norm.logpdf(x, mu, np.sqrt(np.exp(log_s2))))


opt = minimize(neg_loglik_normal, [0.0, 0.0])
print(f"formula:  mu {x.mean():.4f}   sigma2 {np.mean((x - x.mean()) ** 2):.4f}")
print(f"search:   mu {opt.x[0]:.4f}   sigma2 {np.exp(opt.x[1]):.4f}")
print(f"(divide by n-1 instead would give {x.var(ddof=1):.4f}; MLE divides by n)")

# Q2  f(x|theta) = theta / x^(theta+1), x > 1  (Pareto with minimum 1)
section("Q2  f(x|theta) = theta / x^(theta+1): theta_hat = n / sum(log x)")
theta_true = 2.5
x = (1 - rng.uniform(size=N)) ** (-1 / theta_true)  # inverse-CDF draw: F(x) = 1 - x^(-theta)
loglik = lambda t: len(x) * np.log(t) - (t + 1) * np.sum(np.log(x))
opt = minimize_scalar(lambda t: -loglik(t), bounds=(1e-6, 50), method="bounded")
print(f"truth {theta_true}   formula {len(x) / np.sum(np.log(x)):.4f}   search {opt.x:.4f}")

# Q3  U[theta1, theta2]
section("Q3  U[theta1, theta2]: theta1_hat = min, theta2_hat = max")
x = rng.uniform(-1, 4, 50)
print(f"truth (-1, 4)   formula ({x.min():.4f}, {x.max():.4f})")
print("why no calculus: L = 1/(theta2-theta1)^n is 0 unless theta1 <= min and theta2 >= max,")
print("and shrinking the interval only raises L, so pull both ends in as far as the data allow.")
for t1, t2 in ((x.min(), x.max()), (x.min() - 0.1, x.max()), (x.min() + 0.01, x.max())):
    inside = (t1 <= x.min()) and (t2 >= x.max())
    print(f"  try ({t1:.3f}, {t2:.3f}): L = {(t2 - t1) ** -len(x) if inside else 0:.3e}")

# Q4  Exponential(lambda): median = log(2)/lambda
section("Q4  Exponential median: lambda_hat = 1/x_bar, median_hat = log(2) * x_bar")
lam = 0.5
x = rng.exponential(1 / lam, N)
print(f"true median {np.log(2) / lam:.4f}   invariance {np.log(2) * x.mean():.4f}   "
      f"(sample median {np.median(x):.4f}, a different rule)")

# Q5  Normal 0.95 quantile: a = mu + 1.645 sigma
section("Q5  Normal 0.95 quantile: a_hat = mu_hat + z_0.95 * sigma_hat, z_0.95 = 1.645")
x = rng.normal(10, 3, N)
sig_hat = np.sqrt(np.mean((x - x.mean()) ** 2))
print(f"z_0.95 = {norm.ppf(0.95):.4f}")
print(f"true a {10 + norm.ppf(0.95) * 3:.4f}   invariance {x.mean() + norm.ppf(0.95) * sig_hat:.4f}   "
      f"(empirical 95th percentile {np.quantile(x, 0.95):.4f})")
