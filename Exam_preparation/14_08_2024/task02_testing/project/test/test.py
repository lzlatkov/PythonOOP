from project.furniture import Furniture
from unittest import TestCase, main


class TestFurniture(TestCase):
    def setUp(self):
        self.furniture_available = Furniture(model="Office Chair", price=150.99, dimensions=(1200, 800, 600),
                                             in_stock=True, weight=15.5)
        self.furniture_unavailable = Furniture(model="Desk", price=400.0, dimensions=(2000, 1200, 500), in_stock=False)

    def test_init(self):
        self.assertEqual("Office Chair", self.furniture_available.model)
        self.assertEqual(150.99, self.furniture_available.price)
        self.assertEqual((1200, 800, 600), self.furniture_available.dimensions)
        self.assertTrue(self.furniture_available.in_stock)
        self.assertEqual(15.5, self.furniture_available.weight)

    def test_model_empty_string_or_too_long(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture_available.model = ""
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.furniture_available.model = "B" * 51
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))

    def test_price_non_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture_available.price = -1
        self.assertEqual("Price must be a non-negative number.", str(ex.exception))

    def test_dimensions_too_short_or_non_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture_available.dimensions = (1200, 800)
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.furniture_available.dimensions = (1200, 800, 0)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ex.exception))

    def test_valid_weight(self):
        with self.assertRaises(ValueError) as ex:
            self.furniture_available.weight = -1
        self.assertEqual("Weight must be greater than zero.", str(ex.exception))

    def test_get_available_status_in_stock(self):
        self.assertEqual("Model: Office Chair is currently in stock.", self.furniture_available.get_available_status())

    def test_get_available_status_out_of_stock(self):
        self.assertEqual("Model: Desk is currently unavailable.", self.furniture_unavailable.get_available_status())

    def test_get_specifications_weight(self):
        self.assertEqual("Model: Office Chair has the following dimensions: "
                         "1200mm x 800mm x 600mm and weighs: 15.5", self.furniture_available.get_specifications())

        self.assertEqual("Model: Desk has the following dimensions: "
                         "2000mm x 1200mm x 500mm and weighs: N/A", self.furniture_unavailable.get_specifications())


if __name__ == "__main__":
    main()
