'''
Напишите реализацию функции make_it_count, которая принимает в качестве
аргументов некую функцию (обозначим ее func) и имя глобальной переменной
(обозначим её counter_name), возвращая новую функцию, которая ведет себя
в точности как функция func, за тем исключением, что всякий раз при вызове
инкрементирует значение глобальной переменной с именем counter_name.
'''

import inspect


def make_it_count(func, counter_name):
    func_args = inspect.getfullargspec(make_it_count)[0]
    def new_func(*func_args):
        globals()[counter_name] += 1
        func(*func_args)
    return new_func

# example


def smth_f(smth):  # test function
    print("I have", smth, "problems but Python ain't one")


problems = 0  # test global var



smth_f(1)

new_func = make_it_count(smth_f, "problems")

new_func(10)
new_func(99)
print(problems)
