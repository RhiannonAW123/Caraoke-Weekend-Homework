import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song()
        self.song_2 = Song()
        self.song_3 = Song()
        