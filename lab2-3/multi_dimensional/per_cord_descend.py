from typing import Callable
import numpy as np
from multi_dimensional import *

def perCordDescend(func: Callable[[np.ndarray], float], xStart:  np.ndarray, eps: float = 1e-6, maxIterations: int = 100) -> np.array:
    x_0 =  np.array(xStart, dtype=np.float64)
    x_1 =  np.array(xStart, dtype=np.float64)
    step: float = 1.0
    optCoordinatesCount: int = 0
    for iteration in range(0, maxIterations):

        coordinateId = iteration % len(x_0)
        x_1[coordinateId] -= eps
        y_0 = func(x_1)
        x_1[coordinateId] += 2.0 * eps
        y_1 = func(x_1)
        x_1[coordinateId] -= eps
        x_1[coordinateId] = (x_1[coordinateId] + step) if (y_0 > y_1) else (x_1[coordinateId] - step)
        x_i = x_0[coordinateId]
        x_1 = fibonacci(func, x_0, x_1, eps)
        x_0 =  np.array(x_1, dtype=np.float64)

        if (abs(x_1[coordinateId] - x_i) < 2 * eps):
            optCoordinatesCount += 1
            if (optCoordinatesCount == len(x_1)):
                print("per cord descend iterations number: ", iteration + 1)
                return x_0
            continue   

        optCoordinatesCount = 0

    print("per cord descend iterations number: ", maxIterations)
    return x_0

