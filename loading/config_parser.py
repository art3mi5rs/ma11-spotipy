from configparser import ConfigParser


def _init():
    parser = ConfigParser()
    parser.read('config.ini')
    return parser


def get_import_path():
    parser = _init()
    return parser['files']['import_path']


def get_artist_val():
    parser = _init()
    return parser['music']['artist_type']


def get_album_val():
    parser = _init()
    return parser['music']['album_type']


def get_song_val():
    parser = _init()
    return parser['music']['song_type']


def get_free_status_val():
    parser = _init()
    return parser['users']['free_status']


def get_premium_status_val():
    parser = _init()
    return parser['users']['premium_status']


def get_playlist_message():
    parser = _init()
    return parser['messages']['existing_playlist_message']


def get_loader_message():
    parser = _init()
    return parser['messages']['json_loader_message']


def get_status_message():
    parser = _init()
    return parser['messages']['status_error_message']
