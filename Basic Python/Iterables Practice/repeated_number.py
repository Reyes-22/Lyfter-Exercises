'''Create a program that counts how many times a 
specific number appears in a list. Ask the user 
for a list of numbers and another number to search for.'''
print('ENTER 10 NUMBERS!!!')
my_list = []
counter = 1

while counter <= 10:
    number = int(input('Enter a number:'))
    my_list.append(number)

    counter += 1

number = 0
number_to_search = int(input('Enter the number you want to search for: '))
for i in range(len(my_list)):
    if my_list[i] == number_to_search:
        number += 1
    else:
        continue

print(f'The number {number_to_search} appears {number} times.')
