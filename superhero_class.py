class Character:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def introduce(self):
        print(f"Hi, I'm {self.name} from {self.origin}.")

class Superhero(Character):
    def __init__(self, name, origin, power, secret_identity):
        super().__init__(name, origin)
        self.power = power
        self.__secret_identity = secret_identity  

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

    def reveal_identity(self):
        print(f"{self.name}'s secret identity is {self.__secret_identity}")
