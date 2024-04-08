from classes import Song, Tour
from os import system
list_of_songs: list[Song] = []
tours: list[Tour] = []

def main():
    load_from_file("python/songs.csv")
    load_from_file("python/tour.csv")
    kilep = False
    while not kilep:
        base_menu()
        option = choose_option()
        kilep = sub_menu(option)
        if not kilep:
            print()
            input("Continue...")

def load_from_file(filename: str):
    with open(filename, "r", encoding="utf8") as file:
        file.readline()
        if filename == "python/songs.csv":
            for row in file:
                if row == "":
                    break
                else:
                    list_of_songs.append(Song(row))
        elif filename == "python/tour.csv":
            for row in file:
                if row == "":
                    break
                else:
                    tours.append(Tour(row))

def base_menu():
    system("cls")
    print('''
    __________               __    __________                                     
    \______   \ ____ _____ _/  |_  \______   \_____  _____________  _____ _______ 
    |    |  _// __ \\\\__  \\\   __\  |    |  _/\__  \ \___   /\__  \ \__  \\\_  __ \\\\
    |    |   \  ___/ / __ \|  |    |    |   \ / __ \_/    /  / __ \_/ __ \|  | \/
    |______  /\___  >____  /__|    |______  /(____  /_____ \(____  (____  /__|   
            \/     \/     \/               \/      \/      \/     \/     \/       
        ''')
    print("Welcome to the music database")
    print("Main menu:")
    print("\t1. Play song")
    print("\t2. Get track length")
    print("\t3. Find longest song")
    print("\t4. Find shortest song")
    print("\t5. Get songs by genre")
    print("\t6. Add a new song")
    print("\t7. Search songs by artist")
    print("\t8. Delete a song")
    print("\t9. Sort songs")
    print("\t10. Update song information")
    print("\t11. Get track number")
    print("\t12. Clear browser history")
    print("\t13. Show browser history")
    print("\t0. Exit")
    

def choose_option() -> int:
    while True:
        chosen = input("Choice: ")
        if chosen.isdigit() and 0 <= int(chosen) <= 12:
            return int(chosen)

def sub_menu(choice: int) -> bool:
    system('cls')
    if choice == 1:
        play_song()
    elif choice == 2:
        get_track_length()
    elif choice == 3:
        longest_song()
    elif choice == 4:
        shortest_song()
    elif choice == 5:
        get_genre()
    elif choice == 6:
        add_song('python/songs.csv')
    elif choice == 7:
        search_by_artist()
    elif choice == 8:
        delete_song()
    elif choice == 9:
        sort_songs()
    elif choice == 10:
        update_song_info()
    elif choice == 0:
        print("Goodbye!")
        return True
    elif choice == 11:
        get_track_number()
    elif choice == 12:
        clear_recent_songs()
    elif choice == 13:
        show_recent_songs()
    return False

def play_song():
    song_name = input('Please enter the name of the song you want to play: ')
    found = False
    for song in list_of_songs:
        if song.song_name.lower() == song_name.lower():
            print(f'Playing {song.song_name} by {song.artist_name}')
            found = True
            break
    if not found:
        print('Song not found.')

def get_track_length():
    answer = input('Please enter the name of the track: ')
    found = False
    for song in list_of_songs:
        if song.song_name == answer:
            print(f'The length of the track is: {song.minutes}:{song.seconds}, and it was made by {song.artist_name}')
            add_to_recent_songs(song)
            found = True
            break
    if not found:
        print('Track not found')

def longest_song():
    longest = 0
    for song in list_of_songs:
        if song.length_2 > longest:
            longest = song.length_2
    for song in list_of_songs:
        if song.length_2 == longest:
            print(f'The longest song is: {song.song_name} by {song.artist_name} with a length of {song.length}')
            add_to_recent_songs(song)

def shortest_song():
    shortest = 1000
    for song in list_of_songs:
        if song.length_2 < shortest:
            shortest = song.length_2
    for song in list_of_songs:
        if song.length_2 == shortest:
            print(f'The shortest song is: {song.song_name} by {song.artist_name} with a length of {song.length}')
            add_to_recent_songs(song)

def add_song(filename: str):
    artist = input('Please enter the artist: ')
    album = input('Please enter the album: ')
    song = input('Please enter the song: ')

    while True:
        track_number = input('Please enter the track number: ')
        if is_valid_track_number(track_number):
            break

    while True:
        genre = input('Please enter the genre: ')
        if not is_valid_genre(genre):
            print('Invalid genre. Please try again.')
            continue
        break
    
    while True:
        year = input('Please enter the year: ')
        if is_valid_year(year):
            break
    length = input('Please enter the length: ')
    
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f'{artist};{album};{song};{track_number};{genre};{year};{length}\n')
    file.close()
    load_from_file(filename)
    for song in list_of_songs:
        added_song = song
    add_to_recent_songs(added_song)

def get_genre():
    existing_genres = ['Rock', 'Pop', 'Hip-Hop', 'Grunge', 'Metal', 'Techno', 'Jazz', 'Phonk', 'Country', 'Classical']
    while True:
        genre = input('Please enter the genre: ')
        if genre not in existing_genres:
            print('Invalid genre. Please try again.')
        else:  
            for song in list_of_songs:
                if song.genre.lower() == genre.lower():
                    print(f'Song: {song.song_name}, Artist: {song.artist_name}')
                    add_to_recent_songs(song)
            break

def is_valid_genre(genre: str) -> bool:
    existing_genres = ['Rock', 'Pop', 'Hip-Hop', 'Grunge', 'Metal', 'Techno', 'Jazz', 'Phonk', 'Country', 'Classical']
    if genre not in existing_genres:
        return False
    return True

def is_valid_track_number(track_number: str) -> bool:
    if not track_number.isnumeric():
        print('Invalid track number. Please try again.')
        return False
    return True

def is_valid_year(year: str) -> bool:
    if not year.isdigit():
        print('Invalid year. Please try again.')
        return False
    year = int(year)
    if year > 2024 or year < 1900:
        print('Invalid year. Please try again.')
        return False
    return True

def search_by_artist():
    artist = input('Please enter the artist name: ')
    found = False
    for song in list_of_songs:
        if song.artist_name.lower() == artist.lower():
            print(f'Song: {song.song_name}, Album: {song.album_name}, Track Number: {song.track_number}')
            found = True
            add_to_recent_songs(song)
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
    with open(filename + ".csv", 'w', encoding='utf-8') as file:
        file.write('Artist,Album,Song,Track Number,Genre,Year,Length\n')
        for song in list_of_songs:
            file.write(f'{song.artist_name},{song.album_name},{song.song_name},{song.track_number},{song.genre},{song.year},{song.length}\n')
    print('Sorted songs saved to file successfully.')

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
            add_to_recent_songs(song)
            break
    
    if not found:
        print('Song not found.')
    else:
        with open('python/songs.csv', 'w', encoding='utf-8') as file:
            file.write('Artist,Album,Song,Track Number,Genre,Year,Length\n')
            for song in list_of_songs:
                    file.write(f'{song.artist_name};{song.album_name};{song.song_name};{song.track_number};{song.genre};{song.year};{song.length}\n')
        print('Updated songs saved to file successfully.')

def get_track_number():
    given_song = input('Please enter the desired song: ')
    found = False
    for song in list_of_songs:
        if song.song_name == given_song:
            print(f'\nTrack number: {song.track_number}\nArtist: {song.artist_name}\nAlbum: {song.album_name}')
            found = True
            add_to_recent_songs(song)
    if not found:
        print('No songs found for the given track number.')

def add_to_recent_songs(song:Song):
    file = open("python/recent_songs.csv", "a", encoding="utf8")
    file.write(f"{song.artist_name};{song.album_name};{song.song_name};{song.track_number};{song.genre};{song.year};{song.length}\n")
    file.close()

def clear_recent_songs():
    file = open("python/recent_songs.csv", "w", encoding="utf8")
    file.write("Artist;Album;Song;Track Number;Genre;Year;Length\n")
    print("History cleared")
    file.close()

def show_recent_songs():
    system("cls")
    file = open("python/recent_songs.csv", "r", encoding="utf8")
    file.readline()
    recent_songs : list[Song] = []
    for song in file:
        recent_songs.append(Song(song))
    for song in recent_songs:
        print(f"Artist's name: {song.artist_name}, Album's name: {song.album_name}, Song's name: {song.song_name}, Track number: {song.track_number}, Genre: {song.genre}, Relased in: {song.year}, Lenght: {song.length}")
    file.close()
main()
