class Tasks:
    """
    Класс для создания экземпляра задачи.
    """


    def __init__(
        self,
        task_id: int,
        category: str,
        title: str,
        description: str,
        date_complete: str,
        priority: str,
    ):
        """
        Инициализирует экземпляр задачи.
            task_id (int): Уникальный идентификатор задачи
            category (str): Категория задачи.
            title (str): Название задачи.
            description (str): Подробное описание задачи.
            date_complete (str): Дата выполнения задачи в формате "YYYY-MM-DD".
            priority (str): Приоритет задачи.
        """
        self.id: int = task_id
        self.title: str = title
        self.description: str = description
        self.category: str = category
        self.due_date: str = date_complete
        self.priority: str = priority
        self.status: str = 'не выполнено'
