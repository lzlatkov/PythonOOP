from project.formula_teams.formula_team import FormulaTeam


# class RedBullTeam(FormulaTeam):
#
#     @property
#     def team_data(self):
#         race_expenses = 250_000
#         sponsors = {"Oracle": {1:  1_500_000, 2: 800_000},
#                     "Honda": {8: 20_000, 10: 10_000}}
#         return race_expenses, sponsors
#
#     def calculate_revenue_after_race(self, race_pos: int):
#         pass
class RedBullTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)
        self.expenses_per_race = 250_000

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        # Oracle sponsor
        if race_pos == 1:
            revenue += 1_500_000
        elif race_pos == 2:
            revenue += 800_000
        # Honda sponsor
        if race_pos <= 8:
            revenue += 20_000
        elif race_pos <= 10:
            revenue += 10_000

        revenue -= self.expenses_per_race
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
