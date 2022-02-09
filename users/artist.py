from users.user import User, Status


class Artist(User):
    def __init__(self, name, artistID, albums):
        self.name = name
        self.artistID = artistID
        self.status = Status.premium
        self.albums = albums
        super(Artist, self).__init__(self.name, self.status)
