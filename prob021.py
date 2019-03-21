"""
Amicable numbers

Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import math


def get_divisors(n):
    """
    return set of proper divisors i.e. number less than n which divide evenly into n
    :param n: an integer value
    :return: set of integers corresponding to divisors of n
    """
    ans_arr = [1, ]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans_arr.append(i)
            # adding co-product
            ans_arr.append(n // i)
    return set(ans_arr)


def sum_of_amicable_numbers(limit=100):
    # ambicale pairs will be appended in this list
    list_of_amicable_numbers = []
    # dictionary holding numbers as key and sum of its divisors as value
    dict_for_sum_of_divisors = {}
    for i in range(1, 10000):
        # getting sum of divisor for given i
        current_sum_of_divisor = sum(get_divisors(i))
        # adding it to dictionary
        dict_for_sum_of_divisors[i] = current_sum_of_divisor
        # will check only if value exist in dictionary
        if current_sum_of_divisor < i:
            # check for amicable pair
            if dict_for_sum_of_divisors[current_sum_of_divisor] == i:
                list_of_amicable_numbers.append(current_sum_of_divisor)
                list_of_amicable_numbers.append(i)
    print(list_of_amicable_numbers)
    return sum(list_of_amicable_numbers)


if __name__ == "__main__":
    val = sum_of_amicable_numbers(10000)
    print(val)
