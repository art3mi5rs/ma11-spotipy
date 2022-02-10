from loading.json_loader import JSONLoader
from music.spotipy_directory import Directory
from searching.searching import get_artists
from users.user import User, Status
from pathlib import Path


def main():
    directory = Directory()
    loader = JSONLoader(directory)
    user = User("art3mis", Status().free)
    song_imports = 'songs'
    imports = Path(song_imports).glob('*')

    for file in imports:
        loader.load(file)

    print(get_artists(directory.directory, user))


if __name__ == '__main__':
    main()
