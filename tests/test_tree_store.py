import pytest

from data_sources.mock import MockDatabase
from tree_store.time_optimized import TreeStoreTime
from tree_store.space_optimized import TreeStoreSpace


@pytest.fixture
def mock_data():
    return MockDatabase.fetch_all()


@pytest.mark.parametrize("tree_class", [TreeStoreTime, TreeStoreSpace])
def test_get_all(tree_class, mock_data):
    ts = tree_class(mock_data)
    assert len(ts.get_all()) == 8


@pytest.mark.parametrize("tree_class", [TreeStoreTime, TreeStoreSpace])
def test_get_item(tree_class, mock_data):
    ts = tree_class(mock_data)
    item = ts.get_item(7)
    assert item == {'id': 7, 'parent': 4, 'type': None}


@pytest.mark.parametrize("tree_class", [TreeStoreTime, TreeStoreSpace])
def test_get_children(tree_class, mock_data):
    ts = tree_class(mock_data)
    children = ts.get_children(4)
    assert len(children) == 2
    assert {'id': 7, 'parent': 4, 'type': None} in children
    assert {'id': 8, 'parent': 4, 'type': None} in children


@pytest.mark.parametrize("tree_class", [TreeStoreTime, TreeStoreSpace])
def test_get_all_parents(tree_class, mock_data):
    ts = tree_class(mock_data)
    parents = ts.get_all_parents(7)
    assert len(parents) == 4
    assert parents[0] == {'id': 7, 'parent': 4, 'type': None}
    assert parents[-1] == {'id': 1, 'parent': 'root'}
