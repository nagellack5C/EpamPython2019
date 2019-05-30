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
