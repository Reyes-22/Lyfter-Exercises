def sum_numbers():
    first_number = 7
    second_number = 10
    if first_number < second_number:
        print(f'The number {second_number} is bigger than the {first_number}.')
    else:
        print(
            f'The number {second_number} is smaller than the {first_number}.')


print(first_name)

age = 29


def change_age():
    # global age
    if age < 30:
        age = 30
    # Python treats age as a local variable within the function, and that's why it fails.
    print(age)


change_age()
