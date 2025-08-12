from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        try:
            task = [el for el in self.tasks if task_name == el.name][0]
            task.completed = True
            return f"Completed task {task_name}"
        except IndexError:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = [el for el in self.tasks if el.completed]
        not_completed_tasks = [el for el in self.tasks if not el.completed]
        self.tasks = not_completed_tasks
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        result += "\n".join([el.details() for el in self.tasks])
        return result
