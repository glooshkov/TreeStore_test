from typing import List, Dict


class RealDatabase:
    """Реализация источника данных через условную БД"""

    def __init__(self, connection):
        self.connection = connection

    def fetch_all(self) -> List[Dict]:
        # Реальный SQL-запрос для получения всех данных
        # Здесь возвращается пример данных
        raise NotImplementedError("Подключение к реальной БД не реализовано.")
