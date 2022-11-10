import random 

"""Class for cars establishing time, cars, dirtiness, and wetness"""


class Car:
  def __init__(self, time):
    self.timestamp = time
    self.cars = random.randrange(1, 5)
    self.dirt = random.randrange(1,20)
    self.wet = random.randrange(1,11)

  """method for time stamp of a car refrencing timestamp"""
  def get_tstamp(self):
    return self.timestamp
  """creates .get method for the amount of cars"""
  def get_amt_cars(self):
    return self.cars
  

  """returns wait time of the cars based on time and current time"""
  def wait_time(self, current_time):
    return current_time - self.timestamp
