"""
Factorial digit sum

Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def multiply(st, n):
    """
    Multiply two very large numbers
    st : String
    n: Integer number
    return: String
    """
    product = ""
    carry = 0
    for ch_num in st[::-1]:
        num = int(ch_num)
        curr_pro = (num * n) + carry
        base = curr_pro % 10
        carry = curr_pro // 10
        product = str(base) + product

    if carry != 0:
        product = str(carry) + product

    return product


def sum_of_digits_of_factorial(n):
    fact = "1"
    # counting factorial of 100
    for n in range(2, n + 1):
        fact = multiply(fact, n)

    print(fact)
    # taking digit sum
    ans = 0
    for digit in fact:
        ans += int(digit)
    return ans


if __name__ == "__main__":
    val = sum_of_digits_of_factorial(100)
    print(val)
