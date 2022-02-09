class Types:
    def __init__(self):
        self.artist = "Artist"
        self.album = "Album"
        self.song = "Song"


class Directory:
    def __init__(self, logger):
        self.directory = {}
        self.logger = logger

    def add_song(self, artistID, albumID, song):
        if artistID not in self.directory:
            self.add_artist()
        if albumID not in self.directory[artistID].albums:
            self.add_album()

        album = self.directory[artistID].albums[albumID]
        # TODO: create song
        # TODO: add song to album/artist

    def add_artist(self, artist):
        # TODO: write method code here
        self._update_log(Types.artist, artist.artistID)

    def add_album(self, artist, album):
        # TODO: write method code here
        self._update_log(Types.album, album.albumID)

    def _update_log(self, type, id):
        self.logger.info(f"{type} -ID: {id} was added to the Spotipy directory")
