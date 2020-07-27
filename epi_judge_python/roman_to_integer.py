from test_framework import generic_test

M = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def roman_to_integer(s: str) -> int:
    prev = None
    n = 0
    for c in s:
        curr = M[c]
        if prev is not None and prev < curr:
            n = n - prev + (curr - prev)
        else:
            n += curr

        prev = curr

    return n


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
