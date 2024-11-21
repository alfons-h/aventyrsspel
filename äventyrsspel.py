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
        print(f"Player Name: {self.name}")
        print(f"Player HP: {self.hp}")
        print(f"Level: {self.lvl}")
        print(f"Armor: {self.armor}")
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
                print(f"För få {item_name} för att ta bort. Bara {self.items[item_name]} är tillgängliga.")
        else:
            print(f"{item_name} hittades inte")


class Monster:
    def __init__(self, name, hp, lvl, bild):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.bild = bild

    def __str__(self):
        return f"{self.name}: HP {self.hp}, Level {self.lvl}\n{self.bild}"


rat_img = """lägg in bild"""
slime_img = """lägg in bild"""
goblin_img = """lägg in bild"""
zombie_img = """lägg in bild"""
ghost_img = """lägg in bild"""
vampire_img = """                                  _.-.
                                 ._.-.\
                    .^         _.-'=. \\
                  .'  )    .-._.-=-..' \'.
               .'   .'   _.--._-='.'   |  `.  ^.
             .'   .'    _`.-.`=-./'.-. / .-.\ `. `.
           .'    /      _.-=-=-/ | '._)`(_.'|   \  `.
          /    /|       _.--=.'  `. (.-v-.)/    |\   \
        .'    / \       _.-.' \-.' `-..-..'     / \   `.
       /     /   `-.._ .-.'      `.'  " ". _..-'  |    |
      '      |    |   /   )        \  /   \   \    \    `.
     /      /    /   /   /\                \   \   |      \
    /      /    /  .'  .'\ `.        .'     \   |   \      \
   /      /    /  /   /   \  `-    -' .`.    .  \    \     |
  |      /    / .''\.'    | `.      .'   `.   \  |    |    |
 .'     /    / /   |      |      .'/       `.- `./    /    |
 |     /    .-|   /--.    / `.    |    _.-''\   |     |    \
.'    /  .-'  |  /    `-.|       .'\_.'      `. |`.   |    |
|    |.-'     / /       /           \          \ \ `. \     \
|    /       /  |      /             \         |  `. `.|    |
|   |       /   `.     |      `   .'  \        /    \  \    /
|   |      ///.-'.\    |       \ /    `\      / /-.  \ |    |
|   /      \\\\    `    \.-     |    `-.\     |/   \\\\'.   |
 \ |        \\\|        |      / \      |          //// |  /
 | |         '''        |     /   \     |          |//  |  \
 \ |                    |.-  |     \  .-|          ''   |  /
  \|                    /    |    / ` ../               / /
                        |'   /    |    /               | /
                        \.'  |    | `./                |/
                        /    \   /    \
                        \ `. /   \    /
                         |  |     '. '
                         /  |      |  \
                        /   |      /   `.
                       | | | \   .'  `.. \
                      / / / ._`. \.'-. \`/
             LGB      |/ / /  `'  `  |/|/
                       \|\|"""
werewolf_img = """     _                  _
    | '-.            .-' |
    | -. '..\\,.//,.' .- |
    |   \  \\\||///  /   |
   /|    )M\/%%%%/\/(  . |\
  (/\  MM\/%/\||/%\\/MM  /\)
  (//M   \%\\\%%//%//   M\\)
(// M________ /\ ________M \\)
 (// M\ \(',)|  |(',)/ /M \\) \\\\  
  (\\ M\.  /,\\//,\  ./M //)
    / MMmm( \\||// )mmMM \  \\
     // MMM\\\||///MMM \\ \\
      \//''\)/||\(/''\\/ \\
      mrf\\( \oo/ )\\\/\
           \'-..-'\/\\
              \\/ \\"""
dragon_img = r"""                 ___====-_  _-====___
           _--^^^#####//      \\#####^^^--_
        _-^##########// (    ) \\##########^-_
       -############//  |\^^/|  \\############-
     _/############//   (@::@)   \\############\_
    /#############((     \\//     ))#############\
   -###############\\    (oo)    //###############-
  -#################\\  / VV \  //#################-
 -###################\\/      \//###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv)"""

monsters = [
    Monster("Råtta", 3, 1, rat_img),
    Monster("Slime", 10, 3, slime_img),
    Monster("Goblin", 25, 7, goblin_img),
    Monster("Zombie", 50, 10, zombie_img),
    Monster("Spöke", 75, 12, ghost_img),
    Monster("Vampyr", 100, 15, vampire_img),
    Monster("Varulv", 150, 20, werewolf_img),
    Monster("Drake", 500, 100, dragon_img)
]

current_monster = random.choice(monsters)

print(current_monster)  
print(f"Du stöter på {current_monster.name}.")
print(f"{current_monster.name} har {current_monster.hp} HP.")


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
