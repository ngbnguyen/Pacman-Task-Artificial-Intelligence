import random 
#Question 1: 
# A class with one class attribute
class Car:
    
    # Class attributes
    wheels = 4
    doors = 4
    seats = 5
    
    # Initialize with instance attributes
    def __init__(self, maxSpeed):
        
        self.maxSpeed = maxSpeed
    
    # List out all the characteristics of the car
    def info(self):
        print(f"wheels = ", self.wheels)
        print(f"doors = ", self.doors)
        print(f"seats = ", self.seats)
        print(f"maxSpeed = ", self.maxSpeed)
    
    
    # print out the mas speed of the car in a loop of 10 times
    # I will generate randomly speed of the car in each iteration
    # And append it to a speed_list 
    # After that, print out the max speed in a loop of 10 times.
    def run(self):
        speed_list = []
        for i in range(10):
            n = int(random.random() * self.maxSpeed)
            speed_list.append(n)
        self.info()
        print(f"The max speed of the car in a loop of 10 times: {max(speed_list)}")
        
    
# class CarBMW inherit class Car        
class CarBMW(Car):
    # A BWM Car is a car with maxSpeed = 200
    maxSpeed = 200
    
    def __init__(self):
        pass
    
    def run(self):
        speed_list = []
        for i in range(10):
            n = int(random.random() * self.maxSpeed)
            speed_list.append(n)
        self.info()
        print(f"The max speed of the BWM car in a loop of 10 times: {max(speed_list)}")
                
# class CarToyata inherit class Car  
class CarToyota(Car):
    
    # A Toyota Car is a car with maxSpeed = 100
    maxSpeed = 100
    def __init__(self):
        pass
        
    def run(self):
        speed_list = []
        for i in range(10):
            n = int(random.random() * self.maxSpeed)
            speed_list.append(n)
        self.info()
        print(f"The max speed of the Toyota car in a loop of 10 times: {max(speed_list)}")
        

print("--------------- Car BWM --------------")    
carBMW = CarBMW()
carBMW.run()


print("--------------- Car Toyota --------------") 
carToyota = CarToyota()
carToyota.run()

