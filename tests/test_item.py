"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("Кофеварка", 25000.00, 2)


def test_item_init(item):
    assert item.name == "Кофеварка"
    assert item.price == 25000.00
    assert item.quantity == 2


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50000.00


def test_apply_discount(item):
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 20000.00
