#parent class

class Animal:
    def __init__(self,name ):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")
        
#child class

class Pig(Animal):
    def __init__(self):
        super().__init__("Pig")
    
    def speak(self):
        print(f"{self.name} makes a sound")
        
        
#create instance of Pig

pigI = Pig()
pigI.name = "Piggy"
#call speak method
pigI.speak()