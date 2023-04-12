

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(n):
    for i in range(9, n + 1):
        if is_prime(i):
            print(i)
