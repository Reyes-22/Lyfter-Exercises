print("Enter 10 numbers!")

my_list = []
counter = 1


while counter <= 10:
    number = int(input('Enter a number:'))
    my_list.append(number)

    counter += 1

print(my_list)
print(f'The largest number was {max(my_list)}')
