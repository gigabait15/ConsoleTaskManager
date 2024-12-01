from datetime import datetime
from typing import Dict, Union
from src.TaskManager import TaskManager
from src.Tasks import Tasks
from src.JSONT import JSONT


class Display:
    """
    Класс Display предоставляет интерфейс для взаимодействия пользователя с задачами.
    """

    def __init__(self):
        """
        Инициализирует объект Display, связывая его с менеджером задач, классом задач и JSON-обработчиком.
        """
        self.task_manager = TaskManager()
        self.object_task = Tasks
        self.json_task = JSONT()

    @staticmethod
    def change_priority() -> str:
        """
        Выводит список приоритетов и позволяет пользователю выбрать один из них.
        :return: Выбранный приоритет в виде строки.
        """
        priority_list = ['низкий', 'средний', 'высокий']
        for index, priority in enumerate(priority_list):
            print(index + 1, priority)

        while True:
            try:
                choose_user = int(input('Выберите число: '))
                if 1 <= choose_user <= len(priority_list):
                    return priority_list[choose_user - 1]
                else:
                    print("Нет такого числа.")
            except ValueError:
                print("Введите число!")

    @staticmethod
    def change_task() -> Dict[str, Union[str, None]]:
        """
        Позволяет изменить свойства задачи.
        :return: Словарь с обновленными данными задачи.
        """
        title = input("Новое название (оставьте пустым для сохранения текущего): ").strip()
        description = input("Новое описание (оставьте пустым для сохранения текущего): ").strip()
        category = input("Новая категория (оставьте пустым для сохранения текущей): ").strip()
        priority = Display.change_priority()

        while True:
            due_date = input("Дата (формат: YYYY-MM-DD, оставьте пустым для сохранения текущей): ").strip()
            if not due_date:
                break
            try:
                if due_date < datetime.now().strftime('%Y-%m-%d'):
                    print('Нельзя указывать дату выполнения в прошлом.')
                else:
                    datetime.strptime(due_date, "%Y-%m-%d")
                    break
            except ValueError:
                print("Неверный формат даты. Убедитесь, что дата указана в формате YYYY-MM-DD.")

        return {
            'title': title or None,
            'description': description or None,
            'category': category or None,
            'priority': priority,
            'due_date': due_date or None,
        }

    def task_create(self) -> Dict:
        """
        Создает новую задачу, запрашивая у пользователя данные.
        :return: Словарь с данными новой задачи.
        """
        id: int = int(self.task_manager.get_all_tasks()[-1]['id']) + 1 \
            if self.task_manager.get_all_tasks() else 0

        while True:
            title: str = input("Введите название задачи: ").strip()
            if title:
                break
            print("Пустая строка. Попробуйте снова.")

        while True:
            description: str = input("Введите описание задачи: ").strip()
            if description:
                break
            print("Пустая строка. Попробуйте снова.")

        while True:
            category: str = input('Введите категорию задачи: ').strip()
            if category:
                break
            print("Пустая строка. Попробуйте снова.")

        while True:
            due_date: str = input("Введите дату сдачи задачи (формат: YYYY-MM-DD): ").strip()
            if due_date < datetime.now().strftime('%Y-%m-%d'):
                print('Нельзя указывать дату выполнения в прошлом.')
                continue
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
                break
            except ValueError:
                print("Неверный формат даты. Убедитесь, что дата указана в формате YYYY-MM-DD.")

        priority: str = self.change_priority()

        new_task = Tasks(
            task_id=id,
            title=title,
            description=description,
            category=category,
            date_complete=due_date,
            priority=priority,
        )
        print('Объект задачи успешно создан.')
        return new_task.__dict__

    def choice_task(self, choice_item: str) -> None:
        """
        Фильтрует задачи по указанному параметру.
        :param choice_item: Параметр фильтрации (например, 'category' или 'priority').
        """
        read_list = self.task_manager.get_all_tasks()
        list_choice = [item[choice_item] for item in read_list]

        for index, item in enumerate(set(list_choice)):
            print(index + 1, item)

        while True:
            try:
                user_choose = int(input('Выберите номер: '))
                if 1 <= user_choose <= len(list_choice):
                    print(*[task for task in read_list if task[choice_item] == list_choice[user_choose - 1]], sep='\n')
                    break
                else:
                    print("Некорректный номер.")
            except ValueError:
                print("Введите число.")

    def main(self) -> None:
        """
        Основное меню программы. Управляет взаимодействием пользователя с задачами.
        """
        while True:
            print(
                'Основное меню\n'
                '1 - Создание новой задачи\n'
                '2 - Просмотр задач\n'
                '3 - Изменение задачи\n'
                '4 - Удаление задачи\n'
                '0 - Завершить работу программы\n'
            )
            try:
                user_choose = int(input('Выберите пункт для продолжения: '))
                if user_choose == 0:
                    break

                if user_choose == 1:
                    task = self.task_create()
                    print(f'Задача создана:\n{task}')
                    self.task_manager.add_task(task)

                if user_choose == 2:
                    if len(self.task_manager.get_all_tasks()) == 0:
                        print('Список задач пуст\n')
                        continue
                    else:
                        print(
                            'Меню просмотра задач\n'
                            '\t0 - вернуться назад\n'
                            '\t1 - все задачи\n'
                            '\t2 - по категориям\n'
                            '\t3 - по приоритету\n'
                            '\t4 - по статусу\n'
                            '\t5 - по ключевым словам\n'
                        )
                        try:
                            user_choose_2 = int(input('Выберите пункт для продолжения: '))

                            list_menu_2 = ['category', 'priority', 'status']
                            list_menu_2_ru = ['категориям', 'приоритету', 'статусу']

                            if user_choose_2 == 1:
                                print('Все ваши задачи')
                                print(*self.task_manager.get_all_tasks(), sep='\n', end='\n\n')

                            if 2 <= user_choose_2 <= 4:
                                print(f'Задачи по {list_menu_2_ru[user_choose_2 - 2]}')
                                self.choice_task(list_menu_2[user_choose_2 - 2])

                            if user_choose_2 == 5:
                                user_title_or_desc = input('Введите ключевое слово: ')
                                desc = self.task_manager.get_task_by_title_or_desc(user_title_or_desc)
                                if desc:
                                    print(desc)
                                else:
                                    print(f'Нет задач с указанным ключевым словом: {user_title_or_desc}')

                            if user_choose_2 == 0:
                                continue
                            if user_choose_2 > 5:
                                print('Вы ввели несуществующий номер\n')
                        except ValueError:
                            print('Нужно ввести цифру\n')

                if user_choose == 3:
                    if len(self.task_manager.get_tasks()) == 0:
                        print('Список задач пуст\n')
                        continue
                    else:
                        list1 = [{'id': item['id'], 'title': item['title'], 'status': item['status']} for item in
                                 self.task_manager.get_all_tasks() if item['status'] == 'не выполнено']
                        print('Меню изменения задачи\nХочешь изменить задачу или ее статус\n1 - Изменить задачу\n'
                              '2 - Сменить статус "задачи на выполнено"\n')

                        user_choose_3 = int(input('Введите цифру здесь: '))
                        print(f'Список всех задач подлежащих выполнению')
                        print(*list1, sep='\n', end='\n\n')

                        if user_choose_3 == 1:
                            try:
                                choose_user_3 = int(input('Введите номер задачи: '))
                                if self.task_manager.get_task_by_id(choose_user_3):
                                    change_3 = self.change_task()
                                    self.task_manager.change_task(choose_user_3, **change_3)
                                else:
                                    print('Вы ввели несуществующий номер\n')
                            except ValueError:
                                print('Нужно ввести цифру\n')

                        if user_choose_3 == 2:
                            try:
                                choose_user_3 = int(input('Введите номер задачи: '))
                                if self.task_manager.get_task_by_id(choose_user_3):
                                    self.task_manager.change_task_status(choose_user_3)
                                else:
                                    print('Вы ввели несуществующий номер\n')
                            except ValueError:
                                print('Нужно ввести цифру\n')

                if user_choose == 4:
                    if len(self.task_manager.get_tasks()) == 0:
                        print('Список задач пуст\n')
                        continue
                    else:
                        print('Список задач:')
                        print(*self.task_manager.get_all_tasks(), sep='\n', end='\n\n')
                        try:
                            user_choose_4 = int(input('Введите номер задачи, которую нужно удалить: '))
                            if self.task_manager.get_task_by_id(user_choose_4):
                                self.task_manager.delete_task(user_choose_4)
                            else:
                                print(f'Задачи с номером {user_choose_4} нет')
                        except ValueError:
                            print('Нужно ввести цифру\n')

                    if user_choose > 4:
                        print('Введите число из меню\n')
                        continue

            except ValueError:
                print('Нужно ввести цифру\n')







