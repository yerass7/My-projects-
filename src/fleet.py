class Fleet:
    def __init__(self):
        self.garages = []

    def add_garage(self, garage):
        self.garages.append(garage)
        print(f"Garage '{garage.name}' added to fleet")

    def remove_garage(self, garage):
        if garage in self.garages:
            self.garages.remove(garage)
            print(f"Garage '{garage.name}' removed from fleet")

    def find_vehicle(self, brand):
        for garage in self.garages:
            for vehicle in garage.vehicles:
                if vehicle.brand == brand:
                    print(f"{vehicle} found in garage '{garage.name}'")
                    return vehicle
        print("Vehicle not found")
        return None
