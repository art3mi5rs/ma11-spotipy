from exceptions.exceptions import PlaylistNameError, StatusError
from loading.config_parser import get_free_status_val, get_premium_status_val, get_playlist_message
from spotipy_logging.spotipy_logging import new_user_log, update_playlist_logs


class Status:
    def __init__(self):
        self.free = get_free_status_val()
        self.premium = get_premium_status_val()


class User:
    def __init__(self, username, status):
        self.username = username
        self.status = status
        self.playlists = []
        new_user_log(self.username, self.status)

    def add_playlist(self, name):
        if name in self.playlists:
            raise PlaylistNameError(get_playlist_message())
        elif len(self.playlists) >= 5 & self.status == Status().free:
            raise StatusError()
        else:
            self.playlists.append({name: []})
            update_playlist_logs(self.username, name)

    def add_to_playlist(self, playlist, song):
        if len(playlist) >= 20 & self.status == Status().free:
            raise StatusError()
        else:
            playlist.append({song.name: song})
            update_playlist_logs(self.username, playlist, song.name)
