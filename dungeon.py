import random

from room import Room


class Dungeon:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.pillars = ["A", "E", "I", "P"]
        self.rooms = []
        for i in range(rows):
            self.rooms.append([])
            for j in range(cols):
                self.rooms[i].append(Room(i, j))

        self.generate_maze()

    def get_room(self):
        return self.rooms

    def print(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.rooms[row][col], sep=' ', end="")
            print()

    def draw(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.rooms[row][col].draw_top()
            print()
            for col in range(self.cols):
                self.rooms[row][col].draw_middle()
            print()
            for col in range(self.cols):
                self.rooms[row][col].draw_bottom()
            print()

    def get_neighbors(self, current, visited):
        neighbors = []
        if current.row > 0 and not self.rooms[current.row - 1][current.col] in visited:  # check if we can go north
            neighbors.append(self.rooms[current.row - 1][current.col])
        if current.row < self.rows - 1 and not self.rooms[current.row + 1][
                                                   current.col] in visited:  # check if we can go south
            neighbors.append(self.rooms[current.row + 1][current.col])
        if current.col > 0 and not self.rooms[current.row][current.col - 1] in visited:  # check if we can go west
            neighbors.append(self.rooms[current.row][current.col - 1])
        if current.col < self.cols - 1 and not self.rooms[current.row][
                                                   current.col + 1] in visited:  # check if we can go south
            neighbors.append(self.rooms[current.row][current.col + 1])
        return neighbors

    def create_doors(self, current, neighbor):
        if neighbor.col - current.col > 0:
            current.east = True
            neighbor.west = True
        elif neighbor.col - current.col < 0:
            current.west = True
            neighbor.east = True
        elif neighbor.row - current.row > 0:
            current.south = True
            neighbor.north = True
        elif neighbor.row - current.row < 0:
            current.north = True
            neighbor.south = True

    def generate_maze(self):
        source = self.rooms[0][0]
        target = self.rooms[self.rows - 1][self.cols - 1]
        stack = []
        visited = []
        stack.append(source)
        visited.append(source)
        while len(stack) != 0:
            current = stack[-1]
            # find all neighbors of the current vertex
            # make sure that they are not visited
            neighbors = self.get_neighbors(current, visited)
            # print(current, neighbors)
            if len(neighbors) != 0:
                # pick a random neighbor to move
                neighbor = random.choice(neighbors)
                visited.append(neighbor)
                stack.append(neighbor)
                # make doors at this point
                self.create_doors(current, neighbor)
            else:
                stack.pop()

        # place health potions, vision potions, pits, pillars, entrance and exit
        for i in range(0, len(self.rooms)):
            for j in range(0, len(self.rooms[i])):
                self.set_health_potion(i, j)
                self.set_vision_potion(i, j)
                self.set_pillar(i, j)
                self.set_pit(i, j)
        self.set_entrance()
        self.set_exit()

    def set_health_potion(self, row, col):
        if row != 0 and col != 0 and row != len(self.rooms) - 1 and col != len(self.rooms[row]) - 1:
            r = random.randint(1, 10)
            if r == 1:
                self.rooms[row][col].set_health(True)

    def set_vision_potion(self, row, col):
        if row != 0 and col != 0 and row != len(self.rooms) - 1 and col != len(self.rooms[row]) - 1:
            r = random.randint(1, 10)
            if r == 1:
                self.rooms[row][col].set_vision(True)

    def set_pit(self, row, col):
        if row != 0 and col != 0 and row != len(self.rooms) - 1 and col != len(self.rooms[row]) - 1:
            r = random.randint(1, 10)
            if r == 4:
                self.rooms[row][col].set_pit()

    def set_entrance(self):
        self.rooms[0][0].set_entrance()

    def set_exit(self):
        self.rooms[-1][-1].set_exit()

    def set_pillar(self, row, col):
        if row != 0 and col != 0 and row != len(self.rooms) - 1 and col != len(self.rooms[row]) - 1:
            self.rooms[row][-1].set_pillar()

