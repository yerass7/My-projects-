from src.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, doors, transmission):
        super().__init__(brand, model, year)
        self.doors = doors
        self.transmission = transmission

    def start_engine(self):
        print(f"Car {self.brand} {self.model}: Engine started automatically")

