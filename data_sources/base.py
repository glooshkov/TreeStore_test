from typing import Protocol, List, Dict


class DataSource(Protocol):
    """Интерфейс для источников данных"""

    def fetch_all(self) -> List[Dict]:
        ...
