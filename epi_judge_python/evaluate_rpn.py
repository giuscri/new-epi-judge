from test_framework import generic_test


def evaluate(expression: str) -> int:
    stack = []

    for token in expression.split(","):
        if token in "+-*":
            b, a = stack.pop(), stack.pop()
            stack.append(eval(f"{a} {token} {b}"))
        elif token == "/":
            b, a = stack.pop(), stack.pop()
            stack.append(eval(f"{a} // {b}"))
        else:
            stack.append(token)

    return int(stack.pop())


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
