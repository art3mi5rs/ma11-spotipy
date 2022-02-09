class Album:
    def __init__(self, name, albumID, artistID, songs, logger):
        self.name = name
        self.albumID = albumID
        self.artistID = artistID
        self.songs = songs
        self.logger = logger

    def _update_log(self):
        self.logger.info(f"The album {self.name} - artist ID: {self.artistID} was added to Spotipy")
