class Rectangle:
    def __init__(self, a, b):
        self.side1 = a
        self.side2 = b

    def perimetr(self):
        return (self.side1 + self.side2) * 2

    def square(self):
        return self.side1*self.side2

    def show_sides(self):
        print(f"Side a: {self.side1}\nSide b: {self.side2}")


    def get_rect_perimetr(self):
        return self.perimetr()



def main():
    rect = Rectangle(3, 7)
    print(f"Площа == {rect.square()}")
    print(f"Периметр == {rect.perimetr()}")
    rect.show_sides()

if __name__=="__main__":
    main()
