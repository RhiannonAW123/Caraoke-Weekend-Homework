import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest()
        self.guest_2 = Guest()
        self.guest_3 = Guest()