from users.user import User, Status


class Artist(User):
    def __init__(self, name, artistID, albums, logger):
        super().__init__(name, Status.premium, logger)
        self.name = name
        self.artistID = artistID
        self.status = Status.premium
        self.albums = albums
