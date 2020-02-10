class Rectangle:

    def __init__(self, length=0, width=0):
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def surface(self):
        return self.__length * self.__width


if __name__ == "__main__":
    rectangle1 = Rectangle(10, 20)
    print(rectangle1.surface())

    rectangle2 = Rectangle()
    print(rectangle2.surface())

    rectangle3 = Rectangle(40)
    print(rectangle3.surface())
