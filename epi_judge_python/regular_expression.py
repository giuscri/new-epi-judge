from test_framework import generic_test

def f(r: str, s: str, i: int, j: int) -> bool:
    if i < 0 and j < 0:
        return True
    elif i >= 0 and r[i] == "*" and j < 0:
        return f(r, s, i-2, j)
    elif i < 0 and j >= 0 or i >= 0 and j < 0: # either only the regex or only the text is exhausted
        return False

    assert i >= 0 and j >= 0

    if r[i] == s[j] or r[i] == ".":
        return f(r, s, i-1, j-1)
    elif r[i] == "*" and (r[i-1] == s[j] or r[i-1] == "."):
        zero_occ = f(r, s, i-2, j)
        oneplus_occ = f(r, s, i, j-1)
        return zero_occ or oneplus_occ
    elif r[i] == "*":
        return f(r, s, i-2, j)
    else:
        return False

def is_match(regex: str, s: str) -> bool:
    if not regex.startswith("^"):
        regex = "^.*" + regex
    if not regex.endswith("$"):
        regex = regex + ".*$"

    regex = regex[1:-1]
    return f(regex, s, len(regex)-1, len(s)-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('regular_expression.py',
                                       'regular_expression.tsv', is_match))
