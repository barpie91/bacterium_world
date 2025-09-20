import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

class Bacteria:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.age = 0

  def move(self, bacteria_list):
    direction = random.randint(0, 4)
    if direction == 0:
      if not (self.x, self.y +1) in bacteria_list:
        self.y += 1
    elif direction == 1:
      if not (self.x, self.y -1) in bacteria_list and self.y != 0:
        self.y -= 1
      elif not (self.x, self.y -1) in bacteria_list and self.y == 0:
        self.y = self.y
    elif direction == 2:
      if not (self.x+1, self.y) in bacteria_list:
        self.x += 1
    elif direction == 3:
      if not (self.x-1, self.y) in bacteria_list and self.x != 0:
        self.x -= 1
      elif not (self.x-1, self.y) in bacteria_list and self.x == 0:
        self.x = self.x

  def age_add(self):
    for bact in grid.bacteria_list:
      for food in grid.food_list:
        if bact.x == food.x and bact.y == food.y:
          bact.age += 1