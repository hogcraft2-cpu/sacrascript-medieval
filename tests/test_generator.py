import unittest
from sacrascript.generator import generate


class GeneratorTests(unittest.TestCase):
    def test_polish_prayer_contains_amen(self):
        result = generate("prayer", "pokój", "polish")
        self.assertIn("Modlitwa", result)
        self.assertIn("Amen.", result)

    def test_bilingual_contains_both_languages(self):
        result = generate("blessing", "żniwa", "bilingual")
        self.assertIn("Benedictio", result)
        self.assertIn("Błogosławieństwo", result)

    def test_invalid_kind_fails(self):
        with self.assertRaises(ValueError):
            generate("mass", "Sunday", "latin")

    def test_empty_occasion_fails(self):
        with self.assertRaises(ValueError):
            generate("prayer", "  ", "latin")


if __name__ == "__main__":
    unittest.main()
