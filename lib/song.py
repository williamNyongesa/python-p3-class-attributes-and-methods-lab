class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.increment_count()
        Song.update_genres(self.genre)
        Song.update_artists(self.artist)
        Song.update_genre_count(self.genre)
        Song.update_artist_count(self.artist)

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def update_genres(cls, genre):
        cls.genres.add(genre)

    @classmethod
    def update_artists(cls, artist):
        cls.artists.add(artist)

    @classmethod
    def update_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def update_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
