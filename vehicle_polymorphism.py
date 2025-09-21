class Vehicle:
    def move(self):
        print("Vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print(" Driving on the road")

class Plane(Vehicle):
    def move(self):
        print(" Flying through the sky")

class Boat(Vehicle):
    def move(self):
        print(" Sailing across the water")
