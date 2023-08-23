from les.car import carclass

class Electrocar(carclass.CarClass):
    def __init__(self, brand, model, year, probig):
        super().__init__(brand, model, year, probig)
        self.battery = 100

    def show_car(self):
        print(f"{self.brand},{self.model},{self.year},{self.probig},")

    def description_battery(self):
        print(f"This cas has power: {self.battery}%")