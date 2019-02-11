"""
Largest palindrome product

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def reverse_number(n):
    """
    reverse a number
    for input 1234 returns 4321
    """
    ans = 0
    while n:
        ans = (ans * 10) + (n % 10)
        n = n // 10
    return ans


def is_palindrome(n):
    """
    Check whether integer number is palindrome ( reads the same both ways)
    """
    if n == reverse_number(n):
        return True
    return False


def largest_palindrome(digits=3):
    upper_limit = (10**digits) - 1  # 999
    lower_limit = 10**(digits - 1)  # 100
    largest = 0

    i = upper_limit
    while i >= lower_limit:
        j = i
        # As all further products will be less than largest
        if i * j < largest:
            break
        while j >= lower_limit:
            if is_palindrome(i * j) and (i * j) > largest:
                largest = i * j
            j -= 1
        i -= 1

    return largest

print(largest_palindrome())
