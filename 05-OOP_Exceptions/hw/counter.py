"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    count = 0

    class Enhanced(cls):

        def __init__(self):
            nonlocal count
            count += 1

        def get_created_instances(self=None):
            nonlocal count
            return count

        def reset_instances_counter(self):
            nonlocal count
            oldcount, count = count, 0
            return oldcount

    return Enhanced


@instances_counter
class User:
    pass



if __name__ == '__main__':

    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print("must be 3:", user.get_created_instances())  # 3
    user.reset_instances_counter()  # 3