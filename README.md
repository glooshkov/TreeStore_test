# TreeStore Test Project

## Описание проекта
Данный проект представляет собой реализацию системы управления деревьями с различными типами производительности и потребления памяти. Реализованы два класса:

- **TreeStoreTime**: Оптимизирован для скорости работы за счет увеличения потребления памяти.
- **TreeStoreSpace**: Оптимизирован для меньшего потребления памяти за счет снижения производительности.

Проект также содержит:
- Мокированный источник данных (MockDatabase).
- Интерфейс для работы с реальной базой данных (RealDatabase).
- Фабрику для выбора источника данных (DataSourceFactory).
- Набор тестов для проверки корректности работы классов TreeStore.

---

## Структура проекта

```
TreeStore_test/
├── data_sources/
│   ├── __init__.py
│   ├── mock.py
│   ├── real.py
├── tree_store/
│   ├── __init__.py
│   ├── time.py
│   ├── space.py
├── tests/
│   ├── __init__.py
│   ├── test_tree_store.py
├── main.py
├── requirements.txt
├── README.md
```

### Основные файлы и их назначение:
- **`data_sources/mock.py`**: Реализация мокированного источника данных.
- **`data_sources/real.py`**: Интерфейс для работы с реальной базой данных.
- **`tree_store/time.py`**: Класс TreeStoreTime, оптимизированный для скорости работы.
- **`tree_store/space.py`**: Класс TreeStoreSpace, оптимизированный для экономии памяти.
- **`tests/test_tree_store.py`**: Набор тестов для проверки функциональности TreeStoreTime и TreeStoreSpace.
- **`main.py`**: Основной файл запуска приложения.
- **`requirements.txt`**: Список зависимостей проекта.
- **`README.md`**: Документация по проекту.

---

## Установка

### Шаги для запуска проекта:
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/username/TreeStore_test.git
   ```

2. Перейдите в директорию проекта:
   ```bash
   cd TreeStore_test
   ```

3. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Для Linux/macOS
   .venv\Scripts\activate   # Для Windows
   ```

4. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

5. Запустите основной файл проекта:
   ```bash
   python main.py
   ```

---

## Запуск тестов
Для запуска тестов выполните следующую команду:
```bash
pytest tests/test_tree_store.py
```

---

## Примеры использования
Пример использования классов TreeStore приведен в файле `main.py`. Основные возможности включают:

- Получение всех элементов дерева (`get_all`).
- Получение элемента по его идентификатору (`get_item`).
- Получение всех дочерних элементов (`get_children`).
- Получение всех родителей элемента (`get_all_parents`).

Пример вызовов:
```python
mock_source = DataSourceFactory.get_data_source("mock")
ts_mock = TreeStoreTime(mock_source.fetch_all())

print(ts_mock.get_all_parents(7))
print(ts_mock.get_all())
assert ts_mock.get_item(7) == {"id": 7, "parent": 4, "type": None}
```

---

## Авторы
- **Имя Фамилия** - Глушков Андрей.



