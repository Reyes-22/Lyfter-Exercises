import json


def add_new_pokemon():
    pokemon_data = []
    print("Enter pokemon's characteristics >>>")

    pokemon = {'name': {"english": input("Enter pokemon's name: ")},
               'level': int(input("Enter pokemon's level: ")),
               'type': input("Enter pokemon's type: "),
               'base': {
        'Attack': int(input("Enter pokemon's attack: ")),
        'Defense':  int(input("Enter pokemon's defense: ")),
        'HP':  int(input("Enter pokemon's HP: ")),
        'SP. Attack':  int(input("Enter pokemon's SP. Attack: ")),
        'SP. Defense':  int(input("Enter pokemon's SP. Defense: ")),
        'SP. Speed':  int(input("Enter pokemon's Speed: ")),
    }
    }

    pokemon_data.append(pokemon)

    return pokemon_data


def add_pokemon(file, new_pokemon):
    with open(file, "r", encoding="utf-8") as f:
        list_of_pokemon = json.load(f)

    list_of_pokemon.extend(new_pokemon)

    with open(file, "w", encoding="utf-8") as f:
        json.dump(list_of_pokemon, f, indent=4, ensure_ascii=False)


add_pokemon('pokemon.json', add_new_pokemon())
