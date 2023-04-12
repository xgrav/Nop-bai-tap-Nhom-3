

import pytest

from src.source import print_primes

def test_get_prime_numbers():
    assert print_primes(9) == []
    assert print_primes(10) == [2, 3, 5, 7]
    assert print_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert print_primes(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert print_primes(2) == []
    assert print_primes(3) == [2]
