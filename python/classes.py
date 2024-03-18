class Song:
    def __init__(self, row: str) -> None:
        splitted = row.strip().split(';')
        self.artist_name = splitted[0]
        self.album_name = splitted[1]
        self.song_name = splitted[2]
        self.track_number = splitted[3]
        self.genre = splitted[4]
        self.year = int(splitted[5])
        self.length = float(splitted[6].replace(':', '.'))

class Tour:
    def __init__(self, row:str) -> None:
        splitted = row.strip().split(";")
        self.band_name = splitted[0]
        self.year = (splitted[1])
        self.country = splitted[2]
        self.city = splitted[3]
        self.event = splitted[4]