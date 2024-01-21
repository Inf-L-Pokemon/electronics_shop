from src.item import Item


class Phone(Item):
    """
    Класс для представления смартфонов в магазине (наследуется от Item).
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, re_numb: int) -> None:
        if re_numb > 0:
            self.__number_of_sim = re_numb
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
