from loading.json_loader import JSONLoader
from music.spotipy_directory import Directory
from searching.searching import get_artists
from users.user import User, Status


def main():
    directory = Directory()
    loader = JSONLoader(directory)
    user = User("art3mis", Status().free)
    loader.load("C:\\Users\\User\\Shachaf-Repos\\Spotipy\\songs\\song_0C9jZPUv4SuaXkuEQw6L40.json")
    print(get_artists(directory.directory, user))


if __name__ == '__main__':
    main()
