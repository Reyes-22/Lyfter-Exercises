import random


def sum_numbers(list_of_numbers):
    total = 0
    for i in range(len(list_of_numbers)):
        number = list_of_numbers[i]
        total += number
    return total


print(sum_numbers([4, 6, 2, 29]))
