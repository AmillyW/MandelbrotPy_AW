import numpy as np


def MDB_MapRule_Continuous(c, max_iter: int) -> int:
    z = 0
    for n in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            smooth_n = n + 1 - np.log(np.log(abs(z))) / np.log(2)
            return smooth_n
    return max_iter
