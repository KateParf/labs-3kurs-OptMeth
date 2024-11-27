from typing import Callable
import numpy as np
from multi_dimensional import *
from .gradient_descend import grad, partial

def partial2(func: Callable[[np.ndarray], float], x: np.ndarray, row: int, col: int, eps: float) -> float:
    x[col] += eps
    f_r = partial(func, x, row, eps)
    x[col] -= 2 * eps
    f_l = partial(func, x, row, eps)
    x[col] += eps
    return (f_r - f_l) / (2 * eps)

def hessian(func: Callable[[np.ndarray], float], x: np.ndarray, eps: float):
    n = len(x)
    res = np.zeros((n, n), dtype=float)
    for row in range(n):
        for col in range(row + 1):  
            res[row, col] = partial2(func, x, row, col, eps)
            res[col, row] = res[row, col]
    return res

def newtoneRaphson(func: Callable[[np.ndarray], float], xStart: np.ndarray, eps: float = 1e-6, maxIterations: int = 100) -> np.array:
    x_i = np.array(xStart, dtype=float)
    x_i_1 = np.array(xStart, dtype=float)
    cnt = 0
    while cnt != maxIterations:
        gradient = grad(func, x_i, eps)
        hess = np.linalg.inv(hessian(func, x_i, eps))
        x_i_1 = x_i - (np.dot(hess, gradient))
        if np.linalg.norm(x_i_1 - x_i) < 2 * eps: 
            break
        x_i = x_i_1
        cnt+=1

    print("Newtone-Raphson method iterations number: ", cnt)
    return (x_i_1 + x_i) * 0.5

