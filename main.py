from loading.json_loader import JSONLoader
from music.spotipy_directory import Directory


def main():
    directory = Directory()
    loader = JSONLoader(directory)
    loader.load("C:\\Users\\User\\Shachaf-Repos\\Spotipy\\songs\\song_0C9jZPUv4SuaXkuEQw6L40.json")


if __name__ == '__main__':
    main()
