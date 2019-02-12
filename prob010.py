"""
Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
limit = 2000000


def all_prime_upto_n(num_limit):
    """
    return list of all prime number upto n
    """
    is_prime = [True for i in range(num_limit + 1)]
    p = 2
    while (p * p) <= num_limit:
        if is_prime[p]:
            # mark all multiple of p as non-prime
            for j in range(p * 2, num_limit + 1, p):
                is_prime[j] = False
        p += 1

    # generating list of prime number
    list_of_prime_number = []
    for i in range(2, num_limit + 1):
        if is_prime[i]:
            list_of_prime_number.append(i)

    return list_of_prime_number

print(sum(all_prime_upto_n(limit)))
