from pet import Pet

# Create a pet named Mypuppy
pet = Pet("Mypuppy")

# Test all methods
print("Initial state:")
pet.get_status()

print("\nAfter eating:")
pet.eat()
pet.get_status()

print("\nAfter sleeping:")
pet.sleep()
pet.get_status()

print("\nTraining:")
pet.train("sit")
pet.train("roll over")

print("\nShowing tricks:")
pet.show_tricks()
