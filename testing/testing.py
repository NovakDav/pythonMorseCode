import unittest
import morse

class TestMorse(unittest.TestCase):
    def test_encode(self):
        test_veta = "F"
        vysledek = morse.encryption(test_veta)
        self.assertEqual(vysledek, "..-. ")

unittest.main()