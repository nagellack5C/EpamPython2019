'''
Некоторые встроенные функции в Python имеют нестандартное поведение, когда
дело касается аргументов и их значений по умолчанию.
Например, range, принимает от 1 до 3 аргументов, которые обычно называются
start, stop и step и при использовании всех трех, должны указываться
именно в таком порядке. При этом только у аргументов start и step есть значения
по умолчанию (ноль и единица), а у stop его нет, но ведь аргументы без значения
по умолчанию, то есть позиционные аргументы, должны указываться до именнованных,
а stop указывается после start. Более того, при передаче функции только одного
аргумента он интерпретируется как stop, а не start.
Подумайте, каким образом, можно было бы добиться такого же поведения для
какой-нибудь нашей пользовательской функции.
Напишите функцию letters_range, которая ведет себя похожим на range образом,
однако в качестве start и stop принимает не числа, а буквы латинского алфавита
(в качестве step принимает целое число) и возвращает не перечисление чисел, а
список букв, начиная с указанной в качестве start (либо начиная с 'a',
если start не указан), до указанной в качестве stop с шагом step (по умолчанию
равным 1). Добавить возможность принимать словарь с заменами букв для подобия траслитерации.
Т.е. замена символов из оригинального алфавита другими, возможно несколькими символами.
'''


def letters_range(*args, **kwargs):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    if kwargs:
        # first I scan kwargs and store letter indices to prevent double
        # replacements (e.g. if kwargs == {"a": "z", "z": "a"} then
        # if we scan and replace keys 1 by 1 we'd get 'a...a' alphabet
        # instead of 'z...a' alphabet as intended)
        replacements = []
        for char in kwargs:
            replacements.append((alphabet.index(char), str(kwargs[char])))
        for rep in replacements:
            alphabet[rep[0]] = rep[1]
    if len(args) == 1:
        stop = alphabet.index(args[0])
        return alphabet[:stop]
    if len(args) == 2:
        start = alphabet.index(args[0])
        stop = alphabet.index(args[1])
        step = -1 if start > stop else 1
        return alphabet[start:stop:step]
    if len(args) == 3:
        start = alphabet.index(args[0])
        stop = alphabet.index(args[1])
        step = args[2]
        return alphabet[start:stop:step]


print(letters_range("b"))
print(letters_range("b", "j"))
print(letters_range("b", "j", 2))
print(letters_range("j", "b", **{'l': 7, 'o': 0}))
print(letters_range("k", "z", **{'l': 7, 'o': 0}))