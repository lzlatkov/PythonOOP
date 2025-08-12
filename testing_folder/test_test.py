from abc import ABC, abstractmethod


class BaseCollector(ABC):
    def __init__(self, name: str, available_money: float, available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts: list[BaseArtifact] = []

    @property
    def name(self):
        return self.__name
######### TO CHECK !

    @name.setter
    def name(self, value):
        if not re.fullmatch(r'[A-Za-z0-9]+( [A-Za-z0-9]+)*', value):
            raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        self.__name = value

    @property
    def available_money(self):
        return self.__available_money

    @available_money.setter
    def available_money(self, value):
        if value < 0.0:
            raise ValueError("A collector cannot have a negative amount of money!")
        self.__available_money = value

    @property
    def available_space(self):
        return self.__available_space

    @available_space.setter
    def available_space(self, value):
        if value < 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self.__available_space = value

    @abstractmethod
    def increase_money(self):
        pass

    def can_purchase(self, artifact_price: float, artifact_space_required: int):
        if artifact_price > self.available_money or artifact_space_required > self.available_space:
            return False
        return True

    def __str__(self):
        artifacts = ", ".join([a.name for a in self.purchased_artifacts]) if self.purchased_artifacts else "none"
        sorted_purchased_artifacts = sorted(artifacts, key=lambda a: -a)
        result = f"Collector name: {self.name}; Money available: {self.available_money}; Space available: {self.available_space}; Artifacts: {sorted_purchased_artifacts}"
        return result
        # sorted_purchased_artifacts_list = sorted((a.name for a in self.purchased_artifacts), reverse=True)
        # sorted_purchased_artifacts = ", ".join(sorted_purchased_artifacts_list) if sorted_purchased_artifacts_list else 'none'