from typing import List, Optional

from test_framework import generic_test

def f(s: str, i: int, n: int, prefix: str) -> Optional[List[str]]:
    assert n >= 0

    if i >= len(s) and n > 0:
        return None
    elif i < len(s) and n == 0:
        return None
    elif i >= len(s) and n == 0:
        return [prefix]

    r = []
    r.extend(f(s, i+1, n-1, f"{prefix}.{s[i]}") or [])
    if i+1 < len(s) and s[i] != "0" and int(s[i:i+2]) > 0:
        r.extend(f(s, i+2, n-1, f"{prefix}.{s[i:i+2]}") or [])
    if i+2 < len(s) and s[i] != "0" and s[i:i+2] != "00" and 1 < int(s[i:i+3]) < 256:
        r.extend(f(s, i+3, n-1, f"{prefix}.{s[i:i+3]}") or [])

    return r

def get_valid_ip_address(s: str) -> List[str]:
    ips = f(s, 0, 4, "") or []
    return list(map(lambda ip: ip[1:], ips)) # strip initial dot


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
