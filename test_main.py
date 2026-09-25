import unittest

from main import validate_required, validate_date
from main import get_keywords, calculate_match, get_keyword_match


class TestLostFoundMatcher(unittest.TestCase):

    def test_required_field(self):
        self.assertTrue(validate_required("Electronics", "Category"))
        self.assertFalse(validate_required("", "Category"))

    def test_valid_date(self):
        self.assertTrue(validate_date("2026-09-19"))
        self.assertFalse(validate_date("19-09-2026"))

    def test_keywords(self):
        keywords = get_keywords("Black Wireless Earbuds")

        self.assertIn("black", keywords)
        self.assertIn("wireless", keywords)
        self.assertIn("earbuds", keywords)

    def test_match_score(self):
        lost_item = {
            "id": "L101",
            "category": "Electronics",
            "description": "Black wireless earbuds",
            "location": "Metro Station",
            "date": "2026-09-15",
            "status": "Open"
        }

        found_item = {
            "id": "F205",
            "category": "Electronics",
            "description": "Black wireless earbuds case",
            "location": "Metro Station",
            "date": "2026-09-15",
            "status": "Open"
        }

        score = calculate_match(lost_item, found_item)

        self.assertEqual(score, 100)

    def test_keyword_match(self):
        lost_item = {
            "description": "Black wireless earbuds"
        }

        found_item = {
            "description": "Black wireless earbuds case"
        }

        result = get_keyword_match(lost_item, found_item)

        self.assertEqual(result, "Full")


if __name__ == "__main__":
    unittest.main()