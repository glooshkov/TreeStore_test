import itertools
import operator
from typing import List, Dict


class TreeStoreSpace:
    """
    Ниже производительность, но объект класса занимает меньше памяти. Увеличивается удобочитаемость.

    Атирбуты:
        items_dict - словарь вида {id эелемента базового списка: эелемент базового списка}.
        children_dict - словарь вида {id родителя: [список элементов базового списка] }.

    Методы:
        get_all: O(n) (создание списка из значений словаря).
        get_item: O(1) (поиск в словаре).
        get_children: O(k), где k — число детей.
        get_all_parents: O(d) - где d глубина дерева.
    """

    def __init__(self, items):
        """Итоговая сложность: O(n log n)"""
        self.__items_dict = {item['id']: item for item in items}
        self.__children_dict = {pid: [item['id'] for item in items] for pid, items in
                                itertools.groupby(self.__items_dict.values(), operator.itemgetter('parent'))}

    def get_all(self) -> List[Dict]:
        return list(self.__items_dict.values())

    def get_item(self, item_id):
        return self.__items_dict.get(item_id, None)

    def get_children(self, item_id) -> List[Dict]:
        return list(map(self.get_item, self.__children_dict.get(item_id, [])))

    def get_all_parents(self, item_id):
        item = self.get_item(item_id)
        if not item:
            return []

        parent_id = item.get('parent')
        return [item] + self.get_all_parents(parent_id) if parent_id else [item]
