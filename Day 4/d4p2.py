from itertools import groupby

number_of_passwords = 0
for i in range(245318, 765747 + 1):
    num_str = str(i)
    num_list = [int(char) for char in num_str]

    repeating_digit = False
    descending_number = False

    j = 0
    # Length of number is always 6
    while j < 5 and not descending_number:
        if num_list[j] == num_list[j + 1]:
            repeating_digit = True
        elif num_list[j] > num_list[j + 1]:
            descending_number = True
        j += 1
    if repeating_digit and not descending_number:
        flag = False
        grouped_list = [len(list(x)) for _, x in groupby(num_list)]
        # Number repeats twice and only twice
        if 2 in grouped_list:
            number_of_passwords += 1

print(number_of_passwords)
