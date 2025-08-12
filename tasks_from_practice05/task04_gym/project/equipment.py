class Equipment:
    next_equipment_id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.next_equipment_id
        Equipment.next_equipment_id += 1

    @classmethod
    def get_next_id(cls):
        return cls.next_equipment_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

