class Song:
    def __init__(self, row: str) -> None:
        splitted = row.strip().split(';')
        self.artist_name = splitted[0]
        self.album_name = splitted[1]
        self.song_name = splitted[2]
        self.track_number = splitted[3]
        self.genre = splitted[4]
        self.year = int(splitted[5])
        self.length = int(splitted[6].replace(':', ''))
        minutes = self.length // 100
        seconds = self.length % 100
        self.length = f"{minutes}:{seconds:02}"