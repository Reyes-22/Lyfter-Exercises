print('----------Calculator----------')
menu = '''These are the options you have to choose from:
      1. Sum
      2. Subtraction
      3. Multiplication
      4. Division
      5. Delete Result
      '''
print(menu)

current_number = 10
operation = int(input('Enter the number of the operation: '))

if operation < 1 or operation > 5:
    raise Exception("The option is not valid")
while operation != 6:
    number = int(input('Enter the number you want to calculate: '))
    try:
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
            case _:
                raise Exception("The option is not valid!!!!!!")

        print(f'The result is: {current_number}')
        print(menu)
        operation = int(input('Enter the number of the operation: '))

    except ValueError:
        raise Exception('Please enter a valid number')

print(current_number)
