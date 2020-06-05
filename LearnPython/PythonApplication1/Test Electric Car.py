from Car import Car
from Electric_Car import ElectricCar

my_tesla = ElectricCar('Tesla','Model S',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_beettle = Car('volkwagen','Beetle',2018)
print(my_beettle.get_descriptive_name())

print("End")
