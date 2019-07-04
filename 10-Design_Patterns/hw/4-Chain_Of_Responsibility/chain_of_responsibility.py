"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла

В итоге мы должны получить список недостающих ингридиентов.
"""


class FridgeHandler:

    _next_handler = None

    def __init__(self, food_type, amount):
        self.food_type = food_type
        self.amount = amount

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, fridge, history=None):
        if not history:
            history = []
        if fridge[self.food_type] < self.amount:
            history.append(self.food_type)
        if self._next_handler:
            self._next_handler.handle(fridge, history)
        else:
            if not history:
                print("You're good! Go bake!!!")
            else:
                print("You're missing something. Go shopping and buy the following:")
                for h in history:
                    print(h)


perfect_fridge = {
    "eggs": 2,
    "dough": 300,
    "milk": 0.5,
    "sugar": 100,
    "oil": 10,
    "butter": 120
}

bad_fridge = {
    "eggs": 3,
    "dough": 200,
    "milk": 0.6,
    "sugar": 10,
    "oil": 0,
    "butter": 1200
}

eggs_handler = FridgeHandler("eggs", 2)
dough_handler = FridgeHandler("dough", 300)
milk_handler = FridgeHandler("milk", 0.5)
sugar_handler = FridgeHandler("sugar", 100)
oil_handler = FridgeHandler("oil", 10)
butter_handler = FridgeHandler("butter", 120)
eggs_handler.set_next(dough_handler).set_next(milk_handler)\
    .set_next(sugar_handler).set_next(oil_handler).set_next(butter_handler)

eggs_handler.handle(perfect_fridge)
eggs_handler.handle(bad_fridge)
