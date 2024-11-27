from typing import Callable
import numpy as np

PHI = 1.61803398874989484820
PSI = 0.61803398874989484820     

def golden_ratio(func: Callable[[ np.ndarray], float], left:  np.ndarray, right:  np.ndarray, eps: float = 1e-6, maxIterations: int = 100) -> np.array:
    lhs =  np.array(left, dtype=float)
    rhs =  np.array(right, dtype=float)
    x_l = rhs - (rhs - lhs) * PSI
    x_r = lhs + (rhs - lhs) * PSI
    f_l = func(x_l)
    f_r = func(x_r)
    cnt: int = 0
    while(((cnt := cnt + 1) < maxIterations) and (np.linalg.norm(rhs - lhs) > 2 * eps)):
        if (f_l > f_r):
            lhs, x_l, f_l = x_l, x_r, f_r
            x_r = lhs + (rhs - lhs) * PSI
            f_r = func(x_r)
        else:
            rhs, x_r, f_r = x_r, x_l, f_l
            x_l = rhs - (rhs - lhs) * PSI
            f_l = func(x_l)

    print("goldenRatio::function arg range: ", np.linalg.norm(rhs - lhs))
    print("goldenRatio::function probes count: ", cnt + 2)
    return (rhs+lhs)*0.5