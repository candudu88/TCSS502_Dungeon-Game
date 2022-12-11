import unittest

from adventurer import Adventurer


class AdventurerTests(unittest.TestCase):
    """
    This class tests functionality Adventurer class.
    """

    def test_adventurer_init(self):
        """Test instance of Adventurer with only name"""
        adventurer = Adventurer("Player")
        attributes = {"name": adventurer._name,
                      "hit_point": adventurer.hit_point,
                      "number_healing_potions": adventurer._number_healing_potions,
                      "number_vision_potions": adventurer._number_vision_potions}
        expected_attributes = {"name": "Player",
                               "hit_point": adventurer.hit_point,
                               "number_healing_potions": 1,
                               "number_vision_potions": 1}
        self.assertDictEqual(expected_attributes, attributes, "expected attributes were not set")

    def test_adventurer_init_with_potions(self):
        """Test instance of Adventurer with healing and vision potion amounts"""
        adventurer = Adventurer("Player", 2, 5)
        attributes = {"name": adventurer._name,
                      "hit_point": adventurer.hit_point,
                      "number_healing_potions": adventurer._number_healing_potions,
                      "number_vision_potions": adventurer._number_vision_potions}
        expected_attributes = {"name": "Player",
                               "hit_point": adventurer.hit_point,
                               "number_healing_potions": 2,
                               "number_vision_potions": 5}
        self.assertDictEqual(expected_attributes, attributes, "expected attributes were not set")

    def test_get_name(self):
        """Test get_name method of Adventurer"""
        adventurer = Adventurer("Player", 1, 1)
        self.assertEqual("Player", adventurer.get_name(), "expected name of Player")

    def test_get_name_type(self):
        """Test type of returned value from get_name method of Adventurer"""
        adventurer = Adventurer(5, 1, 1)
        self.assertEqual(False, isinstance(adventurer.get_name(), str), "expected name with type of string")

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
        adventurer.add_vision_potion()
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
        hitpoint = str(adventurer.hit_point)
        expected_str = f"Name: Player\nHit point: {hitpoint}\nTotal Healing Potion: 1\nTotal Vision Potion: 1\nList of Pillars Pieces Found: \n\n"
        self.assertEqual(expected_str, output_str, "expected different string format from __str__")


if __name__ == '__main__':
    unittest.main()
