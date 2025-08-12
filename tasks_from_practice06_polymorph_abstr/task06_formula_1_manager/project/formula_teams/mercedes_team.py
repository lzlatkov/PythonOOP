from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)
        self.expenses_per_race = 200_000

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        # Petronas sponsor
        if race_pos == 1:
            revenue += 1_000_000
        elif race_pos == 3:
            revenue += 500_000
        # TeamViewer sponsor
        if race_pos == 5:
            revenue += 100_000
        elif race_pos == 7:
            revenue += 50_000

        revenue -= self.expenses_per_race
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

# class MercedesTeam(FormulaTeam):
#
    #
    # @property
    # def team_data(self):
    #     race_expenses = 200_000
    #     sponsors = {"Petronas": {1: 1_000_000, 3: 500_000},
    #                 "TeamViewer": {5: 100_000, 7: 50_000}}
    #     return race_expenses, sponsors
    #
    # def calculate_revenue_after_race(self, race_pos: int):
    #     pass
