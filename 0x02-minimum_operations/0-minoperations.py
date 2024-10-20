#!/usr/bin/python3
""" Minmum opration"""


def minOperations(n: int) -> int:
    """Perform min operation"""
    if n <= 1:
        return 0
    total_oprations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            n /= divisor
            total_oprations += divisor
        divisor += 1
    return total_oprations
