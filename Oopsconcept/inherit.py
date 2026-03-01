class animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes sound")

class Cat(animal):

    def speak(self):
        super().speak()
        print(f"{self.name} meos")

# mammal = animal("Kitty")
# mammal.speak()


cat = Cat("pussy")
cat.speak()

    