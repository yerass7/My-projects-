from src.car import Car
from src.motorcycle import Motorcycle
from src.garage import Garage
from src.fleet import Fleet

# Vehicles
car1 = Car("Toyota", "Camry", 2022, 4, "Automatic")
car2 = Car("BMW", "X5", 2021, 4, "Automatic")
moto1 = Motorcycle("Yamaha", "R1", 2020, "Sport", False)

# Garages
garage1 = Garage("Central Garage")
garage2 = Garage("VIP Garage")

garage1.add_vehicle(car1)
garage1.add_vehicle(moto1)
garage2.add_vehicle(car2)

# Fleet
fleet = Fleet()
fleet.add_garage(garage1)
fleet.add_garage(garage2)

garage1.list_vehicles()
garage2.list_vehicles()

car1.start_engine()
moto1.start_engine()

fleet.find_vehicle("BMW")

garage1.remove_vehicle(moto1)
fleet.remove_garage(garage2)
