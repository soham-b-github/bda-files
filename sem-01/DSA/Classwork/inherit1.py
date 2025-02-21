# abc = abstract base class
from abc import ABC, abstractmethod

class Animal(ABC):

    # an abstract class forces the developer to implement the methods
    @abstractmethod # this is called a "decorator"
    def movement(self):
        pass


class Dog(Animal):
    def movement(self):
        print("walks")


class Fish(Animal):
    def movement(self):
        print("swims")


