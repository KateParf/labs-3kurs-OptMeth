from typing import Callable

def bisect(func: Callable[[float], float], lhs: float, rhs: float, eps: float = 1e-6, maxIter: int = 100) -> float:
    cnt: int = 0
    if (lhs > rhs):
        rhs, lhs = lhs, rhs
    while(((cnt:=cnt+1) < maxIter) and (rhs-lhs >= 2*eps)):
        xc = (rhs + lhs) * 0.5
        if func(xc - eps) > func(xc + eps):
            lhs = xc
        else:
            rhs = xc
    print("Func probes: ", cnt * 2)
    print("Rang range: ", rhs - lhs)
    return (lhs + rhs) * 0.5