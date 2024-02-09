import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone


@pytest.fixture
def item():
    return Item("Кофеварка", 25000.00, 2)


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


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


def test_name_setter(item):
    item.name = "СуперСмартфон"
    assert item.name == "СуперСмарт"


def test_instantiate_from_csv():
    Item.instantiate_from_csv("src/items.csv")
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number("4.85") == 4


def test_repr_method(item):
    assert repr(item) == "Item('Кофеварка', 25000.0, 2)"


def test_str_method(item):
    assert str(item) == "Кофеварка"


def test_add_method(item, phone):
    assert item + phone == 7
    assert item + item == 4
    assert phone + phone == 10
    with pytest.raises(ValueError):
        phone + 6


def test_fnfe_exception():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("src/item.csv")


def test_icsve_exception():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("tests/broken_test_file.csv")
