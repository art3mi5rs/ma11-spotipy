from users.artist import Artist


def get_artists(directory, user):
    artists = [artist.name for artist in directory.values]
    if user.status is "Free":
        return artists[:5]
    return artists


def get_albums(directory, artist_id, user):
    artist_albums = [album.name for album in directory[artist_id].albums]
    if user.status is "Free":
        return artist_albums[:5]
    return artist_albums


def get_top_hits(directory, artist_id, user):
    pass


def get_songs(directory, album_id, artist_id, user):
    pass
