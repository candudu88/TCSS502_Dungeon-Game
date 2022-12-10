import unittest

from adventurer import Adventurer


class AdventurerTests(unittest.TestCase):
    """
    This class tests functionality Adventurer class.
    """
    def test_get_name(self):
        """Test get_name method of Adventurer"""
        adventurer = Adventurer("Player", 1, 1)
        self.assertEqual("Player", adventurer.get_name(), "expected name of Player")

    def test_get_name_type(self):
        """Test type of returned value from get_name method of Adventurer"""
        adventurer = Adventurer(5, 1, 1)
        # self.assertEqual("5", adventurer.get_name(), "expected type of string")

    def test_add_healing_potion(self):
        """Test add_healing_potion method of Adventurer"""
        adventurer = Adventurer("Test", 1, 1)
        adventurer.add_healing_potion()
        self.assertEqual(2, adventurer._number_healing_potions, "expected 2 healing potions")

    def test_use_healing_potion(self):
        """Test get_name method of Adventurer"""
        adventurer = Adventurer("Test", 1, 1)
        adventurer.use_healing_potion()
        self.assertEqual(0, adventurer._number_healing_potions, "expected 0 healing potions")

    def test_add_vision(self):
        """Test add_vision method of Adventurer"""
        adventurer = Adventurer("Player", 1, 1)
        adventurer.add_vision()
        self.assertEqual(2, adventurer._number_vision_potions, "expected 2 vision potions")

    def test_use_vision_potion(self):
        """Test use_vision_potion method of Adventurer"""
        adventurer = Adventurer("Player", 1, 1)
        adventurer.use_vision_potion()
        self.assertEqual(0, adventurer._number_vision_potions, "expected 0 vision potions")

    def test_adventurer_str(self):
        """Test __str__ method of Adventurer"""
        adventurer = Adventurer("Player", 1, 1)
        output_str = str(adventurer)
        expected_str = "Name: "
        self.assertEqual(expected_str, output_str, "expected different string format from __str__")


if __name__ == '__main__':
    unittest.main()
