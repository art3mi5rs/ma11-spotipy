class Song:
    def __init__(self, name, songID, albumID, artistID, genres, popularity, logger):
        self.name = name
        self.songID = songID
        self.albumID = albumID
        self.artistID = artistID
        self.genres = genres
        self.popularity = popularity
        self.logger = logger

    def _update_log(self):
        self.logger.info(f"The song {self.name} - artist ID: {self.artistID} was added to Spotipy")
