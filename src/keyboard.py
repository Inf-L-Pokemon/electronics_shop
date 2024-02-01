from src.item import Item


class ChangeLang:
    """
    Класс миксин для хранения и изменения раскладки клавиатуры класса Keyboard
    """

    def __init__(self, name: str, price: float, quantity: int, language: str = "EN") -> None:
        """
        Создание экземпляра класса Keyboard.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param language: Раскладка клавиатуры (по умолчанию - "EN")
        """
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self) -> None:
        """
        Метод для изменения раскладки клавиатуры.
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(ChangeLang, Item):
    """
    Класс для представления клавиатур в магазине (наследуется от Item)
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Keyboard.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__(name, price, quantity)
