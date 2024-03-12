from menu_functions import *

def sub_menu(option: int):
    match option:
        case 1:
            name = input("Keresés név alapján: ")
            seached_song = search_by_name(name)
            print(f"Készítő: {seached_song[0]}")
            print(f"Album: {seached_song[1]}")
            print(f"Név: {seached_song[2]}")
            print(f"Száma az albumon bellül: {seached_song[3]}")
            print(f"Fajta: {seached_song[4]}")
            print(f"Kiadás dátuma: {seached_song[5]}")
            print(f"Szám hossza: {seached_song[6]}")
