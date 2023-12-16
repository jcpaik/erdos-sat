import itertools
import math
import os

class Clauses:
    def __init__(self, instance, name, cnf):
        self._instance = instance
        self._name = name
        self._cnf = cnf

    def __len__(self):
        return len(self._cnf)

    def __iter__(self):
        return iter(self._cnf)

    def __str__(self):
        return self._name

    def __repr__(self):
        return f"{self._name} = {self._cnf}"

    def __and__(self, other):
        assert(self._instance is other._instance)
        name = f"({self._name})&({other._name})"
        cnf = self._cnf + other._cnf
        return Clauses(self._instance, name, cnf)

    def __or__(self, other):
        assert(self._instance is other._instance)
        name = f"({self._name})|({other._name})"
        # TODO: Add heuristic to introduce new variable when size explodes
        cnf = [s + o for s, o in itertools.product(self, other)]
        return Clauses(self._instance, name, cnf)

    def __invert__(self):
        name = f"~({self._name})"
        # TODO: Add heuristic to introduce new variable when size explodes
        cnf = [[-v for v in c] for c in itertools.product(*self._cnf)]
        return Clauses(self._instance, name, cnf)

    def implies(self, other):
        return (~self) | other

    def solution(self):
        assert(self._instance._solution is not None)

        for clause in self._cnf:
            any_true = False
            for var in clause:
                if self._instance._solution[abs(var)] == var:
                    any_true = True
                    break
            if not any_true:
                return False
        return True

class SATInstance:
    def __init__(self):
        self._num_vars = 0
        self._clauses = []
        self._solution = None

    def new_var(self, name):
        """Generate a new variable with new name"""
        # TODO: equiv_to option -> new variable is equivalent to given clauses
        self._num_vars += 1
        return Clauses(self, name, [[self._num_vars]])

    def add(self, clauses):
        self._clauses += clauses

    def add_implies(self, c0, c1):
        self.add(c0.implies(c1))

    def write(self, filename):
        with open(filename, "w") as f:
            head = f"p cnf {self._num_vars} {len(self._clauses)}"
            f.write(head + "\n")
            f.writelines([" ".join(map(str, c))+" 0\n" for c in self._clauses])
    
    def load(self, filename):
        self._solution = [None]
        with open(filename, "r") as file:
            for line in file:
                if line[:2] != "v ":
                    continue
                self._solution.extend(map(int, line[2:].split()))

    def solve(self, filename="tmp"):
        self.write(f"{filename}.cnf")
        out_code = os.system(f"kissat {filename}.cnf {filename}.unsat > {filename}.out")
        successful = (out_code == 2560)
        if not successful:
            return False
        else:
            os.system(f"rm {filename}.unsat")
            os.system(f"mv {filename}.out {filename}.sat")
            self.load(f"{filename}.sat")
            return True
