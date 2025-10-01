import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage. {self.health} and {enemy.health}" )

def battle(character1, character2):
    while character1.is_alive() and character2.is_alive():
        character1.attack_enemy(character2)
        if character2.is_alive():
            character2.attack_enemy(character1)

    if character1.is_alive():
        print(f"{character1.name} defeats {character2.name}!")
    else:
        print(f"{character2.name} defeats {character1.name}!")

# Create characters
godzilla = Character("Godzilla", 20, 20, 10)
ghidorah = Character("Ghidorah", 15, 20, 10)

# Start the battle
battle(godzilla, ghidorah)
print(godzilla.health , godzilla.defense)
print(ghidorah.health , ghidorah.defense)