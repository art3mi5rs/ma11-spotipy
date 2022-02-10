from users.artist import Artist


def get_artists(directory, user):
    artists = [artist.name for artist in directory.values]
    return artists


def get_albums(directory, artist_id, user):
    pass

def get_top_hits(directory, artist_id, user):
    pass


def get_songs(directory, album_id, artist_id, user):
    pass
