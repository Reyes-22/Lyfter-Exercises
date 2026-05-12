def get_string(my_string):
    my_list = my_string.split('-')
    my_list.sort(key=str.lower)
    my_string = '-'.join(my_list)
    return print(my_string)


my_string = 'Zoo-Bryan-Python-Code-Learning-Reyes-Web-App-Car'
get_string(my_string)
