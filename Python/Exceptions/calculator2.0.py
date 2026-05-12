def validate_option(option):
    if option < 1 or option > 6:
        raise Exception("The option is not valid")


print('----------Calculator----------')
menu = '''These are the options you have to choose from:
1. Sum
2. Subtraction
3. Multiplication
4. Division
5. Delete Result
6. Exit
'''
print(menu)

current_number = 10
operation = int(input('Enter the number of the operation: '))

validate_option(operation)

while operation != 6:
    try:
        number = int(input('Enter the number you want to calculate: '))
        match operation:
            case 1:
                current_number += number
            case 2:
                current_number -= number
            case 3:
                current_number *= number
            case 4:
                current_number /= number
            case 5:
                current_number = 0

        print(f'The result is: {current_number}')
        print(menu)
        operation = int(input('Enter the number of the operation: '))
        validate_option(operation)

    except ValueError:
        print('Please enter a valid number')

print('The execution has finished')
