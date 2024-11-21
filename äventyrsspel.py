import random
name = input("Vad heter du?--> ")


class Player:
    def __init__(self, name, lvl, hp, armor):
        self.name = name.capitalize()
        self.hp = hp
        self.lvl = lvl
        self.armor = armor
        print("Välkommen " + self.name + " till grottkravlare.")
        print()
        print("     Spelar Stats     ")
        print("══════════════════════")
        print("Player Name: " + (self.name))
        print("Player HP: " + str(self.hp))
        print("Level: " + str(self.lvl))
        print("Armor:" + str(self.armor))
        print("══════════════════════")


player = Player(name, 1, 100, 20)


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
    def __init__(self, name, hp, lvl, bild):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.bild = bild

    def __str__(self):
        return f"{self.name}: HP {self.hp}, Level {self.lvl}, {self.bild}"

monsters = [
    Monster("Råtta", 3, 1, "LÄGG IN BILD HÄR"),
    Monster("Slime", 10, 3, "LÄGG IN BILD HÄR"),
    Monster("Goblin", 25, 7, "LÄGG IN BILD HÄR"),
    Monster("Zombie", 50, 10, "LÄGG IN BILD HÄR"),
    Monster("Spöke", 75, 12, "LÄGG IN BILD HÄR"),
    Monster("Vampyr", 100, 15, "LÄGG IN BILD HÄR"),
    Monster("Varulv", 150, 20, "LÄGG IN BILD HÄR"),
    Monster("Drake", 500, 100, "LÄGG IN BILD HÄR")
]

current_monster = random.choice(monsters) # Får fixa den här senare när vi har fixat rum och dörrar o sånt

print(current_monster.bild)
print(f"Du stöter på {current_monster.name}.")
print(f"{current_monster.name} har {current_monster.hp} HP")

def monster_attack(current_monster, player):
    damage = random.randint(3, 10) * current_monster.lvl
    print(f"{current_monster.name} attackerar dig och gör {damage} skada!")
    player.hp = max(0, player.hp - damage)
    if player.hp > 0:
        print(f"Du har nu {player.hp} HP kvar.")
    else:
        print(f"Du dog!")
        exit()


monster_attack(current_monster, player)