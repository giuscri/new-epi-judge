from test_framework import generic_test

M = "0123456789ABCDEF"

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    negative = num_as_string.startswith("-")
    if negative:
        num_as_string = num_as_string[1:]

    n = 0
    for digit in num_as_string:
        n = n * b1 + int(digit, base=b1)

    result = ""

    while True:
        result = M[n % b2] + result
        n //= b2

        if n < 1:
            break

    if negative:
        result = "-" + result

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
