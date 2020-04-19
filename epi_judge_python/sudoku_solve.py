import copy
import functools
import math
from typing import List, Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from copy import deepcopy

def valid(b: List[List[int]]):
    n = len(b)
    for i in range(n):
        s, nzeros = set(), 0
        for j in range(n):
            if b[i][j] != 0:
                s.add(b[i][j])
            else:
                nzeros += 1

        if nzeros + len(s) < n:
            return False

    for j in range(n):
        s, nzeros = set(), 0
        for i in range(n):
            if b[i][j] != 0:
                s.add(b[i][j])
            else:
                nzeros += 1

        if nzeros + len(s) < n:
            return False
   
    for i in range(0, n, 3):
        for j in range(0, n, 3):
            s, nzeros = set(), 0
            for ii in range(i, i+3):
                for jj in range(j, j+3):
                    if b[ii][jj] != 0:
                        s.add(b[ii][jj])
                    else:
                        nzeros += 1
            
            if nzeros + len(s) < n:
                return False

    return True

def f(b: List[List[int]], i: int, j: int) -> Optional[List[List[int]]]:
    n, m = len(b), len(b[0])
    if n != m:
        raise RuntimeError("n, m are not equal")

    if (i, j) == (n, 0):
        return b

    nexti, nextj = i, j+1
    if j+1 >= n:
        nexti, nextj = i+1, 0

    r = None
    if b[i][j] == 0:
        for x in range(1, n+1):
            bb = deepcopy(b)
            bb[i][j] = x
            if not valid(bb):
                continue
            else:
                r = f(bb, nexti, nextj)
                if r:
                    return r
    else:
        r = f(b, nexti, nextj)

    return r


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    b = f(partial_assignment, 0, 0)
    if not b:
        return False
    else:
        partial_assignment[:] = b[:]
        return True

def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
