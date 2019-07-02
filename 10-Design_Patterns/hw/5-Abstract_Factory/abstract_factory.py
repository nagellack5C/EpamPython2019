"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.

С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.

"""

from abc import ABC, abstractmethod


# quick & dirty meal searching, yaml is a non-standard lib
def get_meal(day, menu, kind):

    with open("menu.yml") as menu_file:
        for i in menu_file:
            if day in i:
                break
        for i in menu_file:
            if kind in i:
                break
        for i in menu_file:
            if menu in i:
                return i.split(": ")[1][1:-2]


class AbstractLunchFactory(ABC):

    @abstractmethod
    def create_vegan_lunch(self):
        pass

    @abstractmethod
    def create_child_lunch(self):
        pass

    @abstractmethod
    def create_china_lunch(self):
        pass


class ConcreteLunchFactory(AbstractLunchFactory):

    def __init__(self, day):
        self.day = day

    def create_vegan_lunch(self):
        return VeganLunch(self.day)

    def create_child_lunch(self):
        return ChildLunch(self.day)

    def create_china_lunch(self):
        return ChinaLunch(self.day)


class Meal:

    def __init__(self, day, menu, kind):
        self.meal_name = get_meal(day, menu, kind)

    def __str__(self):
        return self.meal_name


class AbstractLunch(ABC):

    def __init__(self, day):
        self.day = day
        self.meals = []

    @abstractmethod
    def create_first_meal(self):
        pass

    @abstractmethod
    def create_second_meal(self):
        pass

    @abstractmethod
    def create_drink(self):
        pass

    def __str__(self):
        return f"{self.meals[0]}\n{self.meals[1]}\n{self.meals[2]}"


class VeganLunch(AbstractLunch):

    def create_first_meal(self):
        self.meals.append(Meal(self.day, "vegan", "first"))

    def create_second_meal(self):
        self.meals.append(Meal(self.day, "vegan", "second"))

    def create_drink(self):
        self.meals.append(Meal(self.day, "vegan", "drink"))


class ChildLunch(AbstractLunch):

    def create_first_meal(self):
        self.meals.append(Meal(self.day, "child", "first"))

    def create_second_meal(self):
        self.meals.append(Meal(self.day, "child", "second"))

    def create_drink(self):
        self.meals.append(Meal(self.day, "child", "drink"))


class ChinaLunch(AbstractLunch):

    def create_first_meal(self):
        self.meals.append(Meal(self.day, "china", "first"))

    def create_second_meal(self):
        self.meals.append(Meal(self.day, "china", "second"))

    def create_drink(self):
        self.meals.append(Meal(self.day, "china", "drink"))


if __name__ == "__main__":
    lunch_factory = ConcreteLunchFactory("Tuesday")

    lunch_1 = lunch_factory.create_china_lunch()
    lunch_1.create_first_meal()
    lunch_1.create_second_meal()
    lunch_1.create_drink()
    print("Lunch 1")
    print(lunch_1)
    print("--------")


    lunch_factory_2 = ConcreteLunchFactory("Monday")
    lunch_2 = lunch_factory_2.create_child_lunch()
    lunch_2.create_first_meal()
    lunch_2.create_second_meal()
    lunch_2.create_drink()
    print("Lunch 2")
    print(lunch_2)
    print("--------")