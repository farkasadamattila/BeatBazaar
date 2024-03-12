from classes import *
from os import system
from menu import sub_menu
from list import *


def main():
    load_from_file("songs.csv")
    load_from_file("tour.csv")
    base_menu()
    option = int(choose_opton())
    sub_menu(option)

def load_from_file(filename:str):
    file = open(filename, "r", encoding="utf8")
    match filename:
        case "songs.csv":
            for row in file:
                songs.append(Song(row))
        case "tour.csv":
            for row in file:
                tours.append(Tour(row))
    file.close()

def base_menu():
    system("cls")
    print("BeatBazár")
    print()
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
    if not type(chosen) is int:
        while not chosen.isnumeric():
            print("Csak olyan számokat fogad el amik 10 és 1 között vannak.")
            input("Tovább... ")
            base_menu()
            chosen = choose_opton()
    else: 
        if chosen > 10 or chosen < 1:
            base_menu()
            chosen = choose_opton()
    return chosen


main()