import unittest
from hoogte_boetes import hoogteBoete

class TestMax(unittest.TestCase):

    def test_hoogte_boete_bij_45(self):
        result = hoogteBoete(45)
        self.assertEqual(result,"ok")

    def test_hoogte_boete_bij_65(self):
        result = hoogteBoete(65)
        self.assertEqual(result,30)

    def test_hoogte_boete_bij_90(self):
        result = hoogteBoete(90)
        self.assertEqual(result, "rijbewijs kwijt")

if __name__ == '__main__':
    unittest.main()