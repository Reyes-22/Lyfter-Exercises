import random

list_of_numbers = []

for i in range(10):
    number = random.randint(1, 15)
    list_of_numbers.append(number)

smallest = list_of_numbers[0]

for i in range(len(list_of_numbers)):
    if list_of_numbers[i] < smallest:
        smallest = list_of_numbers[i]

print(list_of_numbers)
print(f'The smallest number is {smallest}.')
