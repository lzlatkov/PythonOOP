from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    @staticmethod
    def __add_object(obj, collection: list):
        if obj not in collection:
            collection.append(obj)

    @staticmethod
    def __get_object(sub_id, collection):
        return next((o for o in collection if o.id == sub_id), None)

    def add_customer(self, customer: Customer):
        self.__add_object(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__add_object(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.__add_object(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_object(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.__add_object(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        sub_id = self.__get_object(subscription_id, self.subscriptions)
        cust_id = self.__get_object(subscription_id, self.customers)
        trainer_id = self.__get_object(subscription_id, self.trainers)
        equip_id = self.__get_object(subscription_id, self.equipment)
        plan_id = self.__get_object(subscription_id, self.plans)
        return '\n'.join([
            sub_id.__repr__(),
            cust_id.__repr__(),
            trainer_id.__repr__(),
            equip_id.__repr__(),
            plan_id.__repr__(),
        ])

