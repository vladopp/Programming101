import datetime
import random
from tabulate import tabulate
import json
import mutagen
from glob import glob


class Song:

    def __init__(self, title="", artist="", album="", length=""):
        if isinstance(length, int):
            raise(TypeError)
        self.__title = str(title)
        self.__artist = str(artist)
        self.__album = str(album)
        self.__length = str(length)

    def title(self):
        return self.__title

    def artist(self):
        return self.__artist

    def album(self):
        return self.__album

    def seconds(self, time):
        time = time.split(':')
        time = time[::-1]
        res = int(time[0])
        for i in range(1, len(time)):
            res += int(time[i])*(60**i)
        return res

    def length(self, seconds=False, minutes=False, hours=False):
        if seconds is True:
            return seconds(self.__length)
        if minutes is True:
            return seconds(self.__length)//60
        if hours is True:
            return seconds(self.__length)//3600
        return self.__length

    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key] for key in song_dict}

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist(), self.title(), self.album(), self.length())

    def __eq__(self, other):
        if self.title() == other.title() and self.artist() == other.artist() and self.album() == other.album() and self.lenght() == other.length():
            return True
        return False

    def __hash__(self):
        return hash(self.title()) + hash(self.artist()) + hash(self.album()) + hash(self.length())


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.__name = str(name)
        self.__repeat = repeat
        self.__shuffle = shuffle
        self.__list = []
        self.__cursong = 0
        self.__listplayed = []

    def name(self):
        return self.__name

    def cursong(self):
        return self.__cursong

    def listplayed(self):
        return self.__listplayed

    def list(self):
        return self.__list

    def shuffle(self):
        return self.__shuffle

    def repeat(self):
        return self.__repeat

    def add_song(self, song):
        self.__list.append(song)

    def remove_song(self, song):
        try:
                self.__list.remove(song)
        except ValueError as e:
            pass

    def add_songs(self, songs):
        if isinstance(songs, list):
            self.__list.extend(songs)
        if isinstance(songs, Playlist):
            self.__list.extend(songs.list())

    def total_length(self):
        length = 0
        for song in self.lsit():
            length += song.length(seconds=True)
        return str(datetime.timedelta(seconds=length))

    def artists(self):
        artists = {}
        for song in self.lsit():
            if song.artist() not in artists:
                artists[song.artist()] = 1
            else:
                artists[song.artist()] += 1
        return artists

    def next_song(self):
        if self.shuffle() is False:
            if self.cursong() != len(self.list()) - 1:
                self.__cursong += 1
                return self.__list[self.__cursong]
            if self.repeat() is True:
                self.__cursong = 0
                return self.__list[self.__cursong]
            raise Exception("Playlist finished")

        if self.shuffle() is True:
            if len(self.listplayed()) == len(self.list()):
                if self.repeat is True:
                    self.__listplayed = []
                else:
                    raise Exception("Playlist finished")
            while True:
                rand = random.randint() % len(self.list())
                if rand not in self.listplayed():
                    self.__listplayed.append(rand)
                    return self.__list[rand]

    def pprint_playlist(self):
        Headers = ["Artist", "Song", "Length"]
        table = []
        for song in self.list():
            temp = []
            temp.append(song.artist())
            temp.append(song.title())
            temp.append(song.length())
            table.append(temp)
        return tabulate(table, headers=Headers)

    def prepare_json(self):
        data = {
            "name": self.name(),
            "songs": [song.prepare_json() for song in self.list()]
        }
        return data

    def save(self):
        filename = self.__name(" ", "-") + ".json"

        with open(filename, "w") as f:
            f.write(json.dumps(self.prepare_json(), indent=True))


class MusicCrawler:

    def __init__(self, path):
        self.path = path

    def generate_playlist(self):

        namels = self.path.split("/")
        namels = [x for x in namels if x != '']
        name = namels[len(namels)-1]
        new = Playlist(name)

        mp3filepath = self.path
        if mp3filepath[len(mp3filepath)-1] == '/':
            mp3filepath += '*.mp3'
        else:
            mp3filepath += '/*.mp3'
        print(mp3filepath)

        for filename in glob(mp3filepath):
            song = mutagen.File(filename, easy=True)
            new.add_song(Song(song['title'][0], ['artist'][0], ['album'][0], ['length'][0]))

        return new.pprint_playlist()

test = Playlist("test")
test.add_song(Song("edno", "az", "parvi", "3:12"))
test.add_song(Song("tri", "az", "parvi", "3:12"))
test.add_song(Song("dve", "az", "parvi", "3:12"))
print(test.pprint_playlist())
