def change_string(my_string):
    reverse_string = ''
    for i in range(len(my_string) - 1, -1, -1):
        reverse_string += my_string[i]
    return reverse_string


print(change_string('My name is Bryan.'))
