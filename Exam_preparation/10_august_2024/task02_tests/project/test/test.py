from unittest import TestCase, main
from project.soccer_player import SoccerPlayer


class TestSoccerPlayer(TestCase):
    def setUp(self):
        self.player = SoccerPlayer("Lionel Messi", 35, 750, "Barcelona")
        self.other_player = SoccerPlayer("Cristiano Ronaldo", 38, 1, "Juventus")

    def test_valid_initialization(self):
        self.assertEqual(self.player.name, "Lionel Messi")
        self.assertEqual(self.player.age, 35)
        self.assertEqual(self.player.goals, 750)
        self.assertEqual(self.player.team, "Barcelona")
        self.assertEqual(self.player.achievements, {})
        self.assertEqual(self.player._VALID_TEAMS, ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"])
        self.assertEqual(SoccerPlayer._VALID_TEAMS, ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"])

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = "Messi"
        self.assertEqual("Name should be more than 5 symbols!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.player.name = "Mess"
        self.assertEqual("Name should be more than 5 symbols!", str(ex.exception))

    def test_age_validation(self):
        with self.assertRaises(ValueError) as ex:
            self.player.age = 15
        self.assertEqual("Players must be at least 16 years of age!", str(ex.exception))

    def test_goals_non_negative(self):
        self.player.goals = -5
        self.assertEqual(self.player.goals, 0)

    def test_team_name_validation(self):
        with self.assertRaises(ValueError) as ex:
            self.player.team = "Alabala"
        self.assertEqual(f"Team must be one of the following: {', '.join(SoccerPlayer._VALID_TEAMS)}!", str(ex.exception))

    def test_change_team_valid(self):
        self.assertEqual(self.player.team, "Barcelona")
        result = self.player.change_team("PSG")
        self.assertEqual(result, "Team successfully changed!")
        self.assertEqual(self.player.team, "PSG")

    def test_change_team_invalid(self):
        self.assertEqual(self.player.team, "Barcelona")
        result = self.player.change_team("Alabala")
        self.assertEqual(result, "Invalid team name!")
        self.assertEqual(self.player.team, "Barcelona")

    def test_add_new_achievement(self):
        self.assertEqual(self.player.achievements, {})
        result = self.player.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.player.achievements, {"Ballon d'Or": 1})

        result = self.player.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.player.achievements, {"Ballon d'Or": 2})

        result = self.player.add_new_achievement("Golden boot")
        self.assertEqual(result, "Golden boot has been successfully added to the achievements collection!")
        self.assertEqual(self.player.achievements, {"Ballon d'Or": 2, "Golden boot": 1})

    def test_comparison_operator_less_than(self):
        result = self.player < self.other_player
        self.assertEqual(result, f"{self.player.name} is a better goal scorer than {self.other_player.name}.")

        result = self.other_player > self.player
        self.assertEqual(result, f"{self.player.name} is a better goal scorer than {self.other_player.name}.")

        self.other_player.goals = 750
        result = self.other_player < self.player
        self.assertEqual(result, f"{self.other_player.name} is a better goal scorer than {self.player.name}.")

        result = self.player < self.other_player
        self.assertEqual(result, f"{self.player.name} is a better goal scorer than {self.other_player.name}.")

        self.player.goals = 1
        self.assertLess(self.player.goals, self.other_player.goals)
        result = self.player < self.other_player
        self.assertEqual(result, f"{self.other_player.name} is a top goal scorer! S/he scored more than {self.player.name}.")


if __name__ == "__main__":
    main()

