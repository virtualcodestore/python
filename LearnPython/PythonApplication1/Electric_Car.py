from Car import Car

class Battery():
    """Battery Class"""
    def __init__(self,battery_size = 80):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """Battery Range"""
        if self.battery_size == 80:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """Representaspects of a car, specif to electric vehicles"""
    def __init__(self,make,model,year):
        """Initialise attributes of the parent class."""
        super().__init__(make,model,year)
        self.battery = Battery()

 

