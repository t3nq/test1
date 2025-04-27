import random


class Randomizer:
    def __init__(self, x, y):
        self.border1 = x
        self.border2 = y
        self.value = self.__get_random_value()

    def __get_random_value(self):
        return random.randint(self.border1, self.border2)

    def get_value(self):
        return self.value


a = int(input("введите число"))
b = int(input("введите число")) 
randomizer = Randomizer(a, b)
result = randomizer.get_value()
print("Ваше число:", result)
