class Cat:
    species = "mammal"
    def __init__(self, name):
        self.name = name

a = Cat("Tom")
b = Cat("Jerry")
a.species = "alien"

print(a.species)  # Output: alien
print(b.species)  # Output: mammal
