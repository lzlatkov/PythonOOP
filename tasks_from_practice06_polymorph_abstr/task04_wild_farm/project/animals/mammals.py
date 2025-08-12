from project.animals.animal import Mammal
from project.food import Fruit, Vegetable, Meat


class Mouse(Mammal):
    @property
    def foods(self):
        return [Fruit, Vegetable]

    @property
    def animal_weight(self):
        return 0.1

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    @property
    def foods(self):
        return [Meat]

    @property
    def animal_weight(self):
        return 0.4

    @staticmethod
    def make_sound():
        return "Woof"


class Cat(Mammal):
    @property
    def foods(self):
        return [Vegetable, Meat]

    @property
    def animal_weight(self):
        return 0.3

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    @property
    def foods(self):
        return [Meat]

    @property
    def animal_weight(self):
        return 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"
