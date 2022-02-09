import logging

def new_user_log(status):
    logging.info(f"A new {status} user was created")


def update_playlist_logs(username, playlist, song=None):
    if song == None:
        logging.info(f"{username} created the new playlist: {playlist}")
    else:
        logging.info(f"{username} added {song.name} to the playlist {playlist}")