import unittest
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room()
        self.room_2 = Room()
        self.room_3 = Room()
        