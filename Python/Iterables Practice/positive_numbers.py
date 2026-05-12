import random

list_of_numbers = []

for i in range(10):
    number = random.randint(-15, 15)
    list_of_numbers.append(number)

number = True
for i in range(len(list_of_numbers)):
    if list_of_numbers[i] < 0 or list_of_numbers[i] == 0:
        number = False

if number == True:
    print('All numbers are positive.')
else:
    print('There is at least a negative number or a zero.')

print(list_of_numbers)
