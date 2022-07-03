class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} bark {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound='Bark'):
        return super().speak(sound)

dog = GoldenRetriever('Hindi', 2)
print(dog, "\n", dog.speak())

