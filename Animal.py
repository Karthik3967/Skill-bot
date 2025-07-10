class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Boww")
class Cat(Animal):
    def sound(self):
        print("Meooooww")
for v in [Dog(),Cat()]:
    v.sound()        