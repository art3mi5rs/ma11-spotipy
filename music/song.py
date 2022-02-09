class Song:
    def __init__(self, name, song_id, album, artists, popularity, genres=None):
        self.name = name
        self.song_id = song_id
        self.album = album
        self.artists = artists
        self.genres = genres
        self.popularity = popularity
