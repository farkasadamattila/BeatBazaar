from adam import Song

list_of_songs: list[Song] = []

def main():
    read_from_file('songs.csv')
    get_track_length()
    longest_song()
    shortest_song()


def read_from_file(file_name: str) -> None:
    with open(file_name, 'r') as file:
        file.readline()
        for row in file:
            list_of_songs.append(Song(row))
    file.close()

def get_track_length():
    answer = input('Please enter the name of the track: ')
    found = False
    for x in list_of_songs:
        if x.song_name == answer:
            print(f'The length of the track is: {x.length}, and it was made by {x.artist_name}')
            found = True
            break
    if not found:
        print('Track not found')

def longest_song():
    longest = 0
    for x in list_of_songs:
        if x.length > longest:
            longest = x.length
    for x in list_of_songs:
        if x.length == longest:
            print(f'The longest song is: {x.song_name} by {x.artist_name} with a length of {x.length}')

def shortest_song():
    shortest = 1000
    for x in list_of_songs:
        if x.length < shortest:
            shortest = x.length
    for x in list_of_songs:
        if x.length == shortest:
            print(f'The shortest song is: {x.song_name} by {x.artist_name} with a length of {x.length}')


main()