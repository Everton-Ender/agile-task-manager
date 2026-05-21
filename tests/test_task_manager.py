from task_manager import TaskManager


def test_add_task():
    manager = TaskManager()
    manager.add_task("Estudar Python")

    assert len(manager.tasks) == 1


def test_complete_task():
    manager = TaskManager()
    manager.add_task("Projeto")

    manager.complete_task(0)

    assert manager.tasks[0]["completed"] is True


def test_remove_task():
    manager = TaskManager()
    manager.add_task("Excluir tarefa")

    manager.remove_task(0)

    assert len(manager.tasks) == 0