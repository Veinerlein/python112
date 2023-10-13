class CarClass:
    def __init__(self, brand, model, year, probig):
        self.brand = brand
        self.model = model
        self.year = year
        self.probig = probig

    def show_car(self):
        print(f"{self.brand},{self.model},{self.year},{self.probig},")


if __name__ == '__main__':
    e = CarClass("Tesla", "T", 2020, 50000)
    e.show_car()
