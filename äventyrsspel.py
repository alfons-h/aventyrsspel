name = input("Vad heter du?--> ")
print("Välkommen " + name + " till grottkravlare.")

class Player:
    def __init__(self, name, lvl, hp):
        self.name = name.capitalize()
        self.hp = hp
        self.lvl = lvl
        print()
        print("     Spelar Stats     ")
        print("══════════════════════")
        print("Player Name: " + (self.name))
        print("Player HP: " + str(self.hp))
        print("Level: " + str(self.lvl))

player = Player(name, 1, 100)

class Inventory:
    def __init__(self):
        self.items = {}  
        
    def add_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print(f"Lade till {quantity} {item_name} till inventariet")

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if self.items[item_name] > quantity:
                self.items[item_name] -= quantity
                print(f"{quantity} {item_name} togs bort")
            elif self.items[item_name] == quantity:
                del self.items[item_name]
                print(f"{quantity} {item_name} togs bort och finns inte längre i inventariet")
            else:
                print(f"Inte tillrräkligt med {item_name} för att ta bort. Bara {self.items[item_name]} är tillgängliga.")
        else:
            print(f"{item_name} hittades inte")

            

class Monster:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl

    def __str__(self):
        return f"{self.name}: HP {self.hp}, Level {self.lvl}"

rat = Monster("Rat", 3, 1)
slime = Monster("Slime", 10, 3)
goblin = Monster("Goblin", 25, 7)
zombie = Monster("Zombie", 50, 10)
ghost_knight = Monster ("Ghost Knight", 75, 12)
vampire = Monster("Vampire", 100, 15)
werewolf = Monster ("Werewolf", 150, 20)
dragon = Monster("Dragon", 500, 100)