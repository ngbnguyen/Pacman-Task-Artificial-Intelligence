# The order of output 1 and 2 are different because: 
#   In the output 1, the lines of code are executed sequentially
#   In the output 2, when doing multithreading, threads will be run concurrently 
#       and each part can handle different task at the same time, 
#       to make best use of available resources (CPU).
# Therefore, the output order of output 2 will not be the same as output 1

# In order to make sure that the output order of output 1 and output 2 is the same we can add 
# the line of code: "time.sleep(2)" in order to delay the time of execution

# Question 2
from threading import Thread
import random , time

class Car2(Thread):
    # Class attributes
    wheels = 4
    doors = 4
    seats = 5
    
    # Initialize with instance attributes
    def __init__(self, maxSpeed):
        super(Car2, self).__init__()
        self.maxSpeed = maxSpeed
        
    # List out all the characteristics of the car
    def info(self):
        print(f"wheels = ", self.wheels)
        print(f"doors = ", self.doors)
        print(f"seats = ", self.seats)
        print(f"maxSpeed = ", self.maxSpeed)
    
    # print out the mas speed of the car in a loop of 10 times
    def run(self):
        speed_list = []
        for i in range(10):
            n = int(random.random() * self.maxSpeed)
            speed_list.append(n)
        self.info()
        print(f"The max speed of the car in a loop of 10 times: maxSpeed= {max(speed_list)}")
        
    
print("--------------- Car BWM --------------")
carBMW = Car2(200)
carBMW.start()
time.sleep(2)
print("--------------- Car Toyota --------------") 
carToyota = Car2(100)
carToyota.start()


