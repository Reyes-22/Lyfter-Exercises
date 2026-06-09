def read_songs(path):
    with open(path, 'r', encoding='utf-8') as file:
        songs = file.readlines()
        return songs


def sort_songs_file(songs, output_path):
    songs = [song.strip() for song in songs if song.strip()]

    songs.sort()

    with open(output_path, 'w', encoding='utf-8') as file:
        for song in songs:
            file.write(song + "\n")


songs = read_songs(
    "C:\\Users\\bjrey\\Desktop\\Lyfter\\Python\\File Management\\Songs.txt")

sort_songs_file(
    songs, "C:\\Users\\bjrey\\Desktop\\Lyfter\\Python\\File Management\\Songs_sorted.txt")
