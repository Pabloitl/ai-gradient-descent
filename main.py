import re
import random
from sympy import (
    symbols,
    lambdify,
    derive_by_array,
    Matrix,
    parse_expr
)


def find_max(f, syms, h: float = 1e-3, eps: float = 1e-3, iterations: int = 100, point: list[float] = None):
    variables = symbols(syms)
    grad_f = lambdify(variables, derive_by_array(f, variables))
    result = Matrix([1] * len(variables))

    if point is None or len(point) != len(variables):
        print(f'\nInvalid point → "{point}", choosing a random one')
        result = Matrix([random.randrange(-100, 100) for _ in range(len(variables))])
    else:
        result = Matrix(point)

    print()
    print(f'Starting at point {result}')

    for _ in range(iterations):
        grad_value = Matrix(grad_f(*result))

        if grad_value.norm() < eps:
            break

        result += grad_value * h

    return (result[0], result[1])


def main():
    syms: str = input('Write independent variables to use separated with spaces\n→ ')
    expr: str = input('Write function with python syntax\n→ ')
    start: str = input('Write point to start separated with spaces\n→ ')

    try:
        f = parse_expr(expr)

        if not valid_start(start):
            print(f'\nResult → {find_max(f, syms, iterations=10000)}')
        else:
            point = list(map(float, re.split(r'\s', start)))

            print(f'\nResult → {find_max(f, syms, iterations=10000, point=point)}')
    except Exception as e:
        print(f'\nSomething went wrong (Check your input)')
        print(f'→ {e}')

def valid_start(start: str) -> bool:
    return re.match(r'^\d+(\s+\d+)+$', start) is not None


if __name__ == "__main__":
    main()
