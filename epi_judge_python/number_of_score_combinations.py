from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    dp = [0 for _ in range(final_score+1)]
    dp[0] = 1
    for ps in individual_play_scores:
        for j in range(ps, final_score+1):
            dp[j] += dp[j-ps]
    return dp[final_score]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
