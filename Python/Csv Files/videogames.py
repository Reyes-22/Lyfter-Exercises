import csv
data = []
headers = ('Name', 'Type', 'Developer', 'Classification')


def add_videogames():
    videogames_data = []
    videogames = int(input('How many videogames do you wanna enter?'))

    for i in range(videogames):
        videogame = {"Name": input("Enter game's name: "),
                     "Type": input("Enter game's type: "),
                     "Developer": input("Enter game's developer: "),
                     "Classification": input("Enter game's classification: ")
                     }

        videogames_data.append(videogame)
        print('\n')

    return videogames_data


data.extend(add_videogames())


with open('videogames.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)


# if we need to add a new video game, we need to use with open, but with the mode "a" append.
