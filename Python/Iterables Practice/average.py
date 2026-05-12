import random

list_of_numbers = []

for i in range(10):
    number = random.randint(50, 100)
    list_of_numbers.append(number)

total = 0
for i in range(len(list_of_numbers)):
    total = total + list_of_numbers[i]

average = total / 10
new_list = []
for i in range(len(list_of_numbers)):
    if average < list_of_numbers[i]:
        new_list.append(list_of_numbers[i])

print(list_of_numbers)
print(average)
print(new_list)
