"""
The Carwash class tracks and defines info about it, such as cars per minute, an internal timer, if it is busy or not, and starting another wash task 


"""
class CarWash:
  """
  Contructior initializing cars per minute, current wash, and time left 


  car_rate: determiens rate of cars 
  current_wash = if there is a car being washed or not, of not it is None

  time_left: determines time remaining on current wash

  
  """
  def __init__(self, cpm):
    self.car_rate = cpm
    self.current_wash = None
    self.time_left = 0
  """
  defines internal_time for for wash 
  
  """
  def internal_time(self):
    if self.current_wash != None:
      self.time_left = self.time_left - 1
      if self.time_left <= 0:
        self.current_wash = None
  
  # determines if wash has a task and is busy refrences current wash 

  def busy(self):
    if self.current_wash != None:
      return True
    else:
      return False

  """Determines when a wash will start, amking the current wash = new wash, amd calculates time left by refrenceing .get_amt_cars() multiplyinh iy by 60 and dividing it by the car rate """
  def start_next_wash(self, new_wash):
    self.current_wash = new_wash
    self.time_left = new_wash.get_amt_cars() * 60 / self.car_rate