from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    username = "Test"
    level = 5
    health = 39.5
    damage = 15.3

    def setUp(self) -> None:
        self.test_hero = Hero(self.username, self.level, self.health, self.damage)
        enemy = Hero("Enemy", self.level, 0, self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.test_hero.username)
        self.assertEqual(self.level, self.test_hero.level)
        self.assertEqual(self.health, self.test_hero.health)
        self.assertEqual(self.damage, self.test_hero.damage)

    def test_class_attribute_type(self):
        self.assertIsInstance(self.test_hero.username, str)
        self.assertIsInstance(self.test_hero.level, int)
        self.assertIsInstance(self.test_hero.health, float)
        self.assertIsInstance(self.test_hero.damage, float)

    def test_enemy_hero_with_same_name_raise_ex(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(enemy)
            self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_lower_or_equal_to_zero(self):
        self.test_hero.health = 0
        enemy = Hero("Enemy", self.level, 100, self.damage)
        with self.assertRaises(ValueError) as error:
            self.test_hero.battle(enemy)
            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test_enemy_hero_health_lower_or_equal_to_zero(self):
        enemy = Hero("Enemy", self.level, 0, self.damage)
        with self.assertRaises(ValueError) as error:
            self.test_hero.battle(enemy)
            self.assertEqual("You cannot fight Enemy. He needs to rest", str(error.exception))

        enemy.health -= 1
        with self.assertRaises(ValueError) as error2:
            self.test_hero.battle(enemy)
            self.assertEqual("You cannot fight Enemy. He needs to rest", str(error2.exception))

    def test_draw(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)
        result = self.test_hero.battle(enemy)
        self.assertEqual(5, self.test_hero.level)
        self.assertEqual(-37.0, self.test_hero.health)
        self.assertEqual(15.3, self.test_hero.damage)
        self.assertEqual("Draw", result)

    def test_hero_win(self):
        enemy = Hero("Enemy", 1, 1, 1)
        result = self.test_hero.battle(enemy)
        self.assertEqual(6, self.test_hero.level)
        self.assertEqual(43.5, self.test_hero.health)
        self.assertEqual(20.3, self.test_hero.damage)
        self.assertEqual("You win", result)

    def test_hero_lose(self):
        enemy = Hero("Enemy", 100, 100, 100)
        result = self.test_hero.battle(enemy)

        self.assertEqual(5, self.test_hero.level)
        self.assertEqual(-9960.5, self.test_hero.health)
        self.assertEqual(15.3, self.test_hero.damage)
        self.assertEqual("You lose", result)

        self.assertEqual(101, enemy.level)
        self.assertEqual(28.5, enemy.health)
        self.assertEqual(105, enemy.damage)

    def test_str(self):
        result = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        self.assertEqual(result, str(self.test_hero))


if __name__ == "__main__":
    main()
