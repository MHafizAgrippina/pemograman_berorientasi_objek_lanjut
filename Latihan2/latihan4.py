class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def get_name(self):
        return print (self.name)
    def get_color(self):
        return print (self.color)

class Mammal(Animal):
    def __init__(self, name, color, fur):
        super().__init__(name, color)
        self.fur = fur
    def get_fur(self):
        return print (self.fur)

class Bird(Animal):
    def __init__(self, name, color, wingspan):
        super().__init__(name, color)
        self.wingspan = wingspan
    def get_wingspan(self):
        return print (self.wingspan)

# Hierarchical Inheritance
class Reptile(Mammal):
    def __init__(self, name, color, fur, scale):
        super().__init__(name, color, fur)
        self.scale = scale
    def get_scale(self):
        return print (self.scale)
    
reptile = Reptile("Cobra", "Black", "Besar", "5m")
reptile.get_name()
reptile.get_color()
reptile.get_fur()
reptile.get_scale()