from spotipy_logging.spotipy_logging import new_loader_log


class Loader:
    def __init__(self, message, directory):
        self.directory = directory
        new_loader_log(message)

    def load(self, resource):
        pass
