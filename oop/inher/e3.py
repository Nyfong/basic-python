#all class that have __init method must call super().__init__() to initialize parent class 
#cuz the __inint will call it self when object is created
#All classes have a method called __init__(), which is always executed when the class is being initiated.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#p1 = Person()
# print(p1.name) error: missing 2 required positional arguments: 'name' and 'age'

#coreect way to create an instance of Person
p1 = Person("John", 36)
print(p1.age, p1.name)