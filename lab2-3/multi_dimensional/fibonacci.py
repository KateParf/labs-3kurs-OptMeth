from typing import Callable
import numpy as np

def fib_prev(fn: float, fn_plus_1: float):
    return fn_plus_1 - fn, fn

def fib_pair(ratio: float):
    fn_i, fn_i_1, cnt = 1.0, 1.0, 0
    while fn_i_1 < ratio:
        cnt += 1
        tmp, fn_i_1 = fn_i_1, fn_i
        fn_i += tmp
    return fn_i, fn_i_1, cnt


def fibonacci(func: Callable[[np.ndarray], float], left:  np.ndarray, right:  np.ndarray, eps: float = 1e-6) -> np.ndarray:
    lhs = np.array(left, dtype=float)
    rhs = np.array(right, dtype=float)
    condition = np.linalg.norm(rhs - lhs) / eps
    fib_2, fib_1, cnt = fib_pair(condition)

    x_l = lhs + (rhs - lhs) * ((fib_2 - fib_1) / fib_2)
    x_r = lhs + (rhs - lhs) * (fib_1 / fib_2)
    f_l = func(x_l)
    f_r = func(x_r)

    for _ in range(cnt):
        fib_1, fib_2 = fib_prev(fib_1, fib_2)      
        if f_l > f_r:
            lhs, x_l, f_l = x_l, x_r, f_r
            x_r = lhs + (rhs - lhs) * (fib_1 / fib_2)
            f_r = func(x_r)
        else:
            rhs, x_r, f_r = x_r, x_l, f_l
            x_l = lhs + (rhs - lhs) * ((fib_2 - fib_1) / fib_2)
            f_l = func(x_l)

    print("fibonacci::function arg range: ", np.linalg.norm(rhs - lhs))
    print("fibonacci::function probes count: ", cnt + 2)
    return (rhs + lhs) * 0.5


