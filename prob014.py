"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
LIMIT = 10**6  # 1000000
dict_num_to_seq_len = {
    1: 1,
    2: 2,
}


def count_sequence_length(num):
    length = 0
    traversed_num_arr = []
    while num != 1:
        if num in dict_num_to_seq_len.keys():
            length += dict_num_to_seq_len[num]
            break
        traversed_num_arr.append(num)
        if num % 2 == 0:
            num = num // 2
        else:
            num = (3 * num) + 1
        length += 1
    # pushing in dictionary
    for index, number in enumerate(traversed_num_arr):
        dict_num_to_seq_len[number] = length - index

    return length

max_length = 0
num_generating_max_length = -1
# looping from 500000 because every smaller number has mapping to 2N
for i in range(500000, LIMIT):
    seq_len = count_sequence_length(i)
    if seq_len > max_length:
        max_length = seq_len
        num_generating_max_length = i

print(num_generating_max_length)
