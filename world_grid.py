import random
from bacteria import Bacteria
from food import Food


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bacteria_list = []
        self.food_list = []

    def add_bacteria(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.bacteria_list.append(Bacteria(x, y))

    def add_food(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.food_list.append(Food(x, y))

    def initialise_simulation(self):
        nb_bact = random.randint(5, 10)
        for _ in range(nb_bact):
            x = random.randint(0, self.width - 1)   # <- ważne: -1
            y = random.randint(0, self.height - 1)  # <- ważne: -1
            self.add_bacteria(x, y)

    def initialise_food(self):
        food_init = random.randint(5, 10)
        for _ in range(food_init):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.add_food(x, y)

    def update(self):
        for b in self.bacteria_list[:]:
            b.move(self)
            b.eat(self)
            b.age_up()