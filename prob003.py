"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def sqrt(n):
    """
    Calculate floor square root (rounded to nearest integer) of positive integer
    Based on babylonian method
    for n = 11 returns 3
    """
    x = n
    y = 1
    accuracy = 0.1
    while (x - y) > accuracy:
        x = (x + y) / 2
        y = n / x
    return math.floor(x)

target_number = 600851475143

prime_factors = []
# dividing by 2 untill it doesn't become odd
while target_number % 2 == 0:
    target_number = target_number // 2
    prime_factors.append(2)

for i in range(3, sqrt(target_number) + 1, 2):
    while target_number % i == 0:
        target_number = target_number // i
        prime_factors.append(i)
    if target_number == 1:
        break

if target_number != 1:
    prime_factors.append(target_number)
print(prime_factors[-1])
