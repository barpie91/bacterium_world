import random

class Bacteria:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0

    def move(self, grid):
        direction = random.randint(0, 3)

        new_x, new_y = self.x, self.y

        if direction == 0:
            new_y += 1
        elif direction == 1:
            new_y -= 1
        elif direction == 2:
            new_x += 1
        elif direction == 3:
            new_x -= 1

        if 0 <= new_x < grid.width and 0 <= new_y < grid.height:

            # collision check
            if not any(b.x == new_x and b.y == new_y for b in grid.bacteria_list):
                self.x = new_x
                self.y = new_y

    def age_up(self):
        self.age += 1

    def eat(self, grid):
        for food in grid.food_list:
            if self.x == food.x and self.y == food.y:
                self.age = max(0, self.age - 1)
                grid.food_list.remove(food)
                break
