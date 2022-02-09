from exceptions.exceptions import PlaylistNameError, StatusError
from spotipy_logging.spotipy_logging import new_user_log, update_playlist_logs


class Status:
    def __init__(self):
        self.free = "Free"
        self.premium = "Premium"


class User:
    def __init__(self, username, status, logger):
        self.username = username
        self.status = status
        self.logger = logger
        self.playlists = []
        new_user_log(status)

    def add_playlist(self, name):
        if name in self.playlists:
            raise PlaylistNameError("This playlist already exists")
        elif len(self.playlists) >= 5 & self.status == "Free":
            raise StatusError()
        else:
            self.playlists.append({name: []})
            update_playlist_logs(self.username, name)

    def add_to_playlist(self, playlist, song):
        if len(playlist) >= 20 & self.status == "Free":
            raise StatusError()
        else:
            playlist.append({song.name: song})
            update_playlist_logs(self.username, playlist, song)
