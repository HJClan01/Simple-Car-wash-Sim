import random
class Dryer:
  
  """Constructor initializes settings, dryer rate, current dry task, and time remaining until a dryer task has finished
  
  dryer rate: determines the time it takes for the dryer to complete tasks

  current_dry_ task: tracks whether or not the dryer has a car 

  time_remianing: determines the timr remaing on current_task if there is one"""
  
  
  def __init__(self, drm):
    self.dryer_time_left = 0
    self.current_dry_task = None 
    self.dryer_rate = drm


  """Defines internal timer"""
  def timer(self):
    if self.current_dry_task != None:
       self.dryer_time_left = self.dryer_time_left - 1
       if self.dryer_time_left <= 0:
         self.current_dry_task = None

  """Determines if the dryer has a car and is "busy" refrences current_dry_task """
  def dryer_busy(self):
    if self.current_dry_task != None:
      return True
    else:
      return False
  
  """Determines when a dryer will start, making the current dry task = next dry, and calculates time left by refrenceing .get_amt_cars() multiplying it by 60 and dividing it by the dryer rate """
  def start_next_dry(self, next_dry):
    self.current_dry_task = next_dry
    self.dryer_time_left  = next_dry.get_amt_cars() * 30 / self.dryer_rate
  

    


