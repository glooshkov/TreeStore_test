import io
import pprint
import sys

import pytest

from data_sources.factory import DataSourceFactory
from tree_store.time_optimized import TreeStoreTime


def run_tests():
    """Функция для запуска тестов с захватом вывода"""
    captured_output = io.StringIO()
    sys.stdout = captured_output

    pytest.main(["-q", "--tb=line"])

    sys.stdout = sys.__stdout__
    print(captured_output.getvalue())


def main():
    mock_source = DataSourceFactory.get_data_source("mock")
    ts_mock = TreeStoreTime(mock_source.fetch_all())

    print(ts_mock.get_all_parents(7))
    pprint.pprint(ts_mock.get_all())

    run_tests()


if __name__ == '__main__':
    main()
