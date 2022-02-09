import json

from loading.loader import Loader
from music.song import Song


class JSONLoader(Loader):
    def __init__(self, directory):
        self.directory = directory
        super(JSONLoader, self).__init__("A new JSONLoader was created", self.directory)

    def load(self, file):
        song_file = open(file)
        song_data = json.load(song_file)
        album_data = song_data['track']['album']
        artists_data = song_data['track']['artists']
        #artist_ids = [artist_data['id'] for artist_data in artists_data]
        song_id = song_data['track']['id']
        song_name = song_data['track']['name']
        song_popularity = song_data['track']['popularity']
        song = Song(song_name, song_id, album_data, artists_data, song_popularity)
        self.directory.add_song(song)
