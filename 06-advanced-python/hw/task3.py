"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря

"""


class ShiftDescriptor:

    def __init__(self, initval):
        if not isinstance(initval, int):
            raise TypeError("Please supply an int")
        self.shift = initval % 26

    def __get__(self, instance, owner):
        new_ord = map(lambda x: x - 26 if x > 122 else x,
                      [ord(symbol) + self.shift for symbol in self.value])
        return "".join(list(chr(x) for x in new_ord))

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Value must be string!")
        if not set(value).issubset(set("abcdefghijklmnopqrstuvwxyz")):
            raise ValueError("Only ASCII letters in string!")
        self.value = value


if __name__ == "__main__":
    class Caesar:
        cypher = ShiftDescriptor(7)
        anticypher = ShiftDescriptor(-7)

    c = Caesar()
    c.cypher = "cypher"
    print(Caesar.cypher)
    c.anticypher = c.cypher
    print(c.anticypher)


    class CeasarSipher:

        message = ShiftDescriptor(4)
        another_message = ShiftDescriptor(7)


    a = CeasarSipher()
    a.message = 'abc'
    a.another_message = 'hello'

    assert a.message == 'efg'
    assert a.another_message == 'olssv'
