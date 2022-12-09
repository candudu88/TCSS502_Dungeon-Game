class Adventurer:
    def __init__(self, name="Player"):
        self.__name = name
        self.__hit_points = 100
        self.__healing_potion_count = 0
        self.__vision_potion_count = 0
        self.__pillars_found = []

    def increase_hit_point(self, amount):
        self.__hit_points = max(0, self.__hit_points - amount)

    def decrease_hit_point(self, amount):
        self.__hit_points = min(100, self.__hit_points + amount)

    def __str__(self):
        return f"Name: {self.__name}\n" \
               f"Hit points: {self.__hit_points}\n" \
               f"Healing potions: {self.__healing_potion_count}" \
               f"Vision potions: {self.__vision_potion_count}\n" \
               f"Pillars found: {self.__pillars_found}"

