from classes import *
from os import system
from list import *


def main():
    load_from_file("python\songs.csv")
    load_from_file("python\\tour.csv")
    kilep = False
    while kilep == False:
        base_menu()
        option = int(choose_opton())
        kilep = sub_menu(option)
        if kilep == False:
            print()
            input("Tovább...")


def load_from_file(filename:str):
    file = open(filename, "r", encoding="utf8")
    file.readline()
    match filename:
        case "python\songs.csv":
            for row in file:
                if row == "":
                    break
                else:
                    songs.append(Song(row))
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
    print("0 - Kilép")
    print("1 - Zene keresés")
    print("2 - Zene felvétele")
    print("3 - ")
    print("4 - ")
    print("5 - ")
    print("6 - ")
    print("7 - ")
    print("8 - ")
    print("9 - ")
    print("10 - ")
    print()

def choose_opton() -> int:
    chosen :str = input("Választás: ")
    if chosen.isnumeric():
        chosen = int(chosen)
        if chosen < 10 or chosen > 0:
            return chosen
        else:
            print("Csak olyan számokat fogad el amik 10 és 0 között vannak1.")
            input("Tovább... ")
            base_menu()
            chosen = choose_opton()
    else:
        print("Csak olyan számokat fogad el amik 10 és 0 között vannak2.")
        input("Tovább... ")
        base_menu()
        chosen = choose_opton()

def sub_menu(option: int) -> bool:
    '''
    Ide írd be a function-t abba a case-be (int) amelyik menupontban van.
    '''
    system('cls')
    match option:
        case 0:
            return True
        case 1:
            name = input("Keresés név alapján: ")
            seached_song = search_by_name(name)
            if seached_song != None:
                print()
                print(f"Készítő: {seached_song.creator}")
                print(f"Album: {seached_song.album}")
                print(f"Név: {seached_song.name}")
                print(f"Száma az albumon bellül: {seached_song.number}")
                print(f"Fajta: {seached_song.genre}")
                print(f"Kiadás éve: {seached_song.year}")
                print(f"Szám hossza: {seached_song.length}")
            else:
                print("Nincs ilyen zene.")

    return False

def search_by_name(name) -> Song:
    for s in songs:
        if s.name in name: 
            return s
    return None

main()