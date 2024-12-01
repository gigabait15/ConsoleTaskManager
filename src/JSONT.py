import json
from typing import List, Dict


class JSONT:
    """
    Класс для работы с JSON-файлом, содержащим задачи.
    """

    @staticmethod
    def read_json_file() -> List[Dict]:
        """
        Читает данные из JSON-файла.
        Если файл пустой, отсутствует или содержит невалидный JSON, возвращает пустой список.
        :return: List[Dict]: Список задач в виде словарей.
        """
        try:
            with open('src/TaskManager.json', 'r', encoding='utf-8') as file:
                data = file.read()
                if not data:
                    return []
                return json.loads(data)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def write_json_file(tasks: List[Dict]) -> None:
        """
        Записывает список задач в JSON-файл.
        :param tasks: (List[Dict]) Список задач для сохранения.
        """
        with open('src/TaskManager.json', 'w', encoding='utf-8') as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
