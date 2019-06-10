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
    class Enhanced(cls):
        count = 0

        def __new__(cls, *args, **kwargs):
            cls.count += 1
            return super().__new__(cls)

        @classmethod
        def get_created_instances(cls):
            return cls.count

        @classmethod
        def reset_instances_counter(cls):
            oldcount, cls.count = cls.count, 0
            return oldcount

    return Enhanced


@instances_counter
class User:
    pass


if __name__ == '__main__':

    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print("must be 3:", user.get_created_instances())  # 3
    user, _, _ = User(), User()
    print("must be 6:", user.get_created_instances())  # 3
    user.reset_instances_counter()  # 3
