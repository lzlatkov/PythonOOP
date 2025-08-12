from unittest import TestCase, main


class TestWorker(TestCase):
    def test_init(self):
        # Arrange, Act
        w = Worker("Test", 1000, 100)

        # Assert
        self.assertEqual(w.name, "Test")
        self.assertEqual(w.salary, 1000)
        self.assertEqual(w.energy, 100)
        self.assertEqual(w.money, 0)

    def test_worker_work_no_energy_raises(self):
        # Arrange
        # Create worker with no energy
        w = Worker("Test", 1000, 0)
        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 0)

        with self.assertRaises(Exception) as ex:
            w.work()

        self.assertEqual(str(ex.exception), "Not enough energy.")
        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 0)

    def test_worker_works(self):
        w = Worker("Test", 1000, 100)
        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 100)

        result = w.work()
        self.assertEqual(w.money, 1000)
        self.assertEqual(w.energy, 99)
        self.assertIsNone(result)

    def test_worker_rest(self):
        w = Worker("Test", 1000, 100)
        self.assertEqual(w.energy, 100)
        result = w.rest()
        self.assertEqual(w.energy, 101)
        self.assertIsNone(result)

    def test_info(self):
        w = Worker("Test", 1000, 100)

        result = w.get_info()
        expected_result = "Test has saved 0 money."

        self.assertEqual(expected_result, result)

        w.work()
        result = w.get_info()
        expected_result = "Test has saved 1000 money."
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
