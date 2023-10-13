from les.shape.rectangle import Rectangle
from les.shape.circle import Circle


class Cylinder(Rectangle, Circle):
    def __init__(self, a, r):
        super().__init__(a, r)
        self.high = a
        self.radius = r

    def v_of_cylynder(self):
        # PIr**2*h
        return (self.radius ** 2) * self.PI * self.high

    def show_sides(self):
        print(f"Основа: {self.radius}\nВисота: {self.high}")

    def get_volume(self):
        return self.v_of_cylynder()


def main():
    cylinder = Cylinder(4, 7)
    print(f"Об'єм циліндру: {cylinder.v_of_cylynder()}")
    cylinder.show_sides()


if __name__ == "__main__":
    main()
