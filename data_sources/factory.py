from data_sources.base import DataSource
from data_sources.mock import MockDatabase
from data_sources.real import RealDatabase


class DataSourceFactory:
    """Фабрика для выбора источника данных"""

    @staticmethod
    def get_data_source(source_type: str, **kwargs) -> DataSource:
        if source_type == "mock":
            print("Работа с мокированным источником данных:")
            return MockDatabase()
        elif source_type == "db":
            return RealDatabase(kwargs["connection"])
        else:
            raise ValueError(f"Unknown source type: {source_type}")
