from music.album import Album
from spotipy_logging.spotipy_logging import directory_update_log
from users.artist import Artist


class Types:
    def __init__(self):
        self.artist = "Artist"
        self.album = "Album"
        self.song = "Song"


class Directory:
    def __init__(self):
        self.directory = {}

    def add_artist(self, artist):
        new_artist = Artist(artist['name'], artist['id'])
        self.directory[new_artist.artist_id] = new_artist
        directory_update_log(Types().artist, new_artist.name, new_artist.artist_id)

    def add_album(self, artists, album):
        for artist in artists:
            albums_updating = self.directory[artist.artist_id].albums
            new_album = Album(album['name'], album['id'], artist)
            albums_updating[new_album.album_id] = new_album
            directory_update_log(Types().album, new_album.name, new_album.album_id)

    def add_song(self, song):
        for artist in song.artists:
            if artist['id'] not in self.directory:
                self.add_artist(artist)
        if song.album['id'] not in self.directory[song.artists[0]['id']].albums.album_id:
            self.add_album(song.artists, song.album)

        album = self.directory[song.artists[0]['id']].albums[song.album.album_id]
        album.songs[song.song_id] = song
        directory_update_log(Types().song, song.name, song.artists)
