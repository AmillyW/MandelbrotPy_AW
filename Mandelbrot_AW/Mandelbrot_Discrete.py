def MDB_MapRule_Discrete(c, max_iter: int) -> int:
    z = 0
    for n in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return n
    return max_iter
