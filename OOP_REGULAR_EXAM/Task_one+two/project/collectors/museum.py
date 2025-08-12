from project.collectors.base_collector import BaseCollector


class Museum(BaseCollector):
    INITIAL_MONEY = 15000.0
    INITIAL_SPACE = 2000

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_MONEY, self.INITIAL_SPACE)

    def increase_money(self):
        self.available_money += 1000.0
