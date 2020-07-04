from test_framework import generic_test


def power(x: float, y: int) -> float:
    if y == 0:
        return 1.0

    if y < 0:
        y *= -1
        x = 1 / x

    r = 1.0
    while y > 0:
        if y & 1 == 1:
            r *= x

        x *= x
        y >>= 1

    return r


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
