---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Gamma and Beta Functions"
tags:
  - decks
---
# STAT 132 Cards - Gamma and Beta Functions (read before the distribution decks)

## Gamma and Beta Functions
| Front | Back | Notes |
| --- | --- | --- |
| What problem does the Gamma function solve? | **It extends factorials beyond whole numbers**, so values like $\Gamma(4.5)$ make sense. | Lecture_01 p.3; motivation |
| What is $\Gamma(5)$? | $4! = 24$. | Lecture_01 p.3; worked example |
| What is $\Gamma(1)$? | $0! = 1$. | Lecture_01 p.4; worked example |
| What step rule does the Gamma function follow, matching $n! = n \cdot (n-1)!$? | $\Gamma(x + 1) = x\,\Gamma(x)$. | formula |
| Read $\Gamma(x) = \int_0^\infty t^{x-1} e^{-t}\,dt$ aloud. | *Read aloud: "Gamma of x equals the integral from zero to infinity of t to the x minus one times e to the minus t, d t."* | Lecture_01 p.3; notation |
| Where does $\Gamma$ appear in the Gamma distribution? | **In its constant $\beta^\alpha / \Gamma(\alpha)$**, which makes the total area 1. | Lecture_01 p.3; assembly; dep: [[Bayes Update Algorithm]] |
| What job does $B(\alpha, \beta)$ do in the Beta distribution? | **It divides $x^{\alpha-1}(1-x)^{\beta-1}$ so the area from 0 to 1 is exactly 1.** | Lecture_01 p.3; assembly |
| What is $B(2, 3)$? | $\dfrac{\Gamma(2)\Gamma(3)}{\Gamma(5)} = \dfrac{1 \cdot 2}{24} = \dfrac{1}{12}$. | worked example |
| Gamma function vs Gamma distribution: which is which? | **$\Gamma$ is a number-making function (factorials extended). Gamma$(\alpha, \beta)$ is a probability curve whose constant contains $\Gamma$.** | discrimination |
| Beta function vs Beta distribution: which is which? | **$B(\alpha, \beta)$ is a number built from Gammas. Beta$(\alpha, \beta)$ is a probability curve on 0 to 1 that divides by it.** | discrimination |
| Why does every distribution need a normalizing constant? | **Its total area (or sum) must be exactly 1 to be a probability.** *Side note, not tested: The constant fixes that.* | motivation; dep: [[Bayes Update Algorithm]] |

# Node map
```json
[
 {
  "name": "Gamma and Beta Functions",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "STAT 132",
  "prereqs": [
   "Factorial"
  ],
  "page": 3,
  "summary": "$\\Gamma(x) = \\int_0^\\infty t^{x-1}e^{-t}dt$ extends factorials ($\\Gamma(n)=(n-1)!$); $B(x,y)=\\Gamma(x)\\Gamma(y)/\\Gamma(x+y)$."
 }
]
```

# Frankenstein problems

None yet.
