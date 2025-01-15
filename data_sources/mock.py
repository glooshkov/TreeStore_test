from typing import List, Dict


class MockDatabase:
    """Реализация мокированного источника данных"""

    @staticmethod
    def fetch_all() -> List[Dict]:
        list_data = [
            {'id': 1, 'parent': 'root'},
            {'id': 2, 'parent': 1, 'type': 'test'},
            {'id': 3, 'parent': 1, 'type': 'test'},
            {'id': 4, 'parent': 2, 'type': 'test'},
            {'id': 5, 'parent': 2, 'type': 'test'},
            {'id': 6, 'parent': 2, 'type': 'test'},
            {'id': 7, 'parent': 4, 'type': None},
            {'id': 8, 'parent': 4, 'type': None}
        ]
        return list_data
