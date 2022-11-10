# WARNING: MR. TENNYSON, SOME PRINT STATMENTS MAY LOOK ODD OR HARD TO READ, STARTED TO EXPERIMENT WITH SOME LIBRAIES EFFECTING THE FORMAT OF THE TEXT IN THE CONSOLE

import random
import datetime
import os 
from queue import Queue 
from car import Car 
from wash import CarWash
from dryer import Dryer 
from colored_strings import colors

"""
Simulation: On any day n amount of cars can come to the car wash. The car wash simulation will run for "100 minutes" for 5 cars per minute.

Dryer Simulation: Along with Henry's Car Wash, The extra dry speed dryer™  is simalar to the car wash simulation, but with different varibles and constants. It will run for the same amount of time as the car wash but can dry 13 cars per minute

"""

def wash_simulation(num_minutes, cars_per_minute):
  """
  Establishes Car Wash Simulation, runs for number of minututes and cars per minute as parameters
  
  num_minutes: int() of number of minutes the car wash will "run" for 
  cars_per_min: int() how many cars can be washed per minute 

  returns:
  None
  """

  henrys_car_wash = CarWash(cars_per_minute) # sets henry's car wash as a CarWash Class 
  car_queue = Queue()
  waiting_times = [] #list to appened waiting times to, to then get the average 
  avg_sim_wait_times = [] # not implemented yet
  j = 0 # nit implemented, but sets j to 0 in order to add 1 everytime in order to print a message after n loops 


  for current_min in range(num_minutes): # loops for each minute for the number of minutes defined 
    if wash_new_car(): # refrences 
      car = Car(current_min)
      car_queue.enqueue(car)


    if (not henrys_car_wash.busy()) and (not car_queue.is_empty()): # as long as the car wash isn't busy and queue is empty, the car wash can start washing a new car 
      next_wash = car_queue.dequeue()
      waiting_times.append(next_wash.wait_time(current_min))
      avg_sim_wait_times.append(next_wash.wait_time(current_min))
      henrys_car_wash.start_next_wash(next_wash)
    
    henrys_car_wash.internal_time() 
    
  

  #if car has more dirt it will take longer to wash
  avg_wait_time = sum(waiting_times) * car.dirt /len(waiting_times)
  j = j + 1

  # calcuates wait time in minutes 
  num_in_mins = avg_wait_time / 60
  # formats string, bolds and changes "CAR WASH" to Cyan 
  # also formats numbers to only have 4 decimal places 
  num_mins_formatted = "{:.4f}".format(num_in_mins)
  print(f'\n{colors.BOLD}{colors.OKCYAN}CAR WASH:{colors.ENDC} Average wait for wash: {num_mins_formatted} minutes, {car_queue.size()} cars remaining')
  # if j == 9:
  #   print(f'\n (*) Average wait time for the car wash today: {sum(avg_sim_wait_times) / len(avg_sim_wait_times)}')





def dryer_sim(num_minutes, dries_per_min):
  """Establishes Car Wash Simulation, runs for number of minututes and cars per minute as parameters
  

  num_minutes: int() of number of minutes the dryer will "run" for 
  dries_per_min: int() how many cars can be washed per minute 


  returns: 
  None
  """
  car_dryer = Dryer(dries_per_min) 
  dryer_queue = Queue()
  dryer_wait_times = []

  

  for current_min in range(num_minutes): # loops for each minute for the number of minutes defined 
    
    if new_dry_task(): # refrences new_dry_task function and is a boolean asking if new_dry_task() is True   
      washed_car = Car(current_min)

      dryer_queue.enqueue(washed_car)
    
    if (not car_dryer.dryer_busy()) and (not dryer_queue.is_empty()): # If dryer isnt busy start new car 
      next_dry = dryer_queue.dequeue() 
      dryer_wait_times.append(next_dry.wait_time(current_min))
      car_dryer.start_next_dry(next_dry)

    car_dryer.timer()

  # calculates avg wait time for dryer by getting the sum of the list dryer_wait_times and multiplying that by cars wetness then dividing it by the amount of times 
  avg_dryer_wait = sum(dryer_wait_times) * washed_car.wet / len(dryer_wait_times)

  # converts time to mins 
  time_mins = avg_dryer_wait / 60
  #formats time_mins to have 4 decimal places 
  time_mins_formatted = "{:.4f}".format(time_mins)

  #(colors.() is a class that changes the properties of words, .ENDC ends that change )
  print(f'\n{colors.UNDERLINE}{colors.YELLOW}Dryer:{colors.ENDC} Average wait for the wet cars: {time_mins_formatted} minutes\n {dryer_queue.size()} cars remaining to dry ')
    


# decides if a new car will be washed 
def wash_new_car():
  num = random.randrange(1, 8)
  if num == 7:
    return True
  else:
    return False

# decides if a car will be dried 
def new_dry_task():
  number = random.randrange(1, 9)
  return True if number == 8 else False
  

# function that uses os library to clear the console for clearity and cleanliness 
def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):  
    command = 'cls'
  os.system(command)



#add sim for weekend v weekday??


# constants and variable defining 
n = 0
global num_minutes
num_minutes = 100
dries_per_min = 13 
cars_per_minute = 5
now = datetime.datetime.now()

#starts simulation and calls functions to start 
for i in range(10):
    if n == 0: #with 0 iterations at the beginning print car wash is open
      clearConsole()
      print(f""" {colors.HEADER}Henry's car wash is now open for {now.strftime("%A")}{colors.ENDC}""")
    wash_simulation(num_minutes, 5)
    dryer_sim(num_minutes, dries_per_min)
    n += 1
    if n == 10: #after 10 interations, print the wash is clsoed 
     print("\nHenry's Car Wash is now closed")
  






