---
type: reference
domain: stats
course: "STAT 132"
status: draft
---
# Flowchart: steps 1 and 2 (model for X, then the prior partner)

Step 1 asks questions of one result X and ends at a data model. Step 2 follows the arrow out of that model to its prior partner, then sets the partner's settings from the pretend data. Gold boxes are data models, blue boxes are priors.

**Override (2a):** if the problem gives the prior (a list of candidates with weights, or a named curve), use it and ignore the partner arrows. A list means step 6 adds.

```mermaid
flowchart TD
  subgraph S1["STEP 1: model for X (one result)"]
    Q1{"1a. What does one result look like?"}
    Q1 -->|"yes or no (1 or 0)"| BERN["Bernoulli(θ)"]
    Q1 -->|"whole-number count"| Q1b{"1b. Is there a fixed maximum?"}
    Q1 -->|"number on a continuous scale"| Q1c{"1c. What range can X take?"}
    Q1 -.->|"none of these"| OUT["1d. Out of scope: flag it"]
    Q1b -->|"yes: successes out of n tries"| BIN["Binomial(n, θ)"]
    Q1b -->|"no: events in a window"| POIS["Poisson(λ)"]
    Q1c -->|"between 0 and 1"| BETAX["Beta (mostly used as a prior)"]
    Q1c -->|"two fixed ends, flat"| UNIX["Uniform (mostly used as a prior)"]
    Q1c -->|"positive only"| QPOS{"Which shape?"}
    Q1c -->|"any number, negatives too"| QANY{"Which shape?"}
    QPOS -->|"wait for one event"| EXPO["Exponential(β)"]
    QPOS -->|"skewed hump"| GAMX["Gamma (mostly used as a prior)"]
    QANY -->|"symmetric bell"| NORM["Normal(μ), σ² known"]
    QANY -.->|"anything else"| OUT
  end

  subgraph S2["STEP 2: prior partner (2b), then its settings (2c)"]
    PBETA["Prior: Beta(α, β)"]
    PGAM["Prior: Gamma(α, β)"]
    PNORM["Prior: Normal"]
    SBETA["α = pretend successes
    β = pretend failures
    no idea at all: Beta(1, 1) = Uniform(0, 1)"]
    SGAMP["Poisson data:
    α = pretend events
    β = pretend windows"]
    SGAME["Exponential data:
    α = pretend events
    β = pretend total waiting time"]
    SNORM["prior center and spread,
    given in the problem"]
  end

  BERN -->|"θ is between 0 and 1"| PBETA
  BIN -->|"θ is between 0 and 1"| PBETA
  POIS -->|"λ is above 0"| PGAM
  EXPO -->|"β is above 0"| PGAM
  NORM -->|"μ is any number"| PNORM
  PBETA --> SBETA
  PGAM -->|"if X is Poisson"| SGAMP
  PGAM -->|"if X is Exponential"| SGAME
  PNORM --> SNORM

  classDef data fill:#f6d365,stroke:#8a6d00,color:#000
  classDef prior fill:#9ec5fe,stroke:#1f4e8c,color:#000
  classDef out fill:#eeeeee,stroke:#888,color:#000,stroke-dasharray: 4 3
  class BERN,BIN,POIS,EXPO,NORM data
  class PBETA,PGAM,PNORM,BETAX,UNIX,GAMX prior
  class OUT out
```

Sources: decision tree and allowed parameter values in [[STAT 132 Distribution Sheets]]; prior pairs in [[STAT 132 Kernels]] Table 3.
