import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Juicy", "The Notorious B.I.G", "Hip Hop")
        self.song_2 = Song("Club Tropicana", "Wham", "Classics")
        self.song_3 = Song("Thunderstruck", "ACDC", "Rock")
        self.guest_1 = Guest("Rory", 50)
        self.guest_2 = Guest("Steve", 40)
        self.guest_3 = Guest("Ally", 60)
        self.guest_4 = Guest("Stuart", 30)
        self.guest_5 = Guest("Liz", 50)
        self.guest_6 = Guest("Rosie", 40)
        self.room_1 = Room("Hip Hop Room", self.song_1.title, self.song_1.artist, 6, 5, 100)
        self.room_2 = Room("Classics Room", self.song_2.title, self.song_2.artist, 6, 3, 150)
        self.room_3 = Room("Rock Room", self.song_3.title, self.song_3.artist, 6, 4, 200)

    def test_room_has_name(self):
        self.assertEqual("Hip Hop Room", self.room_1.name)
        self.assertEqual("Classics Room", self.room_2.name)
        self.assertEqual("Rock Room", self.room_3.name)

    def test_room_has_fee(self):
        self.assertEqual(5,self.room_1.fee)
        self.assertEqual(3,self.room_2.fee)
        self.assertEqual(4,self.room_3.fee)

    