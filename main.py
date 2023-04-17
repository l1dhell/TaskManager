import datetime


class Task:
    def __init__(self, name, description, deadline, date):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.date = date
        self.subtasks = []
        self.status = "В работе"

    # добавление подзадачи
    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

    # удаление подзадачи
    def remove_subtask(self, subtask):
        self.subtasks.remove(subtask)

    # установка статуса выполнения задачи
    def set_status(self, status):
        self.status = status

    # проверка выполнения задачи в срок
    def check_deadline(self):
        if self.status == "Выполнено в срок":
            return True
        elif self.status == "Выполнено с опозданием":
            delta = datetime.datetime.now() - self.deadline
            return delta.days > 0
        else:
            return False

    # проверка завершенности задачи
    def is_completed(self):
        return self.status == "Выполнено в срок" or self.status == "Выполнено с опозданием" or self.status == "Отменено"


class TaskManager:
    def __init__(self):
        self.tasks = []

    # добавление задачи
    def add_task(self, task):
        self.tasks.append(task)

    # удаление задачи
    def remove_task(self, task):
        self.tasks.remove(task)

    # поиск задачи по названию
    def search_by_name(self, name):
        result = []
        for task in self.tasks:
            if task.name == name:
                result.append(task)
        return result

    # поиск задачи по описанию
    def search_by_description(self, description):
        result = []
        for task in self.tasks:
            if task.description == description:
                result.append(task)
        return result

    # поиск задачи по дедлайну
    def search_by_deadline(self, deadline):
        result = []
        for task in self.tasks:
            if task.deadline == deadline:
                result.append(task)
        return result

    # поиск задачи по дате
    def search_by_date(self, date):
        result = []
        for task in self.tasks:
            if task.date == date:
                result.append(task)
        return result

    # сортировка задач по названию
    def sort_by_name(self):
        self.tasks.sort(key=lambda task: task.name)

    # сортировка задач по описанию
    def sort_by_description(self):
        self.tasks.sort(key=lambda task: task.description)

    # сортировка задач по дедлайну
    def sort_by_deadline(self):
        self.tasks.sort(key=lambda task: task.deadline)

    # сортировка задач по дате
    def sort_by_date(self):
        self.tasks.sort(key=lambda task: task.date)

    # автоматическое удаление завершенных задач и подзадач
    def remove_completed_tasks(self):
        for task in self.tasks:
            if task.is_completed():
                self.tasks.remove(task)
            else:
                for subtask in task.subtasks:
                    if subtask.is_completed():
                        task.remove_subtask(subtask)

# Пример использования
task_manager = TaskManager()

# Создаем задачи
task1 = Task("Позвонить в банк", "Позвонить в банк и узнать про кредитную карту", datetime.date(2023, 4, 20), datetime.date.today())
task2 = Task("Подготовить отчет", "Подготовить отчет о продажах за первый квартал", datetime.date(2023, 4, 15), datetime.date.today())
task3 = Task("Записаться на курсы английского языка", "Записаться на курсы английского языка в LanguageLink", datetime.date(2023, 4, 30), datetime.date.today())

# Добавляем задачи в менеджер задач
task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

# Выводим все задачи
print("Все задачи:")
for task in task_manager.tasks:
    print(f"{task.name} - {task.status}")
