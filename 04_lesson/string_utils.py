class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """

    def capitalize(self, string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной
        и возвращает этот же текст
        Пример: `capitilize("skypro") -> "Skypro"`
        """
        return string.capitalize()

    def trim(self, string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале, если они есть
        Пример:делает первую букву заглавной
           """
        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)
        return string

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращаете текст
 если строка содержит искомый символ
        ими утилит- если нет
        """
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass

        return res

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки
        """
        if self.contains(string, symbol):
            string = string.replace(symbol, "")
        return string