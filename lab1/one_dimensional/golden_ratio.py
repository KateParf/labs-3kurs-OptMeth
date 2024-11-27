from typing import Callable

PHI = 1.61803398874989484820
PSI = 0.61803398874989484820

def golden_ratio(func: Callable[[float], float], lhs: float, rhs: float, eps: float = 1e-6, maxIter: int = 100) -> float:
    
    cnt: int = 0
    rhs, lhs = (lhs, rhs) if (lhs > rhs) else (rhs, lhs)
    xl = rhs - (rhs - lhs) * PSI
    xr = lhs + (rhs - lhs) * PSI
    fl = func(xl)
    fr = func(xr)

    while((cnt := cnt + 1) < maxIter and rhs-lhs >= 2 * eps):

        if fl > fr:
            lhs, xl, fl = xl, xr, fr
            xr = lhs + (rhs - lhs) * PSI
            fr = func(xr)
        else:
            rhs, xr, fr = xr, xl, fl
            xl = rhs - (rhs - lhs) * PSI
            fl = func(xl)

    print("Func probes: ", cnt + 2)
    print("Rang range: ", rhs - lhs)
    return (lhs + rhs) * 0.5
        