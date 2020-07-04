from test_framework import generic_test


def reverse(x: int) -> int:
    negative_input = x < 0
    if negative_input:
        x *= -1

    r = 0
    while x > 0:
        r *= 10
        r += x % 10
        x //= 10

    if negative_input:
        r *= -1

    return r

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
