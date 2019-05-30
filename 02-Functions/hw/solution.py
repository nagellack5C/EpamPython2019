import inspect

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


# tests

print(letters_range("b"))
print(letters_range("b", "j"))
print(letters_range("b", "j", 2))
print(letters_range("j", "b", **{'l': 7, 'o': 0}))
print(letters_range("k", "z", **{'l': 7, 'o': 0}))


'''
Напишите реализацию функции atom, которая инкапсулирует некую переменную,
предоставляя интерфейс для получения и изменения ее значения,
таким образом, что это значение нельзя было бы получить или изменить
иными способами.
Пусть функция atom принимает один аргумент, инициализирующий хранимое значение
(значение по умолчанию, в случае вызова atom без аргумента - None),
а возвращает 3 функции - get_value, set_value, process_value, delete_value,такие, что:

get_value - позволяет получить значение хранимой переменной;
set_value - позволяет установить новое значение хранимой переменной,
	возвращает его;
process_value - принимает в качестве аргументов сколько угодно функций
	и последовательно (в порядке перечисления аргументов) применяет эти функции
	к хранимой переменной, обновляя ее значение (перезаписывая получившийся
	результат) и возвращая получишееся итоговое значение.
delete_value - удаляет значение
'''


def atom(val = None):
    locals()["val"] = val

    def get_value():
        nonlocal val
        try:
            print(val)
        except Exception:
            print("haha it's gone")

    def set_value(new_val):
        nonlocal val
        val = new_val
        return val

    def process_value(*args):
        nonlocal val
        for func in args:
            val = func(val)
        return val

    def delete_value():
        nonlocal val
        del val

    return get_value, set_value, process_value, delete_value


# tests

gv, sv, pv, dv = atom(13)
gv()
sv(100500)

multiply = lambda x: x * 2
increase = lambda x: x + 2

gv()
pv(multiply, increase)
gv()
dv()
gv()



'''
Напишите реализацию функции make_it_count, которая принимает в качестве
аргументов некую функцию (обозначим ее func) и имя глобальной переменной
(обозначим её counter_name), возвращая новую функцию, которая ведет себя
в точности как функция func, за тем исключением, что всякий раз при вызове
инкрементирует значение глобальной переменной с именем counter_name.
'''


def make_it_count(func, counter_name):
    func_args = inspect.getfullargspec(make_it_count)[0]

    def new_func(*func_args):
        globals()[counter_name] += 1
        func(*func_args)

    return new_func


# tests


def smth_f(smth):  # test function
    print("I have", smth, "problems but Python ain't one")


problems = 0  # test global var

smth_f(1)
new_func = make_it_count(smth_f, "problems")
new_func(10)
new_func(99)
print(problems)


'''Напишите функцию modified_func, которая принимает функцию (обозначим ее func),
а также произвольный набор позиционных (назовем их fixated_args) и именованных
(назовем их fixated_kwargs) аргументов и возвращает новую функцию,
которая обладает следующими свойствами:

1.При вызове без аргументов повторяет поведение функции func, вызванной
с fixated_args и fixated_kwargs.
2.При вызове с позиционными и именованными аргументами дополняет ими
fixed_args (приписывает в конец списка fixated_args), и fixated_kwargs
(приписывает новые именованные аргументы и переопределяет значения старых)
и далее повторяет поведение func с этим новым набором аргументов.
3.Имеет __name__ вида func_<имя функции func>
4.Имеет docstring вида:

"""
A func implementation of <имя функции func>
with pre-applied arguments being:
<перечисление имен и значений fixated_args и fixated_kwargs>
source_code:
   ...
"""

Для того, чтобы получить имена позиционных аргументов и исходный код, советуем использовать
возможности модуля inspect.

Попробуйте применить эту функцию на написанных функциях из дз1, дз2, дз3. К функциям min, max, any() ?
'''


def modified_func(func, *fixed_args, **fixed_kwargs):

    def mod_func(*args, **kwargs):
        f_args = list(fixed_args)
        if args:
            f_args.extend(args)
        f_kwargs = fixed_kwargs
        if kwargs:
           f_kwargs.update(kwargs)
        original_args = inspect.getfullargspec(func)
        if original_args[2]:  # check if func accepts kwargs
            return func(*fixed_args, **fixed_kwargs)
        return func(*fixed_args)  # if it doesn't we call it with args only

    mod_func.__name__ = "func_" + func.__name__
    mod_func.__doc__ = f'''A func implementation of {func.__name__}
        with pre-applied arguments being:
        {fixed_args} and {fixed_kwargs}
        source_code: {inspect.getsource(func)}'''

    return mod_func


# tests

test_fa = [1, 5, 3]
test_kwa = {"a": 0, "b": 1}


def test_func(*args, **kwargs):
    print("Hello World")


mf = modified_func(test_func, *test_fa, **test_kwa)

mf(*[4, 8, 15, 16, 23, 42], **{"a": "z"})

print(mf.__name__)
print(mf.__doc__)

print("\n----------function tests----------\n")

# works fine on
mod_atom = modified_func(atom, test_fa)
gv, sv, pv, dv = mod_atom(11, test_fa)
gv()
sv(1)
gv()

mod_lr = modified_func(letters_range, "a", "z", 1, **{"b": 6})
print(mod_lr(**{"b": "я"}))
print(mod_lr.__name__)


# !! won't work on imported functions dependent on global variables. I guess
# importing such functions is a bad practice

# but works fine if this function is defined in the same module
x = 1

mod_mic = modified_func(make_it_count, test_func, "x")
mod_counter = mod_mic()
mod_counter()
print(x)

# won't work on built-ins
# mod_max = modified_func(max, 1, 2, 3, 4, 5, 5)
# print(mod_max(7, 11))
# mod_min = modified_func(min, 1, 2, 3, 4, 5, 5)
# mod_any = modified_func(any, 0, 2, 3, 4, 5, 5)
