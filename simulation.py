from world_grid import Grid
import time
#import importlib
#import inspect

"""
m = importlib.import_module(Grid.__module__)
print("Grid class comes from module:", Grid.__module__)
print("Module file:", m.__file__)
print("Grid has update():", hasattr(Grid, "update"))
print("Grid methods:", [name for name, _ in inspect.getmembers(Grid, inspect.isfunction)])
"""

def run_simulation():
    grid = Grid(10, 10)

    grid.initialise_simulation()
    grid.initialise_food()

    steps = 20

    for step in range(steps):
        print(f"\nStep {step}")

        # update
        grid.update()

        # print state
        for b in grid.bacteria_list:
            print(f"Bacteria at ({b.x},{b.y}) age={b.age}")

        # food info
        print(f"Food count: {len(grid.food_list)}")

        time.sleep(0.5)


if __name__ == "__main__":
    run_simulation()