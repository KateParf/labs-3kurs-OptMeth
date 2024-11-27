from typing import Callable
import numpy as np
from multi_dimensional import *
from .gradient_descend import grad

def conjGradientDescend(func: Callable[[np.ndarray], float], xStart: np.ndarray, eps: float = 1e-6, maxIterations: int = 100) -> np.array:
	x_i = np.array(xStart, dtype=float)
	x_i_1 = np.array(xStart, dtype=float)
	s_i = -1.0*grad(func, xStart, eps)
	cnt: int = 0
	while cnt != maxIterations:
		x_i_1 = x_i + s_i
		x_i_1 = fibonacci(func, x_i, x_i_1, eps)
		if np.linalg.norm(x_i_1 - x_i) < 2 * eps:
			break
		s_i_1 = grad(func, x_i_1, eps)
		omega = (np.sqrt(np.sum(s_i_1 * s_i_1)) ** 2) / (np.sqrt(np.sum(s_i * s_i)) ** 2)
		s_i * omega - s_i_1
		x_i = x_i_1
		cnt += 1
		
	print("Conj gradient descend iterations number: ", cnt + 1)
	return (x_i_1 + x_i) * 0.5
