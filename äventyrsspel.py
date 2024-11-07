name = input("Vad heter du?-->")

class Player:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.hp = hp
        self.lvl = lvl
    
        print("Player name: " + self.name)
        print("Player hp: " + str(self.hp))
        print("Level: " + str(self.lvl))

player = Player(name, 1, 100)

class inventory:
    def __init__(self):
        self.items = []
        
    def add_item(self,item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name] +=quantity
        else:
            self.items[item_name] = quantity
        print(f"added {quantity} {item_name} to inventory")

        def remove_item(self,item_name,quantity=1):
            if item_name in self.items:
                if self.items[item_name] > quantity:
                    self.items[item_name] -=quantity
                    print(f"{quantity} {item_name} was removed")

        



        








class Creature:
    def __init__(monster,name,hp,lvl):
        monster.name = name
        monster.hp = hp
        monster.lvl = lvl
