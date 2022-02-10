from loading.json_loader import JSONLoader
from music.spotipy_directory import Directory
from searching.searching import get_artists


def main():
    directory = Directory()
    loader = JSONLoader(directory)
    loader.load("C:\\Users\\User\\Shachaf-Repos\\Spotipy\\songs\\song_0C9jZPUv4SuaXkuEQw6L40.json")
    print(get_artists(directory.directory))


if __name__ == '__main__':
    main()
