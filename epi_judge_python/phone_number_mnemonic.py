from typing import List

from test_framework import generic_test, test_utils

M = {
    "0": "0",
    "1": "1",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ"
}

def phone_mnemonic(phone_number: str) -> List[str]:
    if not phone_number:
        return [""]

    n = phone_number[0]
    l = phone_mnemonic(phone_number[1:])
    ll = []
    for c in M[n]:
        for s in l:
            ll.append(c + s)
    return ll


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
