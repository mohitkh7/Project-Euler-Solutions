"""
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters
The use of "and" when writing out numbers is in compliance with British usage.
"""


def number_to_text(num):
    """
    return textual representation of a given number
    for num 192 returns one hundred and ninety-two
    :param num: integer number in range 1 to 1000
    :return: string
    """
    # adding zero to make indexing compatible
    ans = ""
    hundreds_text_arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", ]
    tens_text_arr = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", ]
    unit_text_arr = hundreds_text_arr \
        + ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    hundreds_place = num // 100  # 7 in 786
    last_two_digit = num % 100  # 86 in 786
    tens_place = (num % 100) // 10  # 8 in 786
    unit_place = num % 10  # 6 in 786

    # corner case
    if num == 1000:
        return "one thousand"

    # 100 - 999
    if hundreds_place > 0:
        ans += hundreds_text_arr[hundreds_place] + " hundred"
        # not perfect hundred like 400
        if last_two_digit != 0:
            ans += " and "

    # 20 - 99
    if tens_place >= 2:
        ans += tens_text_arr[tens_place]
        unit_place = num % 10
        if unit_place != 0:
            ans += "-" + unit_text_arr[unit_place]
    # 1-19
    if last_two_digit > 0 and last_two_digit < 20:
        ans += unit_text_arr[last_two_digit]

    return ans


def count_char_in_text(num_str):
    """
    count character in string representation of number
    :param num_str: String
    :return: int
    """
    ans = 0
    for ch in num_str:
        if ch != " " and ch != '-':
            ans += 1
    return ans

if __name__ == "__main__":
    sum_of_char = 0
    for i in range(1, 1001):
        num_str = number_to_text(i)
        ch_count = count_char_in_text(num_str)
        sum_of_char += ch_count
        # print(num_str, " --> ", count_char_in_text(num_str))
    print(sum_of_char)
