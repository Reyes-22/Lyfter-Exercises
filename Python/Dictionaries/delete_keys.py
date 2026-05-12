my_dictionary = {
    'Name': 'Bryan',
    'Last Name': 'Reyes',
    'Age': 29,
    'Email': 'bjreyes962010@hotmail.com',
    'Country': 'Costa Rica',
}

keys_to_delete = ['Email', 'Country']

for key in keys_to_delete:
    my_dictionary.pop(key, None)

print(my_dictionary)
