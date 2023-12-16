# An SAT encoding of Erdős-Szekeres conjecture

This program is a part of a research paper by 
[Jineon Baek](https://jcpaik.github.io/) and [Martin Balko](https://kam.mff.cuni.cz/~balko/) 
in preparation.

The _Erdős–Szekeres conjecture_ states that 
$2^{n-2} + 1$ points on a plane, with no three on a line,
should contain a set of $n$ points forming the vertices of a convex polygon.
This software solves a hypergraph generalization of the problem defined as the following.

- The input values are $n, a, b$ and $N$.
- Every subsets of size 3 of the set $[N] = \{1, 2, \dots, N\}$ should be colored by either red or blue.
- Any increasing sequence $1 \leq a_1 < \cdots < a_m \leq N$ is a _red chain_ (resp. _blue chain_) if the set of each three consecutive values $\{a_i, a_{i+1}, a_{i+2}\}$ is colored red (resp. blue).
- A pair of a red chain of length $a$ and a blue chain of length $b$ sharing the same leftmost and rightmost value is called an _$n$-gon_ where $n = a + b - 2$. 

The program either 

- finds a coloring of all size 3 subsets of $[N]$ with no $n$-gon, red chain of size $a$ or blue chain of size $b$
- or prove that no such coloring exists

using the [Kissat](https://github.com/arminbiere/kissat) SAT solver.

More details on why is this problem a generalization of the Erdős–Szekeres conjecture will be in our upcoming draft.

## Dependencies

- [fire](https://github.com/google/python-fire) python library
  - Either manually install it or use [pipenv](https://pypi.org/project/pipenv/)
- [kissat](https://github.com/arminbiere/kissat) installed and located in `$PATH`

## Usage

```
python main.py n a b N
```

If using pipenv, one can run `pipenv install` and then `pipenv shell` 
then run the command above. 
Otherwise, one should install the [fire](https://github.com/google/python-fire) python library.

If a coloring exists, the program stores a coloring in `.color` file, which is a text file
with each line `i j k C` denoting the coloring `C` (either `R` or `B` for red or blue respectively) 
of the set $\{i, j, k\}$.
If a coloring does not exist, the program stores a proof of unsolvability in `.unsat` file.

The default `filename` used is `etv_n_a_b_N` where the corresponding values of n, a, b and N are replaced with their actual values. This can be overriden using `--filename` option.

The program also spawns the following files as well.

- `filename.cnf` for the actual SAT instance used
- `filename.out` for the output of the Kissat solver