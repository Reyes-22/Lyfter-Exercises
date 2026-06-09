import random


def is_prime(number):
    # the number must be greater than 1
    if number <= 1:
        return False
    # we iterate from 2 to the number -1
    for i in range(2, number):
        # if one of the numbers reach 0, the number is not prime
        if number % i == 0:
            return False
    # otherwise the number is prime
    return True


def get_prime_numbers(list_of_numbers):
    new_list = []
    for i in range(len(list_of_numbers)):
        if is_prime(list_of_numbers[i]):
            new_list.append(list_of_numbers[i])
    return new_list


list_of_numbers = []
for i in range(25):
    numbers = random.randint(0, 50)
    list_of_numbers.append(numbers)

print(list_of_numbers)
print(get_prime_numbers(list_of_numbers))
