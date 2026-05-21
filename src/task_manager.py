class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority="Média"):
        task = {
            "title": title,
            "completed": False,
            "priority": priority
        }
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)


if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task("Criar sistema")
    manager.add_task("Implementar testes", "Alta")

    print(manager.list_tasks())