from typing import Callable
import numpy as np
from multi_dimensional import *

def partial(func: Callable[[np.ndarray], float], x: np.ndarray, index: int, eps: float) -> float:
    x[index] += eps
    f_r = func(x)
    x[index] -= 2.0 * eps
    f_l = func(x)
    x[index] += eps
    return (f_r - f_l) / eps * 0.5

def grad(func: Callable[[np.ndarray], float], x: np.ndarray, eps: float):
	df = np.array(x)
	for i in range(len(x)):
		df[i] = partial(func, x, i, eps)
	return df

def gradientDescend(func: Callable[[np.ndarray], float], xStart: np.ndarray, eps: float = 1e-6, maxIterations: int = 100) -> np.array:
	x_i = np.array(xStart, dtype=float)
	x_i_1 = np.array(xStart, dtype=float)
	cnt: int = 0
	while cnt != maxIterations:
		x_i_1 = x_i - grad(func, x_i, eps)
		x_i_1 = fibonacci(func, x_i, x_i_1, eps)
		if np.linalg.norm(x_i_1 - x_i) < 2 * eps: 
			break
		x_i = x_i_1
		cnt += 1
	
	print("gradient descend iterations number: ", cnt + 1)
	return (x_i_1 + x_i)*0.5


