import random
class Adventurer:
    def __init__(self, name, healing_potions=1, vision_potions=1):
        self._name = name
        self.hit_point = random.randrange(75, 100)
        self._number_healing_potions = healing_potions
        self._number_vision_potions = vision_potions
        self.pillar_A = False
        self.pillar_E = False
        self.pillar_I = False
        self.pillar_P = False



    def get_name(self):
        return self._name

    def add_healing_potion(self):
        self._number_healing_potions += 1

    def use_healing_potion(self):
        if self._number_healing_potions > 0:
            self._number_healing_potions -= 1

    def add_vision(self):
        self._number_vision_potions += 1

    def use_vision_potion(self):
        if self._number_vision_potions > 0:
            self._number_vision_potions -= 1

    def __str__(self):
        """This method overrides the version from the object class and is called when you print a Adventurer"""
        res = "Name: " + str(self._name) + "\n" \
               + "Hit point: " + str(self.hit_point) + "\n" \
               + "Total Healing Potion: " + str(self._number_healing_potions) + "\n" \
               + "Total Vision Potion: " + str(self._number_vision_potions) + "\n" \
               + "List of Pillars Pieces Found: "
        if self.pillar_A:
            res = res + "Abstraction "
        if self.pillar_E:
            res = res + "Encapsulation "
        if self.pillar_I:
            res = res + "Inheritance "
        if self.pillar_P:
            res = res + "Polymorphism "
        res = res + "\n\n"
        return res



ad = Adventurer("warrior")
print(ad)
