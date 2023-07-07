# TODO: copy the jupyter notebook codes to here, make it reproducable

import os
import fire
import lib.erdos as erdos
from lib.util import binom

def main(n, a, b, N, filename=None, signotope=False):
    inst = erdos.etv(n, a, b, N)
    if not filename:
        filename = f"etv_{n}_{a}_{b}_{N}"
    inst.solve(filename)

if __name__ == '__main__':
    fire.Fire(main)
