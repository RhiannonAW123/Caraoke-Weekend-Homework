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

    def test_guest_has_name(self):
        self.assertEqual("Rory", self.guest_1.name)
        self.assertEqual("Steve", self.guest_2.name)
        self.assertEqual("Ally", self.guest_3.name)
        self.assertEqual("Stuart", self.guest_4.name)
        self.assertEqual("Liz", self.guest_5.name)
        self.assertEqual("Rosie", self.guest_6.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest_1.wallet)
        self.assertEqual(40, self.guest_2.wallet)
        self.assertEqual(60, self.guest_3.wallet)
        self.assertEqual(30, self.guest_4.wallet)
        self.assertEqual(50, self.guest_5.wallet)
        self.assertEqual(40, self.guest_6.wallet)
        