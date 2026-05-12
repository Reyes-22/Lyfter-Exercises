def show_menu():
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


def enter_option():
    while True:
        try:
            option = int(input('Enter the number of the operation: '))
            if option > 0 and option <= 6:
                return option
            else:
                print("Invalid number! Try again")
        except ValueError:
            print('You must enter a valid number!')


def sum_number(a, b):
    return a + b


def subtract_number(a, b):
    return a - b


def multiply_number(a, b):
    return a * b


def divide_number(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("A number can't be divided by 0. Try Again")
        return a


def delete_result(number):
    number = 0
    return number


def main():
    show_menu()

    current_number = 0

    operation = enter_option()

    while operation != 6:
        try:
            number = int(input('Enter the number you want to calculate: '))
            match operation:
                case 1:
                    new_number = sum_number(current_number, number)
                case 2:
                    new_number = subtract_number(current_number, number)
                case 3:
                    new_number = multiply_number(current_number, number)
                case 4:
                    new_number = divide_number(current_number, number)
                case 5:
                    new_number = delete_result(current_number)

            print(f'The result is: {new_number}')
            current_number = new_number
            show_menu()
            operation = enter_option()
        except ValueError:
            print('You must enter a valid number!')
            show_menu()


main()
