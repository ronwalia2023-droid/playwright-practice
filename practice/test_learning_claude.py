class Dog:
    def __init__(self, name , age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"{self.name} says fuck you! and he is a {self.breed}.")
    

my_dog = Dog("Buddy", 3, "Golden Retriever")
my_dog.bark()
