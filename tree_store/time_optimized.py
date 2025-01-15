from typing import List, Dict


class TreeStoreTime:
    """
    Большая производительность, но есть недостаток увелиения общей занимаемой памяти объекта класса на ~30%.

    Атирбуты:
        items - базовый список данных.
        items_dict - словарь вида {id эелемента базового списка: эелемент базового списка}.
        children_dict - словарь вида {id родителя: [список элементов базового списка] }.

    Методы:
        get_all: O(1) (прямая ссылка на массив).
        get_item: O(1) (поиск в словаре).
        get_children: O(1) (поиск по ключу).
        get_all_parents: O(d) - где d глубина дерева.
    """

    def __init__(self, items: List[Dict]):
        """Итоговая сложность: O(n)"""
        self.__items = items
        self.__items_dict = {item['id']: item for item in items}
        self.__children_dict = {}
        for item in items:
            parent_id = item['parent']
            if parent_id not in self.__children_dict:
                self.__children_dict[parent_id] = []
            self.__children_dict[parent_id].append(item)

    def get_all(self) -> List[Dict]:
        return self.__items

    def get_item(self, item_id: int) -> Dict:
        return self.__items_dict.get(item_id)

    def get_children(self, item_id: int) -> List[Dict]:
        return self.__children_dict.get(item_id, [])

    def get_all_parents(self, item_id: int) -> List[Dict]:
        parents = []
        while (current_item := self.get_item(item_id)) and current_item['parent'] != 'root':
            parents.append(current_item)
            item_id = current_item['parent']
        if current_item:
            parents.append(current_item)
        return parents
