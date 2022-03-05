from gradient_descent import follow_gradient

def main():
    minimize = input('To minimize input (-) otherwise maximize\n→ ') == '-'
    variables = input('Write independent variables to use separated with spaces\n→ ')
    f = input('Write function with python syntax\n→ ')
    start = input('Write point to start separated with spaces\nprefix with "rand" to indicate a range of random values)\n→ ')
    point, random = parse_point(start)

    starting_point, *result = follow_gradient(f, variables, point=point, random=random, minimize=minimize)

    print()
    print(f'Starting at point → {starting_point}')
    print(f'Result → {result}')


def parse_point(point: str) -> tuple[list[float], bool]:
    start: int = 1 if 'rand' in point else 0

    return (list(map(float, point.split(' ')[start:])), start == 1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f'\nSomething went wrong (Check your input)')
