import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Rory", 50)
        self.guest_2 = Guest("Steve", 40)
        self.guest_3 = Guest("Ally", 60)
        self.guest_4 = Guest("Stuart", 30)
        self.guest_5 = Guest("Liz", 50)
        self.guest_6 = Guest("Rosie", 40)