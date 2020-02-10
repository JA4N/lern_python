class Cuboid:

    def __init__(self, length=0, width=0, height=0):
        self.__length = length
        self.__width = width
        self.__height = height

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def surface(self):
        return self.__length * self.__width * 6

    def volume(self):
        return self.surface() * self.__height


if __name__ == "__main__":
    cuboid1 = Cuboid(10, 20, 5)
    print(cuboid1.surface())
    print(cuboid1.volume())

    cuboid2 = Cuboid()
    print(cuboid2.surface())
    print(cuboid2.volume())

    cuboid3 = Cuboid(40, 5)
    print(cuboid3.surface())
    print(cuboid3.volume())
