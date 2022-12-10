class Room:
    def __init__(self, row, col):
        self.__healthPotion = False
        self.__visionPotion = False
        self.__pillar = "No pillar"
        self.__hasPillar = False
        self._healthPotion = False
        self._visionPotion = False
        self._pillar = "No pillar"
        self._pit = False
        self._exit = False
        self._entrance = False
        self._visited = False
        self.row = row
        self.col = col
        self.north = False
        self.south = False
        self.west = False
        self.east = False

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
    # def __str__(self):
    #     result = ""
    #     if self.north:
    #         result += "N"
    #     else:
    #         result += "_"
    #     if self.south:
    #         result += "S"
    #     else:
    #         result += "_"
    #     if self.west:
    #         result += "W"
    #     else:
    #         result += "_"
    #     if self.east:
    #         result += "E"
    #     else:
    #         result += "_"
    #     result += " "
    #     # result += f"({self.row}, {self.col})"
    #     return result

    def __str__(self):
        res = ""
        res += "* - *\n" if self.north else "*****\n"
        res += "|" if self.west else "*"
        if self._healthPotion and self._visionPotion:
            res += " M "
        elif self._healthPotion:
            res += " H "
        elif self._visionPotion:
            res += " V "
        elif self._pit:
            res += " X "
        elif self._exit:
            res += " O "
        elif self._entrance:
            res += " i "
        elif self._pillar == "Abstraction":
            res += " A "
        elif self._pillar == "Encapsulation":
            res += " E "
        elif self._pillar == "Inheritance":
            res += " I "
        elif self._pillar == "Polymorphism":
            res += " P "
        else:
            res += "   "
        res += "|\n" if self.east else "*\n"
        res += "* - *\n" if self.south else "*****\n"
        return res

    def get_health_potion(self):
        return self._healthPotion

    def set_health_potion(self, bool):
        self._healthPotion = bool

    def get_vision_potion(self):
        return self._visionPotion

    def set_vision_potion(self, bool):
        self._visionPotion = bool

    def get_pillar(self):
        return self._pillar

    def get_pit(self):
        return self._pit

    def set_pit(self, bool):
        self._pit = bool

    def get_exit(self):
        return self._exit

    def set_exit(self, flag):
        self._exit = flag

    def get_entrance(self):
        return self._entrance

    def set_entrance(self, flag):
        self._entrance = flag

    def set_pillar(self, pillar):
        self._pillar = pillar

    def get_pillar(self):
        return self._pillar

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


    def __repr__(self):
        return str(self)

    def set_health(self, add_potion):
        self._healthPotion = add_potion

    def set_vision(self, add_vision):
        self.__visionPotion = add_vision

    def can_enter(self):
        return not self.__impassable and not self._visited

    def is_exit(self):
        return self.__exit

    def set_visited(self, visited):
        self._visited = visited

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






room = Room(0, 0)
# room.set_pillar("Inheritance")
room._entrance = True
room._exit = True
room._pit = True
print(room)

