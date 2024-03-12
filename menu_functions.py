from list import songs, tours
from classes import Song, Tour

def search_by_name(name) -> Song:
    for s in songs:
        if s.name in name: 
            return s
    return None