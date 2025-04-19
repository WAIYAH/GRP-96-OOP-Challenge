
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


    def sleep(self):
        self.energy = max(0, self.energy - 5)  # Reduce energy by 5, not below 0
        self.happiness += 2
        self.hunger += 1


    def get_status(self):
        print(f"Pet: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        

            
    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")


    def show_tricks(self):
        if self.tricks:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")






