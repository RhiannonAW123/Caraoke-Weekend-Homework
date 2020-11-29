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

    def test_room_has_capacity(self):
        self.assertEqual(6, self.room_1.capacity)
        self.assertEqual(6, self.room_2.capacity)
        self.assertEqual(6, self.room_3.capacity)

    def test_room_has_till(self):
        self.assertEqual(100, self.room_1.till)
        self.assertEqual(150, self.room_2.till)
        self.assertEqual(200, self.room_3.till)

    def test_room_has_song_played_title(self):
        self.assertEqual("Juicy", self.room_1.song_played_title)
        self.assertEqual("Club Tropicana", self.room_2.song_played_title)
        self.assertEqual("Thunderstruck", self.room_3.song_played_title)

    def test_room_has_song_played_artist(self):
        self.assertEqual("The Notorious B.I.G", self.room_1.song_played_artist)
        self.assertEqual("Wham", self.room_2.song_played_artist)
        self.assertEqual("ACDC", self.room_3.song_played_artist)

    def test_room_has_no_guests(self):
        self.assertEqual(0, self.room_1.guest_count())

    def test_room_can_check_in_guests(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual("Rory", self.room_1.guest_list[0].name)
        self.assertEqual(1, self.room_1.guest_count())

    def test_room_can_check_out_guests(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_out_guest(self.guest_1)
        self.assertEqual(0, self.room_1.guest_count())

    def test_play_list_has_no_songs(self):
        self.assertEqual(0, self.room_1.song_count())

    def test_add_song_to_room(self):
        self.room_1.add_song_to_play_list(self.song_1)
        self.assertEqual("Juicy", self.room_1.play_list[0].title)
        self.assertEqual(1, self.room_1.song_count())
        
    
