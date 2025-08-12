from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    @property
    def foods(self):
        return [Meat]

    @property
    def animal_weight(self):
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def animal_weight(self):
        return 0.35

    @property
    def foods(self):
        return [Seed, Fruit, Vegetable, Meat]

    @staticmethod
    def make_sound():
        return "Cluck"



