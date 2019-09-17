import unittest
from hoogte_boetes import hoogte_boete

class TestMax(unittest.TestCase):

    def test_hoogte_boete_bij_45(self):
        result = hoogte_boete(45)
        self.assertEqual(result,"ok")

    def test_hoogte_boete_bij_65(self):
        result = hoogte_boete(65)
        self.assertEqual(result,30)

    def test_hoogte_boete_bij_90(self):
        result = hoogte_boete(90)
        self.assertEqual(result, "rijbewijs kwijt")

if __name__ == '__main__':
    unittest.main()