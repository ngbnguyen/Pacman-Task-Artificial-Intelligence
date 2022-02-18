# Question 2
from threading import Thread
import random

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



print("--------------- Car Toyota --------------") 
carToyota = Car2(100)
carToyota.start()


