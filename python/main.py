from classes import *
from os import system

list_of_songs : list[Song] = []

tours : list[Tour] = []

def main():
    load_from_file("python\songs.csv")
    load_from_file("python\\tour.csv")
    kilep = False
    while kilep == False:
        base_menu()
        option = choose_opton()
        kilep = sub_menu(option)
        if kilep == False:
            print()
            input("Continue...")

def load_from_file(filename:str):
    file = open(filename, "r", encoding="utf8")
    file.readline()
    match filename:
        case "python\songs.csv":
            for row in file:
                if row == "":
                    break
                else:
                    list_of_songs.append(Song(row))
        case "python\\tour.csv":
            for row in file:
                if row == "":
                    break
                else:
                   tours.append(Tour(row))
    file.close()

def base_menu():
    system("cls")
    print("BeatBazár")
    print()
    print("\t1. Get track length")
    print("\t2. Find longest song")
    print("\t3. Find shortest song")
    print("\t4. Get songs by genre")
    print("\t5. Add a new song")
    print("\t6. Search songs by artist")
    print("\t7. Delete a song")
    print("\t8. Sort songs")
    print("\t9. Update song information")
    print("\t0. Exit")
    print()

def choose_opton() -> int:
    while True:
        chosen :str = input("Choice: ")
        if chosen.isdigit() and int(chosen) <= 10 and int(chosen) >= 0:
            return int(chosen)

def sub_menu(choice: int) -> bool:
    system('cls')
    if choice == 1:
        get_track_length()
    elif choice == 2:
        longest_song()
    elif choice == 3:
        shortest_song()
    elif choice == 4:
        get_genre()
    elif choice == 5:
        add_song('python/songs.csv')
    elif choice == 6:
        search_by_artist()
    elif choice == 7:
        delete_song()
    elif choice == 8:
        sort_songs()
    elif choice == 9:
        update_song_info()
    elif choice == 0:
        return True
    return False

def get_track_length():
    answer = input('Please enter the name of the track: ')
    found = False
    for x in list_of_songs:
        if x.song_name == answer:
            print(f'The length of the track is: {x.minutes}:{x.seconds}, and it was made by {x.artist_name}')
            found = True
            break
    if not found:
        print('Track not found')

def longest_song():
    longest = 0
    for x in list_of_songs:
        if x.length_2 > longest:
            longest = x.length_2
    for x in list_of_songs:
        if x.length_2 == longest:
            print(f'The longest song is: {x.song_name} by {x.artist_name} with a length of {x.length}')

def shortest_song():
    shortest = 1000
    for x in list_of_songs:
        if x.length_2 < shortest:
            shortest = x.length_2
    for x in list_of_songs:
        if x.length_2 == shortest:
            print(f'The shortest song is: {x.song_name} by {x.artist_name} with a length of {x.length}')

def get_genre():
    genre = input('Please enter the genre: ')
    for x in list_of_songs:
        if x.genre == genre:
            print(f'{x.song_name} by {x.artist_name}')

def add_song(filename:str):
    artist = input('Please enter the artist: ')
    album = input('Please enter the album: ')
    song = input('Please enter the song: ')

    while True:
        track_number = input('Please enter the track number: ')
        if is_valid_track_number(track_number):
            break

    while True:
        genre = input('Please enter the genre: ')
        if is_valid_genre(genre):
            break
    
    while True:
        year = input('Please enter the year: ')
        if is_valid_year(year):
            break
    
    length = input('Please enter the length: ')
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f'{artist};{album};{song};{track_number};{genre};{year};{length}\n')
    file.close()

def is_valid_genre(genre: str) -> bool:
    existing_genres = ['rock', 'pop', 'hip-hop', 'jazz', 'country', 'classical']
    if genre.lower() in existing_genres:
        return True
    else:
        print('Invalid genre. Please try again.')
        return False
    
def is_valid_track_number(track_number: str) -> bool:
    if not track_number.isnumeric():
        print('Invalid track number. Please try again.')
        return False
    return True

def is_valid_genre(genre: str) -> bool:
    existing_genres = ['rock', 'pop', 'hip-hop', 'jazz', 'country', 'classical', 'phonk']
    if genre.lower() in existing_genres:
        return True
    else:
        print('Invalid genre. Please try again.')
        return False

def is_valid_year(year: str) -> bool:
    if not year.isdigit():
        print('Invalid year. Please try again.')
        return False
    year = int(year)
    if year > 2024 or year < 1900:
        print('Invalid year. Please try again.')
        return False
    else:  
        return True

def search_by_artist():
    artist = input('Please enter the artist name: ')
    found = False
    for song in list_of_songs:
        if song.artist_name.lower() == artist.lower():
            print(f'Song: {song.song_name}, Album: {song.album_name}, Track Number: {song.track_number}')
            found = True
    if not found:
        print('No songs found for the given artist.')

def delete_song():
    song_name = input('Please enter the name of the song you want to delete: ')
    found = False
    for x in list_of_songs:
        if x.song_name.lower() == song_name.lower():
            file = open('python\songs.csv', 'w', encoding='utf-8')
            list_of_songs.remove(x)
            file.write('Artist,Album,Song,Track Number,Genre,Year,Length\n')
            for y in list_of_songs:
                file.write(f'{y.artist_name};{y.album_name};{y.song_name};{y.track_number};{y.genre};{y.year};{y .length};\n')
            print(f'{x.song_name} by {x.artist_name} has been deleted.')
            found = True
            break
    if not found:
        print('Song not found.')

def sort_songs():
    sort_by = input('Please enter the attribute to sort by (song_name, artist_name, length, genre, year): ')
    if sort_by == 'song_name':
        list_of_songs.sort(key=lambda x: x.song_name)
    elif sort_by == 'artist_name':
        list_of_songs.sort(key=lambda x: x.artist_name)
    elif sort_by == 'length':
        list_of_songs.sort(key=lambda x: x.length)
    elif sort_by == 'genre':
        list_of_songs.sort(key=lambda x: x.genre)
    elif sort_by == 'year':
        list_of_songs.sort(key=lambda x: x.year)
    else:
        print('Invalid attribute. Please try again.')
        return
    print('Songs sorted successfully.')
    
    filename = input('Please enter the filename to save the sorted songs: ')
    with open(filename+".csv", 'w', encoding='utf-8') as file:
        file.write('Artist,Album,Song,Track Number,Genre,Year,Length\n')
        for song in list_of_songs:
            file.write(f'{song.artist_name},{song.album_name},{song.song_name},{song.track_number},{song.genre},{song.year},{song.length}\n')
    print('Sorted songs saved to file successfully.')

def is_valid_track_number(track_number: str) -> bool:
    if not track_number.isnumeric():
        print('Invalid track number. Please try again.')
        return False
    return True

def update_song_info():
    song_name = input('Please enter the name of the song you want to update: ')
    found = False
    for song in list_of_songs:
        if song.song_name.lower() == song_name.lower():
            print(f'Current information for {song.song_name}:')
            print(f'Artist: {song.artist_name}')
            print(f'Album: {song.album_name}')
            print(f'Track Number: {song.track_number}')
            print(f'Genre: {song.genre}')
            print(f'Year: {song.year}')
            print(f'Length: {song.length}')
            
            artist = input('Please enter the new artist: ')
            album = input('Please enter the new album: ')
            while True:
                track_number = input('Please enter the new track number: ')
                if not track_number.isdigit():
                    print('Invalid track number. Please try again.')
                else:
                    break
            
            while True:
                genre = input('Please enter the new genre: ')
                if is_valid_genre(genre):
                    break
                else:
                    print('Invalid genre. Please try again.')
            
            while True:
                year = input('Please enter the new year: ')
                if is_valid_year(year):
                    break
                else:
                    print('Invalid year. Please try again.')
            
            length = input('Please enter the new length: ')
            
            song.artist_name = artist
            song.album_name = album
            song.track_number = track_number
            song.genre = genre
            song.year = year
            song.length = length
            
            print(f'Song information updated for {song.song_name}.')
            found = True
            break
    
    if not found:
        print('Song not found.')
    else:
        with open('python/songs.csv', 'w', encoding='utf-8') as file:
            file.write('Artist,Album,Song,Track Number,Genre,Year,Length\n')
            for song in list_of_songs:
                    file.write(f'{song.artist_name};{song.album_name};{song.song_name};{song.track_number};{song.genre};{song.year};{song.length}\n')
        print('Updated songs saved to file successfully.')


main()

