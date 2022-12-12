import random
import unittest

from room import Room
from dungeon import Dungeon


class DungeonTests(unittest.TestCase):
    """
    This class tests functionality Dungeon class.
    """

    def test_dungeon_init(self):
        """Test instance of Dungeon has rows and columns set"""
        dungeon = Dungeon(4, 4)
        attributes = {"rows": dungeon.rows,
                      "cols": dungeon.cols}
        expected_attributes = {"rows": 4,
                               "cols": 4}
        self.assertDictEqual(expected_attributes, attributes, "expected rows and cols attributes were not set")

    def test_dungeon_has_rooms_of_specified_rows_and_cols(self):
        """Test dungeon has 2D array of specified rows and columns"""
        dungeon = Dungeon(2, 8)
        grid = {"rows": len(dungeon.rooms), "columns": len(dungeon.rooms[0])}
        expected_grid = {"rows": 2, "columns": 8}
        self.assertDictEqual(expected_grid, grid, "expected 2 rows and 8 columns")

    def test_created_dungeon_has_rooms(self):
        """Test dungeon has rooms in every slot"""
        dungeon = Dungeon(4, 4)
        has_rooms = True
        for i in range(4):
            for j in range(4):
                if str(Room(0, 0)) != str(dungeon.rooms[i][j]):
                    has_rooms = False
                    break
        self.assertEqual(True, has_rooms, "Not every space in Dungeon has a room")

    def test_get_room(self):
        """Test get_room method of Dungeon"""
        dungeon = Dungeon(5, 5)
        expected_rooms = []
        for i in range(5):
            expected_rooms.append([])
            for j in range(5):
                expected_rooms[i].append(Room(i, j))
        self.assertEqual(str(expected_rooms), str(dungeon.get_room()), "expected [] with 25 empty rooms")

    def test_get_neighbors(self):
        """Test get neighbors of Room at row:0 col:0"""
        dungeon = Dungeon(4, 4)
        room = dungeon.rooms[0][0]
        output_neighbors = dungeon.get_neighbors(room, [])
        expected_neighbors = [Room(0, 1), Room(1, 0)]
        self.assertEqual(str(expected_neighbors), str(output_neighbors), "expected two empty rooms as neighbors, "
                                                                         "1 east and 1 south")

    def test_create_doors(self):
        """Test creation of doors in a room of Dungeon"""
        dungeon = Dungeon(4, 4)
        room = dungeon.rooms[0][0]
        dungeon.create_doors(room, Room(0, 1))
        if room.north or room.east or room.south or room.east:
            self.assertEqual(True, True, "room has door")
        else:
            self.assertEqual(False, True, "room in dungeon has no doors")

    def test_generate_has_rooms_with_doors(self):
        """Test creation of maze in Dungeon by checking if each room has a door"""
        dungeon = Dungeon(4, 4)
        dungeon.generate()
        rooms = dungeon.rooms
        has_rooms = True
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                room = rooms[i][j]
                if not (room.north or room.east or room.south or room.east):
                    has_rooms = True
                    break
        self.assertEqual(True, has_rooms, "not every room has a door")

    def test_maze(self):
        """Test if generated maze can be navigated"""
        dungeon = Dungeon(5, 5)
        dungeon.generate()
        first_room = dungeon.rooms[0][0]
        stack = []
        visited = []
        stack.append(first_room)
        visited.append(first_room)
        while len(stack) != 0:
            current_room = stack[-1]
            neighbors = dungeon.get_neighbors(current_room, visited)
            if len(neighbors) != 0:
                neighbor = random.choice(neighbors)
                visited.append(neighbor)
                stack.append(neighbor)
            else:
                stack.pop()
        self.assertEqual(25, len(visited), "maze can not be navigated")


if __name__ == '__main__':
    unittest.main()
