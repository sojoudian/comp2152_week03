# Dice Options created using list() and range()
diceOptions = list(range(1, 7))

# Weapons list
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

print("Available Weapons: ", ', '.join(weapons))

def getCombatStrength(prompt):
    while True:
        value = int(input(prompt))
        if 1 <= value <= 6:
            return value
        else:
             print("Invalid Input! Please enter a number between 1-6")