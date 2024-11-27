from typing import Callable
import numpy as np

def bisect(func: Callable[[np.ndarray], float], left:  np.ndarray, right:  np.ndarray, eps: float = 1e-6, maxIterations: int = 100) -> np.array:
    lhs = np.array(left, dtype=float)
    rhs = np.array(right, dtype=float)
    x_c = np.divide((rhs - lhs), np.linalg.norm(rhs - lhs)) * eps
    dir = x_c
    cnt: int = 0
    while(((cnt:=cnt+1) < maxIterations) and (np.linalg.norm(rhs - lhs) >= 2 * eps)):
        x_c = (rhs + lhs) * 0.5
        if (func(x_c + dir) > func(x_c - dir)):
            rhs = x_c
        else:
            lhs = x_c

    print("biSect function arg range: ", np.linalg.norm(rhs - lhs))
    print("biSect function probes count: ", 2 * cnt)

    return (rhs + lhs)*0.5

