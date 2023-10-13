class Circle:
    PI = 3.14

    def __init__(self, r):
        self.radius = r

    def __str__(self):
        return f"Circle with  {self.square()}"

    def v_of_circle(self):
        # 2PIr
        return self.radius * 2 * self.PI

    def square(self):
        # PIr**2
        print(self.PI * self.radius ** 2)
        return self.PI * self.radius ** 2

    def show_sides(self):
        print(f"У кола радіус: {self.radius}")

    def get_circle_square(self):
        return int(self.square())


circles = [Circle(4), Circle(2), Circle(6), Circle(8), Circle(1)]


def main():
    # circle = Circle(4)
    # print(f"Обєм (довжина лінії) кола: {circle.v_of_circle()}")
    # print(f"Площа круга: {circle.square()}")
    # circle.show_sides()
    # print(circle.get_circle_square())
    circle_max_s = max(circles, key=lambda c: c.get_circle_square())
    print(circle_max_s)


if __name__ == "__main__":
    main()
