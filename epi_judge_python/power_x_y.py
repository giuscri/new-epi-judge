from test_framework import generic_test


def power(x: float, y: int) -> float:
    if y == 0:
        return 1.0

    if y < 0:
        y *= -1
        x = 1 / x

    p = power(x, y // 2)
    if y & 1 == 0:
        return p * p
    else:
        return x * p * p


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
