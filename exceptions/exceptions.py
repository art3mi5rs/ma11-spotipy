class PlaylistNameError(ValueError):
    def __init__(self, message):
        self.message = message
        super(PlaylistNameError, self).__init__(message)


class StatusError(RuntimeError):
    def __init__(self):
        super(StatusError, self).__init__("Invalid action for status level")
