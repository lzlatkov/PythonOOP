from typing import List, Union

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity <= len(self.animals):
            return f"Not enough space for animal"

        if self.__budget < price:
            return f"Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        worker = next((w for w in self.workers if w.name == worker_name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum(worker.salary for worker in self.workers)
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_animal_care = sum(animal.money_for_care for animal in self.animals)
        if self.__budget >= total_animal_care:
            self.__budget -= total_animal_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        return self.__print_status(self.animals, "Lion", "Tiger", "Cheetah")
        # lions = []
        # tigers = []
        # cheetahs = []
        # for animal in self.animals:
        #     if animal.__class__.__name__ == "Lion":
        #         lions.append(animal)
        #     elif animal.__class__.__name__ == "Tiger":
        #         tigers.append(animal)
        #     elif animal.__class__.__name__ == "Cheetah":
        #         cheetahs.append(animal)
        #
        # result = [f"You have {len(self.animals)} animals", f"----- {len(lions)} Lions:"]
        # result.extend(repr(lions))
        # result.append(f"----- {len(tigers)} Tigers:")
        # result.extend(repr(tigers))
        # result.append(f"----- {len(cheetahs)} Cheetahs:")
        # result.extend(repr(cheetahs))
        #
        # return "\n".join(result)

    def workers_status(self):
        return self.__print_status(self.workers, "Keeper", "Caretaker", "Vet")
        # keepers = []
        # care_takers = []
        # vets = []
        # for worker in self.workers:
        #     if worker.__class__.__name__ == "Keeper":
        #         keepers.append(worker)
        #     elif worker.__class__.__name__ == "Caretaker":
        #         care_takers.append(worker)
        #     elif worker.__class__.__name__ == "Vet":
        #         vets.append(worker)
        #
        # result = [f"You have {len(self.workers)} workers", f"----- {len(keepers)} Keepers:"]
        # result.extend(repr(keepers))
        # result.append(f"----- {len(care_takers)} Caretakers:")
        # result.extend(repr(care_takers))
        # result.append(f"----- {len(vets)} Vets:")
        # result.extend(repr(vets))
        #
        # return "\n".join(result)

    @staticmethod
    def __print_status(obj_list: list[Union[Animal, Worker]], *class_names: str):
        elements = {name: [] for name in class_names}
        for obj in obj_list:
            elements[obj.__class__.__name__].append(repr(obj))

        result = [f"You have {len(obj_list)} {str(obj_list[0].__class__.__bases__[0].__name__).lower()}s"]
        for key, value in elements.items():
            result.append(f"----- {len(value)} {key}s:")
            result.extend(value)

        return "\n".join(result)

