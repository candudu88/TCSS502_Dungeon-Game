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
        self.assertEqual("5", adventurer.get_name(), "expected name \"5\" of type string but got an int")

    def test_set_number_healing_potions(self):
        """Test set_number_healing_potions method of Adventurer"""
        adventurer = Adventurer("Player", 2, 1)
        adventurer.set_number_healing_potions(5)
        self.assertEqual(5, adventurer._number_healing_potions, "expected number of healing potions to be 5")

    def test_reset_all_pillar(self):
        """Test reset_all_pillar method of Adventurer"""
        adventurer = Adventurer("Player", 2, 1)
        adventurer.pillar_A = True
        adventurer.pillar_E = True
        adventurer.pillar_I = True
        adventurer.pillar_P = True
        adventurer.reset_all_pillar()
        pillars = {"pillarA": adventurer.pillar_A,
                   "pillarE": adventurer.pillar_E,
                   "pillarI": adventurer.pillar_I,
                   "pillarP": adventurer.pillar_P}
        expected_pillars = {"pillarA": False,
                            "pillarE": False,
                            "pillarI": False,
                            "pillarP": False}
        self.assertDictEqual(expected_pillars, pillars, "expected all pillars(A, E, I, P) to be reset to False")

    def test_set_number_vision_potions(self):
        """Test set_number_healing_potions method of Adventurer"""
        adventurer = Adventurer("Player", 1, 2)
        adventurer.set_number_vision_potions(10)
        self.assertEqual(10, adventurer._number_vision_potions, "expected number of vision potions to be 10")

    def set_hit_point(self):
        """Test set_hit_point method of Adventurer"""
        adventurer = Adventurer("Player", 2, 1)
        original_hp = adventurer.hit_point
        adventurer.set_hit_point()
        new_hp = adventurer.hit_point
        if original_hp != new_hp:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False, "the hit point was not set to a new hit point")

    def set_hit_point_is_in_range(self):
        """Test range of new hit point from set_hit_point method of Adventurer"""
        adventurer = Adventurer("Player", 2, 1)
        new_hp = adventurer.set_hit_point()
        if 75 <= new_hp <= 100:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False, "the hit point is not in range 75-100")

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

    def test_vision_potion(self):
        """Test vision_potion method of Adventurer"""
        adventurer = Adventurer("Player", 1, 4)
        self.assertEqual(4, adventurer.get_vision_potion(), "expected number of vision potions to be 4")

    def test_get_healing_potion(self):
        """Test get_healing_potion method of Adventurer"""
        adventurer = Adventurer("Player", 8, 1)
        self.assertEqual(8, adventurer.get_healing_potion(), "expected number of healing potions to be 8")

    def test_use_vision_potion(self):
        """Test use_vision_potion method of Adventurer"""
        adventurer = Adventurer("Player", 1, 1)
        adventurer.use_vision_potion()
        self.assertEqual(0, adventurer._number_vision_potions, "expected 0 vision potions")

    def test_damage_by_pit(self):
        """Test damage_by_pit method of Adventurer"""
        adventurer = Adventurer("Player", 2, 1)
        original_hp = adventurer.hit_point
        adventurer.damage_by_pit()
        new_hp = adventurer.hit_point
        if new_hp < original_hp:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False, "expected hit point to be reduced")

    def test_damage_by_pit_does_not_exceed_zero_hp(self):
        """Test hit_point does not exceed 0 after damage_by_pit method of Adventurer"""
        adventurer = Adventurer("Player", 2, 1)
        for i in range(101):
            adventurer.damage_by_pit()
        self.assertEqual(0, adventurer.hit_point, "expected hit point >= 0 after damage by pit")

    def test_adventurer_str(self):
        """Test __str__ method of Adventurer"""
        adventurer = Adventurer("Player", 1, 1)
        output_str = str(adventurer)
        hitpoint = str(adventurer.hit_point)
        expected_str = f"Name: Player\nHit point: {hitpoint}\nTotal Healing Potion: 1\nTotal Vision Potion: 1\nList of Pillars Pieces Found: \n\n"
        self.assertEqual(expected_str, output_str, "expected different string format from __str__")


if __name__ == '__main__':
    unittest.main()
