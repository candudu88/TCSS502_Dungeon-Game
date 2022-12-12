import unittest

from room import Room


class RoomTests(unittest.TestCase):
    """
    This class tests functionality Room class.
    """

    def test_room_init(self):
        """Test instance of Adventurer with row and columns"""
        room = Room(10, 20)
        attributes = {"row": room.row,
                      "col": room.col}
        expected_attributes = {"row": 10,
                               "col": 20}
        self.assertDictEqual(expected_attributes, attributes, "expected row and col attributes were not set")

    def test_room_str(self):
        """Test string representation of Room has correct format"""
        room = Room(0, 0)
        expected_str = "*****\n" \
                       "*   *\n" \
                       "*****\n"
        self.assertEqual(expected_str, str(room), "expected format for str of Room did not match")

    def test_room_str_with_health_potion(self):
        """Test string representation of Room with health potion has correct format"""
        room = Room(0, 0)
        room.set_health_potion(True)
        expected_str = "*****\n" \
                       "* H *\n" \
                       "*****\n"
        self.assertEqual(expected_str, str(room), "expected format for str of Room with health potion did not match")

    def test_room_str_with_vision_potion(self):
        """Test string representation of Room with health potion has correct format"""
        room = Room(0, 0)
        room.set_vision_potion(True)
        expected_str = "*****\n" \
                       "* V *\n" \
                       "*****\n"
        self.assertEqual(expected_str, str(room), "expected format for str of Room with vision potion did not match")

    def test_room_str_with_pillar(self):
        """Test string representation of Room with pillar has correct format"""
        room = Room(0, 0)
        room.set_pillar("Abstraction")
        expected_str = "*****\n" \
                       "* A *\n" \
                       "*****\n"
        self.assertEqual(expected_str, str(room), "expected format for str of Room with pillar did not match")

    def test_room_str_with_pit(self):
        """Test string representation of Room with pit has correct format"""
        room = Room(0, 0)
        room.set_pit(True)
        expected_str = "*****\n" \
                       "* X *\n" \
                       "*****\n"
        self.assertEqual(expected_str, str(room), "expected format for str of Room with pit did not match")

    def test_room_str_with_exit(self):
        """Test string representation of Room with exit has correct format"""
        room = Room(0, 0)
        room.set_exit(True)
        expected_str = "*****\n" \
                       "* O *\n" \
                       "*****\n"
        self.assertEqual(expected_str, str(room), "expected format for str of Room with exit did not match")

    def test_room_str_with_entrance(self):
        """Test string representation of Room with entrance has correct format"""
        room = Room(0, 0)
        room.set_entrance(True)
        expected_str = "*****\n" \
                       "* i *\n" \
                       "*****\n"
        self.assertEqual(expected_str, str(room), "expected format for str of Room with entrance did not match")

    def test_room_str_with_health(self):
        """Test string representation of Room with health potion has correct format"""
        room = Room(0, 0)
        room.set_health(True)
        expected_str = "*****\n" \
                       "* H *\n" \
                       "*****\n"
        self.assertEqual(expected_str, str(room), "expected format for str of Room with health potion did not match")

    # def test_room_str_with_vision(self):
    #     """Test string representation of Room with vision potion has correct format"""
    #     room = Room(0, 0)
    #     room.set_vision(True)
    #     expected_str = "*****\n" \
    #                    "* V *\n" \
    #                    "*****\n"
    #     self.assertEqual(expected_str, str(room), "expected format for str of Room with vision potion did not match")

    def test_get_health_potion(self):
        """Test get_health_potion method of Room"""
        room = Room(0, 0)
        self.assertEqual(False, room.get_health_potion(), "expected False, Room should not have health potion")

    def test_set_health_potion(self):
        """Test set_health_potion method of Room"""
        room = Room(0, 0)
        room.set_health_potion(True)
        self.assertEqual(True, room.get_health_potion(), "expected True, Room should have health potion")

    def test_get_vision_potion(self):
        """Test get_vision_potion method of Room"""
        room = Room(0, 0)
        self.assertEqual(False, room.get_vision_potion(), "expected False, Room should not have vision potion")

    def test_set_vision_potion(self):
        """Test set_vision_potion method of Room"""
        room = Room(0, 0)
        room.set_vision_potion(True)
        self.assertEqual(True, room.get_vision_potion(), "expected True, Room should have vision potion")

    def test_get_pillar(self):
        """Test get_pillar method of Room"""
        room = Room(0, 0)
        self.assertEqual("No pillar", room.get_pillar(), "expected \"No pillar\"")

    def test_get_pit(self):
        """Test get_pit method of Room"""
        room = Room(0, 0)
        self.assertEqual(False, room.get_pit(), "expected False, Room should not pit")

    def test_set_pit(self):
        """Test set_pit method of Room"""
        room = Room(0, 0)
        room.set_pit(True)
        self.assertEqual(True, room.get_pit(), "expected True, Room should have a pit")

    def test_get_exit(self):
        """Test get_exit method of Room"""
        room = Room(0, 0)
        self.assertEqual(False, room.get_exit(), "expected False, Room should have an exit")

    def test_set_exit(self):
        """Test set_exit method of Room"""
        room = Room(0, 0)
        room.set_exit(True)
        self.assertEqual(True, room.get_exit(), "expected True, Room should be an exit")

    def test_get_entrance(self):
        """Test get_entrance method of Room"""
        room = Room(0, 0)
        self.assertEqual(False, room.get_entrance(), "expected False, Room should not be an entrance")

    def test_set_entrance(self):
        """Test set_entrance method of Room"""
        room = Room(0, 0)
        room.set_entrance(True)
        self.assertEqual(True, room.get_entrance(), "expected False, Room should be an entrance")

    def test_set_pillar(self):
        """Test set_pillar method of Room"""
        room = Room(0, 0)
        room.set_pillar("Encapsulation")
        self.assertEqual("Encapsulation", room.get_pillar(), "expected pillar of \"A\" in Room")

    def test_room_repr(self):
        """Test repr of Room to be the same as str"""
        room = Room(0, 0)
        self.assertEqual(str(room), repr(room), "expected repr to be the same as str")

    def test_draw_top(self):
        """Test print statement of draw_top method of Room"""
        room = Room(0, 0)
        # test print statements

    def test_draw_middle(self):
        """Test print statement of draw_top method of Room"""
        room = Room(0, 0)
        # test print statements

    def test_draw_bottom(self):
        """Test print statement of draw_bottom method of Room"""
        room = Room(0, 0)
        # test print statements

    def test_set_health(self):
        """Test set_health method of Room"""
        room = Room(0, 0)
        room.set_health("Health Potion")
        self.assertEqual("Health Potion", room.get_health_potion(), "expected Room to have \"Health Potion\"")

    def test_set_vision(self):
        """Test set_vision method of Room"""
        room = Room(0, 0)
        room.set_vision("Vision Potion")
        self.assertEqual("Vision Potion", room._Room__visionPotion, "expected Room to have \"Vision Potion\"")

    def test_can_enter(self):
        """Test cen_enter method of Room when not impassible and not visited"""
        room = Room(0, 0)
        self.assertEqual(True, room.can_enter(), "expected Room that player can enter")

    def test_is_exit(self):
        """Test is_exit method of Room"""
        room = Room(0, 0)
        self.assertEqual(False, room.is_exit(), "expected Room to be an exit")

    def test_set_visited(self):
        """Test is_exit method of Room"""
        room = Room(0, 0)
        room.set_visited(True)
        self.assertEqual(True, room._visited, "expected Room to be visited")

    def test_get_has_pit(self):
        """Test get_has_pit method of Room"""
        room = Room(0, 0)
        self.assertEqual(False, room.get_has_pit(), "expected Room to have no pit")


if __name__ == '__main__':
    unittest.main()
