import unittest
from src.models.artlang import ArtLang

class TestArtLang(unittest.TestCase):
    def setUp(self):
        self.artlang = ArtLang()

    def test_generate_output(self):
        result = self.artlang.generate_output("Test content generation")
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
