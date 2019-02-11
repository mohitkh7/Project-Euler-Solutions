"""
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def is_prime(n):
    if n == 0 or n == 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i += 6
    return True

nth = 10001
ith = 0
j = 2
while ith != nth:
    if is_prime(j):
        ith += 1
    j += 1

print(j - 1)
