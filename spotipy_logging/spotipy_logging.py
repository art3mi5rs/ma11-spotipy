import logging

from users.user import User
from users.artist import Artist



def new_user_log(user):
    logging.info(f"{user.username}, a {user.status} user was created")


def update_playlist_logs(username, playlist, song=None):
    if song is None:
        logging.info(f"{username} created the new playlist: {playlist}")
    else:
        logging.info(f"{username} added {song.name} to the playlist {playlist}")


def directory_update_log(type, name, id):
    logging.info(f"{type} {name} -ID: {id} was added to the Spotipy directory")


def new_loader_log(message):
    logging.info(message)


def playlist_error_log(message):
    logging.error(f"ERROR: {message}")


def status_error_log():
    logging.error("ERROR: Invalid action for status level")
