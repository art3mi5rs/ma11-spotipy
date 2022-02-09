from spotipy_logging.spotipy_logging import playlist_error_log, status_error_log


class PlaylistNameError(ValueError):
    def __init__(self, message):
        playlist_error_log(message)
        self.message = message
        super(PlaylistNameError, self).__init__(message)


class StatusError(RuntimeError):
    def __init__(self):
        status_error_log()
        super(StatusError, self).__init__("Invalid action for status level")
