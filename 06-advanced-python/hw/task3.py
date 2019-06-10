"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря

"""


class ShiftDescriptor:

    def __init__(self, initval):
        self.shift = initval

    def __get__(self, instance, owner):
        return "".join([chr(ord(symbol) + self.shift)
                        for symbol in self.value])

    def __set__(self, instance, value):
        self.value = value


class CeasarSipher:

    message = ShiftDescriptor(4)
    another_message = ShiftDescriptor(7)


a = CeasarSipher()
a.message = 'abc'
a.another_message = 'hello'

assert a.message == 'efg'
assert a.another_message == 'olssv'
