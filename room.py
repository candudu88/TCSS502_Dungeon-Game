class Room:
    def __init__(self, row, col):
        self.__healthPotion = False
        self.__visionPotion = False
        self.__pillar = "No pillar"
        self.__hasPillar = False
        self._pit = False
        self._exit = False
        self.__entrance = False
        self.__visited = False
        self.__healthChance = 50
        self.row = row
        self.col = col
        self.north = False
        self.south = False
        self.west = False
        self.east = False

    def get_health_chance(self):
        return self.__healthChance

    # def __str__(self):
    #     item_count = 0;
    #     if self.__healthPotion:
    #         item_count += 1
    #     if self.__visionPotion:
    #         item_count += 1
    #
    #
    #     if item_count > 1:
    #         return "M"
    #
    #     return "Health potion: " + str(self.__healthPotion) + "\n" \
    #            + "Vision potion: " + str(self.__visionPotion) + "\n" \
    #            + "Pillar: " + str(self.__pillar) + "\n" \
    #            + "Pit: " + str(self.__pit) + "\n" \
    #            + "Impassable: " + str(self.__impassable) + "\n" \
    #            + "Entrance: " + str(self.__entrance) + "\n" \
    #            + "Exit: " + str(self.__exit) + "\n\n"
    def __str__(self):
        result = ""
        if self.north:
            result += "N"
        else:
            result += "_"
        if self.south:
            result += "S"
        else:
            result += "_"
        if self.west:
            result += "W"
        else:
            result += "_"
        if self.east:
            result += "E"
        else:
            result += "_"
        result += " "
        # result += f"({self.row}, {self.col})"
        return result

    def __repr__(self):
        return str(self)

    def draw_top(self):
        if self.north:
            print("*   *", end="")
        else:
            print("*****", end="")

    def draw_middle(self):
        if self.west:
            print(" ", end="")
        else:
            print("*", end="")
        print("   ", end="")
        if self.east:
            print(" ", end="")
        else:
            print("*", end="")

    def draw_bottom(self):
        if self.south:
            print("*   *", end="")
        else:
            print("*****", end="")

    def set_health(self, add_potion):
        self.__healthPotion = add_potion

    def set_vision(self, add_vision):
        self.__visionPotion = add_vision

    def can_enter(self):
        return not self.__impassable and not self.__visited

    def is_exit(self):
        return self.__exit

    def set_visited(self, visited):
        self.__visited = visited

    def set_entrance(self):
        self.__entrance = True

    def set_impassible(self, is_impassable):
        self.__impassable = is_impassable

    def set_exit(self):
        self._exit = True

    def set_pillar(self):
        self.__hasPillar = True

    def set_pit(self):
        self._pit = True

    def get_has_pit(self):
        return self._pit


