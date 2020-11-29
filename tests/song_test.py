import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Juicy", "The Notorious B.I.G", "Hip Hop")
        self.song_2 = Song("Club Tropicana", "Wham", "Classics")
        self.song_3 = Song("Thunderstruck", "ACDC", "Rock")
