class Album:
    def __init__(self, name, album_id, artists, songs={}):
        self.name = name
        self.album_id = album_id
        self.artists = artists
        self.songs = songs
