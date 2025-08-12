from unittest import TestCase, main
from project.mammal import Mammal


class MammalTest(TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "Test type", "Test sound")

    def test_init(self):
        self.assertEqual(self.mammal.name, "Test")
        self.assertEqual(self.mammal.type, "Test type")
        self.assertEqual(self.mammal.sound, "Test sound")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Test makes Test sound", result)

    def test_get_kingdon(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_get_info(self):
        result = self.mammal.info()
        self.assertEqual(result, "Test is of type Test type")


if __name__ == "__main__":
    main()
