"""Names scores

Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
# opening and reading content of file
file = open("p022_names.txt", "r")
content = file.read()

"""
file content format
"MARY","PATRICIA","LINDA",........
"""

# removing reduntant double quotes
cleaned_content = content.replace('"', '')

# convert string to arr
name_arr = cleaned_content.split(",")

# sort array
name_arr.sort()

ans = 0
for i, name in enumerate(name_arr):
    alpha_value = 0
    for ch in name:
        alpha_value += ord(ch) - 64  # Because A=65, B=66 and so on
    ans += (i + 1) * alpha_value
print(ans)
