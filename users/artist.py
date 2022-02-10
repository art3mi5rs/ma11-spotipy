from users.user import User, Status


class Artist(User):
    def __init__(self, name, artist_id, albums={}):
        self.name = name
        self.artist_id = artist_id
        self.status = Status().premium
        self.albums = albums
        super(Artist, self).__init__(self.name, self.status)
