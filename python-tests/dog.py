class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} (age {self.age}) says Woof!")


rex= Dog("Rex",3)
rex.speak()
