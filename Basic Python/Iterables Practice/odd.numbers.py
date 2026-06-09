my_list = [5, 3, 2, 4, 9, 8, 6, 45, 5, 2, 1, 44, 65, 22, 32, 14, 17]

for i in range(len(my_list)-1, - 1, - 1):
    if my_list[i] % 2 != 0:
        my_list.pop(i)

print(my_list)
