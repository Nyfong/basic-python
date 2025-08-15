# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Child class inherits from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

# Using the classes
my_dog = Dog("Buddy")
my_dog.speak()  # Buddy barks
