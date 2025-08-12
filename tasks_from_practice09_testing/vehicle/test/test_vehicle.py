from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    fuel = 3.5
    horse_power = 100

    def setUp(self):
        self.test_vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init(self):
        self.assertEqual(self.fuel, self.test_vehicle.fuel)
        self.assertEqual(self.fuel, self.test_vehicle.capacity)
        self.assertEqual(self.horse_power, self.test_vehicle.horse_power)
        self.assertEqual(1.25, self.test_vehicle.fuel_consumption)

    def test_class_attributes_type(self):
        self.assertIsInstance(self.test_vehicle.fuel, float)
        self.assertIsInstance(self.test_vehicle.capacity, float)
        self.assertIsInstance(self.test_vehicle.horse_power, float)
        self.assertIsInstance(self.test_vehicle.fuel_consumption, float)

    def test_drive_success(self):
        self.test_vehicle.drive(2)
        self.assertEqual(1, self.test_vehicle.fuel)

    def test_drive_fail(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(4)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_success(self):
        self.test_vehicle.fuel = 1
        self.test_vehicle.refuel(1.2)
        self.assertEqual(2.2, self.test_vehicle.fuel)

    def test_refuel_fail(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(5)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_method(self):
        expected_result = "The vehicle has 100 horse power with 3.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, str(self.test_vehicle))


if __name__ == "__main__":
    main()
