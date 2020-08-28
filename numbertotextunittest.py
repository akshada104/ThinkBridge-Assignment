import unittest
from numbertotext import format


class TestW2N(unittest.TestCase):
    def test_positives(self):
        self.assertEqual(format("2003984"), "Twenty  Lakh Three Thousand Nine Hundred and Eighty Four only")
        self.assertEqual(format("19"), "Nineteen only")
        self.assertEqual(format("2019"), "Two Thousand Nineteen only")
        self.assertEqual(format("00"), "Zero only")
        self.assertEqual(format("55,555.12"),"Fifty Five Thousand Five Hundred and Fifty Five 55/100 only")
        self.assertEqual(format("0.12"),"Zero 12/100 only")
        self.assertEqual(format("219,23,789"),"Two Crore Nineteen Lakh Twenty Three Thousand Seven Hundred and Eighty Nine only")

if __name__ == '_main_':
    unittest.main()