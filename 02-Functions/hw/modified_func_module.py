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
import inspect


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

mf(*[1,4,8,8], **{"a": "z"})

print(mf.__name__)
print(mf.__doc__)

print("\n----------function tests----------\n")

# importing other functions here for the sake of readability
from atom_module import atom
from letters_range_module import letters_range
from make_it_count_module import make_it_count

# works fine on
mod_atom = modified_func(atom, test_fa)
gv, sv, pv, dv = mod_atom(11, test_fa)
gv()
sv(1)
gv()

mod_lr = modified_func(letters_range, "a", "z", 1, **{"b": 6})
print(mod_lr(**{"b": "я"}))
print(mod_lr.__name__)


# !! won't work on functions dependent on global variables. I guess
# importing such functions is a bad practice
# x = 1

# mod_mic = modified_func(make_it_count, test_func, "x")
# mod_counter = mod_mic()
# mod_counter()

# won't work on built-ins
# mod_max = modified_func(max, 1, 2, 3, 4, 5, 5)
# print(mod_max(7, 11))
# mod_min = modified_func(min, 1, 2, 3, 4, 5, 5)
# mod_any = modified_func(any, 0, 2, 3, 4, 5, 5)