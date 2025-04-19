
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 10  # Very hungry
        self.energy = 0   # Tired
        self.happiness = 0
        self.tricks = []  # For bonus methods


    def eat(self):
        self.hunger = max(0, self.hunger - 5)  # Reduce hunger by 5, not below 0
        self.happiness += 1
