# An SAT encoding of Erdos-Szekeres conjecture

## Dependencies

- [fire](https://github.com/google/python-fire) python library
  - Either manually install it or use [pipenv](https://pypi.org/project/pipenv/)
- [kissat](https://github.com/arminbiere/kissat) installed and located in `$PATH`

## Usage

```
python main.py n a b N
```
checks if `N` points with no `n`-gon, `a`-cap and `b`-cup exists. The SAT
instance is produced as `cnf` file, and either the solution or unsatisfiabilty
proof is generated as `.sat` or `.unsat` file respectively.
