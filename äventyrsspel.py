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
        print("Player name: " + (self.name))
        print("Player hp: " + str(self.hp))
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

            

class Creature:
    def __init__(monster,name,hp,lvl):
        monster.name = name
        monster.hp = hp
        monster.lvl = lvl
