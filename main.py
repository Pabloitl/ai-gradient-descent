from sympy import (
    symbols,
    lambdify,
    derive_by_array,
    Matrix,
    parse_expr
)


def find_max(f, syms, h: float = 1e-3, eps: float = 1e-3, iterations: int = 100):
    variables = symbols(syms)
    grad_f = lambdify(variables, derive_by_array(f, variables))
    result = Matrix([1] * len(variables))

    for _ in range(iterations):
        grad_value = Matrix(grad_f(*result))

        if grad_value.norm() < eps:
            break

        result += grad_value * h

    return (result[0], result[1])


def main():
    syms: str = input('Write independent variables to use separated with spaces\n→ ')
    expr: str = input('Write function with python syntax\n→ ')

    try:
        f = parse_expr(expr)

        print(f'\nResult → {find_max(f, syms, iterations=10000)}')
    except Exception as _:
        print(f'\nCannot parse → "{expr}" (Check your input)')

if __name__ == "__main__":
    main()
