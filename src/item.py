import csv


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, rename: str) -> None:
        self.__name = rename
        if len(self.__name) > 10:
            self.__name = self.__name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filepath: str) -> None:
        """
        Инициализирует экземпляры класса `Item` данными из файла ".csv".
        """
        cls.all = []
        with open(filepath, "r", encoding="UTF-8") as f:
            dict_item = csv.DictReader(f)
            for item in dict_item:
                Item(item["name"], float(item["price"]), int(item["quantity"]))

    @staticmethod
    def string_to_number(str_number: str) -> int:
        """
        Возвращает число из числа-строки
        """
        return int(float(str_number))
