from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    stack = []

    for paren in s:
        if paren in "([{":
            stack.append(paren)
        elif paren in ")]}" and len(stack) > 0:
            popped_paren = stack.pop()
            if popped_paren + paren == "()":
                pass
            elif popped_paren + paren == "[]":
                pass
            elif popped_paren + paren == "{}":
                pass
            else:
                return False
        else:
            return False

    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
