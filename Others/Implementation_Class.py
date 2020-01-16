class Car:

    def __init__(self):
        self.rpm = 0
        self.speed = 0
        self.gear = 0
    
    def change_rpm(self, new_value):
        self.rpm = new_value

    def shift(self, new_value):
        self.gear = new_value

    def apply_brakes(self, decrement):
        self.speed = self.speed - decrement

#Create two different car objects
car1 = Car()
car2 = Car()

#Invoke methods on those objects
car1.change_rpm(2500)
car1.shift(2)

car2.change_rpm(2500)
car2.shift(2)
car2.change_rpm(4000)
car2.apply_brakes(200)