from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class FlyingAnimal(Animal):
    @abstractmethod
    def fly(self):
        pass


class Bird(FlyingAnimal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def make_sound(self):
        print(f"{self.name} is making a bird sound")

    def fly(self):
        print(f"{self.name} is flying with wingspan {self.wingspan}")


class Bat(FlyingAnimal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def make_sound(self):
        print(f"{self.name} is making a bat sound")

    def fly(self):
        print(f"{self.name} is flying with wingspan {self.wingspan}")


class Penguin(Animal):
    def make_sound(self):
        print(f"{self.name} is making a penguin sound")


bird = Bird("Sparrow", 20)
bat = Bat("Fruit Bat", 30)
penguin = Penguin("Emperor Penguin")

bird.make_sound()
bird.fly()

bat.make_sound()
bat.fly()

penguin.make_sound()
