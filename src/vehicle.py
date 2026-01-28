class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.brand} {self.model}: Engine started")

    def stop_engine(self):
        print(f"{self.brand} {self.model}: Engine stopped")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
