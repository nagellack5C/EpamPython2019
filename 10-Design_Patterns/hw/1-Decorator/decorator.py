"""
Используя паттерн "Декоратор" реализуйте возможность дополнительно добавлять к кофе
    маршмеллоу, взбитые сливки и сироп, а затем вычислить итоговую стоимость напитка.
"""


class Component:
    def get_cost(self):
        raise NotImplementedError("Override get_cost method")


class BaseCoffee(Component):
    def get_cost(self):
        return 90


class Decorator(Component):
    _component = None

    def __init__(self, component):
        self._component = component

    def add_cost(self):
        raise NotImplementedError("Override add_cost method")

    def get_cost(self):
        return self.add_cost() + self._component.get_cost()


class Whip(Decorator):
    def add_cost(self):
        return 30


class Marshmallow(Decorator):
    def add_cost(self):
        return 40


class Syrup(Decorator):
    def add_cost(self):
        return 50


if __name__ == "__main__":
    coffee = BaseCoffee()
    coffee = Whip(coffee)
    coffee = Marshmallow(coffee)
    coffee = Syrup(coffee)
    print("Итоговая стоимость за кофе: {}".format(str(coffee.get_cost())))
