class Car(object):
    """A simple attempt to represent a Car"""
    def __init__(self,make,model,year):
        """Initialize attributes to make a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        """Personlised greeting to the user"""
        print("This car has " + str(self.odometer_reading) + "miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
       self.odometer_reading += mileage
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

 

