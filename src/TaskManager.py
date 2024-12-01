from typing import List, Dict, Optional
from src.JSONT import JSONT


class TaskManager:
    """
    Класс TaskManager предназначен для управления задачами.
    Работает с JSON-файлом для хранения задач.
    """

    def __init__(self):
        """
        Инициализирует объект TaskManager, связывая его с методами чтения и записи JSON.
        """
        self.get_tasks = JSONT.read_json_file
        self.write_tasks = JSONT.write_json_file

    def get_all_tasks(self) -> List[Dict]:
        """
        Возвращает список всех задач.
        :return: Список задач (каждая задача представлена словарем).
        """
        return self.get_tasks()

    def get_task_by_id(self, task_id: int) -> bool:
        """
        Проверяет наличие задачи с указанным ID.
        :param task_id: ID задачи для поиска.
        :return: True, если задача с указанным ID существует, иначе False.
        """
        tasks = self.get_tasks()
        return any(task['id'] == task_id for task in tasks)

    def get_task_by_title_or_desc(self, item: str) -> Optional[Dict]:
        """
        Ищет задачу по совпадению в названии или описании.
        :param item: Текст для поиска в названии или описании.
        :return: Словарь с задачей, если найдено совпадение, иначе None.
        """
        tasks = self.get_tasks()
        for task in tasks:
            if item in task['title'] or item in task['description']:
                return task
        return None

    def add_task(self, task: Dict) -> None:
        """
        Добавляет новую задачу в список.
        :param task: Словарь с данными новой задачи.
        """
        tasks = self.get_tasks()
        tasks.append(task)
        self.write_tasks(tasks)
        print(f'Задача с id {task["id"]} успешно добавлена в список')

    def change_task(self, task_id: int, **kwargs) -> None:
        """
        Изменяет данные существующей задачи.
        :param task_id: ID задачи, которую нужно изменить.
        :param kwargs: Поля для изменения (title, description, category, priority, due_date).
        """
        tasks = self.get_tasks()
        for task in tasks:
            if task['id'] == task_id:
                task['title'] = kwargs.get('title', task['title'])
                task['description'] = kwargs.get('description', task['description'])
                task['category'] = kwargs.get('category', task['category'])
                task['priority'] = kwargs.get('priority', task['priority'])
                task['due_date'] = kwargs.get('due_date', task['due_date'])

        self.write_tasks(tasks)
        print(f'Задача номер {task_id} изменена\n')

    def change_task_status(self, task_id: int) -> None:
        """
        Меняет статус задачи на 'выполнена'.
        :param task_id: ID задачи, статус которой нужно изменить.
        """
        tasks = self.get_tasks()
        for task in tasks:
            if task['id'] == task_id:
                task['status'] = 'выполнена'

        self.write_tasks(tasks)
        print(f'Статус задачи под номером {task_id} изменен на "выполнена"\n')

    def delete_task(self, task_id: int) -> None:
        """
        Удаляет задачу из списка.
        :param task_id: ID задачи, которую нужно удалить.
        """
        tasks = self.get_tasks()
        for task in tasks:
            if task['id'] == task_id:
                pop_task = tasks.pop(tasks.index(task))
                print(f'Удаленная задача:\n{pop_task}')
        self.write_tasks(tasks)
