list_of_words = []

counter = 1

while counter <= 5:
    words = input('Enter a word: ')
    list_of_words.append(words)
    counter += 1

new_list = []
for i in range(len(list_of_words)):
    if len(list_of_words[i]) > 4:
        new_list.append(list_of_words[i])

print(new_list)
