class Song:
    def __init__(self, row:str) -> None:
        splitted = row.strip().split(";")
        self.creator = splitted[0]
        self.album = splitted[1]
        self.name = splitted[2]
        self.number = (splitted[3])
        self.genre = splitted[4]
        self.year = (splitted[5])
        self.length = splitted[6]

class Tour:
    def __init__(self, row:str) -> None:
        splitted = row.strip().split(";")
        self.band_name = splitted[0]
        self.year = (splitted[1])
        self.country = splitted[2]
        self.city = splitted[3]
        self.event = splitted[4]