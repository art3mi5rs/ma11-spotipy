from spotipy_logging.spotipy_logging import directory_update_log


class Types:
    def __init__(self):
        self.artist = "Artist"
        self.album = "Album"
        self.song = "Song"


class Directory:
    def __init__(self):
        self.directory = {}

    def add_song(self, artistID, albumID, song):
        if artistID not in self.directory:
            self.add_artist()
        if albumID not in self.directory[artistID].albums:
            self.add_album()

        album = self.directory[artistID].albums[albumID]
        album.songs.append({song.songID: song})
        directory_update_log(Types.song, song.name, song.artistID)

    def add_artist(self, artist):
        self.directory.append({artist.artistID: artist})
        directory_update_log(Types.artist, artist.name, artist.artistID)

    def add_album(self, artist, album):
        albums_updating = self.directory[artist.artistID].albums
        albums_updating.append({album.albumID: album})
        directory_update_log(Types.album, album.name, album.albumID)
