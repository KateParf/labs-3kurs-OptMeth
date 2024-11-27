from one_dimensional import *

def test_f(x):
    return x * (x - 1)

if __name__ == "__main__":
    print(f"bisect    : {bisect(lambda x: x * (x - 1.0), -2, 2)}\n")
    print(f"golden    : {golden_ratio(lambda x: x * (x - 1.0), -2, 2)}\n")
    print(f"fibonacci : {fibonacci(lambda x: x * (x - 1.0), -2, 2)}\n")