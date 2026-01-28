class Garage:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"{vehicle} added to garage '{self.name}'")

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            print(f"{vehicle} removed from garage '{self.name}'")

    def list_vehicles(self):
        print(f"\nGarage: {self.name}")
        for vehicle in self.vehicles:
            print("-", vehicle)
