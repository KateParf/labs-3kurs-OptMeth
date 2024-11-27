from multi_dimensional import *
import numpy as np

def targetFunc(x: np.ndarray) -> float:
    return (x[0] - 6) * x[0] + (x[1] - 5) * x[1] 

def bound1(x: np.ndarray) -> float:
    #return 1 / (5 - x[0] * 2 + x[1] * 3)
    return 1 / (x[0] - 11)

def bound2(x: np.ndarray) -> float:
    #return 1 / (6 + x[0] * 3 - x[1])
    return 1 / (-x[0] - 2)

def bound3(x: np.ndarray) -> float:
    #return 1 / (6 + x[0] * 3 - x[1])
    return 1 / (x[1] - 6)

def bound4(x: np.ndarray) -> float:
    #return 1 / (6 + x[0] * 3 - x[1])
    return 1 / (-x[1] - 2)
    


if __name__ == "__main__":
    x_0 = np.array([5.0, 3.0], dtype=float)
    x_1 = np.array([0.0, 0.0], dtype=float)
    x_start = np.array([-14, -33.98], dtype=float)
    boundaries = []

    # print(f"bisect             : {bisect(targetFunc, x_1, x_0)}\n")
    # print(f"golden             : {golden_ratio(targetFunc, x_1, x_0)}\n")
    # print(f"fibonacci          : {fibonacci(targetFunc, x_1, x_0)}\n")
    # print(f"perCordDescend     : {perCordDescend(targetFunc, x_start)}\n")
    # print(f"gradientDescend    : {gradientDescend(targetFunc, x_start)}\n")
    # print(f"conjGradientDescend: {conjGradientDescend(targetFunc, x_start)}\n")
    # print(f"newtoneRaphson     : {newtoneRaphson(targetFunc, x_start)}\n")

    target = PenaltyFunction()
    target.target = targetFunc
    
    print(f"gradientDescend with penalty: {gradientDescend(target, x_start)}")
    print(f"conjGradientDescend with penalty: {conjGradientDescend(target, x_start)}")
    print(f"newtoneRaphson with penalty: {newtoneRaphson(target, x_start)}")

    target.add_bound(bound1)
    target.add_bound(bound2)
    target.add_bound(bound3)
    target.add_bound(bound4)

    print(f"gradientDescend with penalty:     {gradientDescend(target, x_start)}")
    print(f"conjGradientDescend with penalty: {conjGradientDescend(target, x_start)}")
    print(f"newtoneRaphson with penalty:      {newtoneRaphson(target, x_start)}")

    