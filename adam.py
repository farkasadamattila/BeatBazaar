class Song:
    def __init__(self, row: str) -> None:
        splitted = row.strip().split(';')
        if len(splitted) >= 6:
            self.artist_name = splitted[0]
            self.album_name = str(splitted[1])
            self.song_name = splitted[2]
            self.track_number = splitted[3]
            self.genre = splitted[4]
            self.year = int(splitted[5])
            length_minutes, length_seconds = map(int, splitted[6].split(':'))
            self.length = f"{length_minutes}:{length_seconds:02}"
        else:

            pass