from typing import Callable

def fib_prev(fn: float, fn_plus_1: float):
    return fn_plus_1 - fn, fn

def fib_pair(ratio: float, fn_i: float, fn_i_1: float, iter: int):
    while fn_i < ratio:
        iter += 1
        tmp, fn_i_1 = fn_i_1, fn_i
        fn_i += tmp
    return fn_i, fn_i_1, iter


def fibonacci(func: Callable[[float], float], lhs: float, rhs: float, eps: float = 1e-6, maxIter: int = 100) -> float:
    if (lhs > rhs):
        rhs, lhs = lhs, rhs
    ratio = (rhs - lhs) / eps
    fn_i: float = 1
    fn_i_1: float = 1
    cnt: int = 0
    fn_i, fn_i_1, cnt = fib_pair(ratio, fn_i, fn_i_1, cnt)

    xr = lhs + (rhs - lhs) * (fn_i_1 / fn_i)
    xl = lhs + (rhs - lhs) * ((fn_i - fn_i_1) / fn_i)

    fl = func(xl)
    fr = func(xr)

    fn_i_1, fn_i = fib_prev(fn_i_1, fn_i)
    cnt_ = cnt + 1

    while cnt_ := cnt_ - 1:
        if fl > fr:
            lhs, xl, fl = xl, xr, fr
            xr = lhs + (rhs - lhs) * (fn_i_1 / fn_i)
            fr = func(xr)
        else:
            rhs, xr, fr = xr, xl, fl
            xl = lhs + (rhs - lhs) * ((fn_i - fn_i_1) / fn_i)
            fl = func(xl)
        fn_i_1, fn_i = fib_prev(fn_i_1, fn_i)

    print("Func probes: ", cnt + 2)
    print("Rang range: ", rhs - lhs)
    return (lhs + rhs) * 0.5
        



