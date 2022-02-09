from exceptions.exceptions import PlaylistNameError, StatusError


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
        self._update_log()

    def add_playlist(self, name):
        if name in self.playlists:
            raise PlaylistNameError("This playlist already exists")
        elif len(self.playlists) >= 5 & self.status == "Free":
            raise StatusError()
        else:
            #TODO: create a new playlist
            pass

    def add_to_playlist(self, playlist, song):
        if len(playlist) >= 20 & self.status == "Free":
            raise StatusError()
        else:
            #TODO: add song to playlist
            pass

    def _update_log(self):
        self.logger.info(f"A new {self.status} user was created")
