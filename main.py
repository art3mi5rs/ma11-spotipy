from loading.config_parser import get_import_path
from loading.json_loader import JSONLoader
from music.spotipy_directory import Directory
from searching.searching import get_artists
from users.user import User, Status
from pathlib import Path


def main():
    directory = Directory()
    loader = JSONLoader(directory)
    user = User("art3mis", Status().free)
    imports = Path(get_import_path()).glob('*')

    for file in imports:
        loader.load(file)

    print(get_artists(directory.directory, user))


if __name__ == '__main__':
    main()
