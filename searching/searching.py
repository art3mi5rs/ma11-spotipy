from spotipy_logging.spotipy_logging import update_searching_log
from users.artist import Artist
from music.album import Album
from music.song import Song


def get_song_popularity(song):
    return song.popularity


def get_artists(directory, user):
    artists = [artist.name for artist in directory.values]
    if user.status is "Free":
        update_searching_log("artist", "Free")
        return artists[:5]
    update_searching_log("artist", "Premium")
    return artists


def get_albums(directory, artist_id, user):
    artist_albums = [album.name for album in directory[artist_id].albums]
    if user.status is "Free":
        update_searching_log("album", "Free")
        return artist_albums[:5]
    update_searching_log("album", "Premium")
    return artist_albums


def get_songs(directory, album_id, artist_id, user):
    album_songs = [song.name for song in directory[artist_id].albums[album_id]]
    if user.status is "Free":
        update_searching_log("song", "Free")
        return album_songs[:5]
    update_searching_log("song", "Premium")
    return album_songs


def get_top_hits(directory, artist_id, user):
    artist_songs = []
    for album in directory[artist_id].albums:
        artist_songs.extend(album.songs.values())
    artist_songs.sort(key=get_song_popularity)

    if user.status is "Free":
        update_searching_log("top-hits", "Free")
        return artist_songs[:5]
    update_searching_log("top-hits", "Premium")
    return artist_songs[:10]
