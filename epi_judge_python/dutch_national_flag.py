import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

def _partition(A, start, stop, discriminator):
  i, j = start, stop-1
  while i <= j:
    while i < stop and discriminator(A[i]):
      i += 1
    while j >= start and not discriminator(A[j]):
      j -= 1

    if j <= i:
      break
    else:
      A[i], A[j] = A[j], A[i]
      i += 1
      j -= 1

  return A[:i], A[i:], i

def partition1(A, i, j, pivot):
  """Partitions A[i:j] into < pivot, >= pivot"""

  discriminator = lambda x, pivot=pivot: x < pivot
  return _partition(A, i, j, discriminator)

def partition2(A, i, j, pivot):
  """Partitions A[i:j] into == pivot, > pivot"""

  discriminator = lambda x, pivot=pivot: x == pivot
  return _partition(A, i, j, discriminator)

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
  pivot = A[pivot_index]
  _, _, i = partition1(A, 0, len(A), pivot)
  _, _, _ = partition2(A, i, len(A), pivot)


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
