import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Juicy", "The Notorious B.I.G", "Hip Hop")
        self.song_2 = Song("Club Tropicana", "Wham", "Classics")
        self.song_3 = Song("Thunderstruck", "ACDC", "Rock")

    def test_song_has_title(self):
        self.assertEqual("Juicy", self.song_1.title)
        self.assertEqual("Club Tropicana", self.song_2.title)
        self.assertEqual("Thunderstruck", self.song_3.title)