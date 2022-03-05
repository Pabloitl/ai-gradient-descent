from math import ceil, floor
from random import randrange

from sympy import Matrix, derive_by_array, lambdify, parse_expr, symbols


def follow_gradient(
        function: str,
        syms: str,
        point: list[float],
        h: float           = 1e-3,
        eps: float         = 1e-3,
        iterations: int    = 10000,
        minimize: bool     = True,
        random: bool       = False
    ):
    f         = parse_expr(function)
    variables = symbols(syms, seq=True)
    grad_f    = lambdify(variables, derive_by_array(f, variables))
    result    = Matrix([randrange(floor(point[0]), ceil(point[1])) if random else point[i] for i in range(len(variables))])
    start_point = result
    change_sign = -1 if minimize else 1

    for _ in range(iterations):
        gradient = Matrix(grad_f(*result))

        if gradient.norm() < eps:
            break

        result += gradient * h * change_sign

    return start_point.tolist(), *result
