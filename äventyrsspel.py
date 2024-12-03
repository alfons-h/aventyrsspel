import time
import random

name = input("Vad heter du?--> ")


class Player:
    def __init__(self, name, lvl, hp, armor, gold):
        self.name = name.capitalize()
        self.hp = hp
        self.lvl = lvl
        self.armor = armor
        self.gold = gold
        
        print("""
              
              """)
        print("Välkommen " + self.name + " till grottkravlare.")
        time.sleep(0.1)
        print()
        time.sleep(0.05)
        print("     Spelar Stats     ")
        time.sleep(0.05)
        print("══════════════════════")
        print(f"Player Name: {self.name}")
        time.sleep(0.05)
        print(f"Player HP: {self.hp}")
        time.sleep(0.05)
        print(f"Level: {self.lvl}")
        time.sleep(0.05)
        print(f"Armor: {self.armor}")
        time.sleep(0.05)
        print(f"Guld: {self.gold}")
        print("══════════════════════")

player = Player(name, 1, 100, 20, 0)

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


rat_img = r"""                       ,     .
                       (\,;,/)
                        (o o)\//,
                         \ /     \,
                         `+'(  (   \    )
                            //  \   |_./
                          '~' '~----'    """
scorpion_img = r""" 
        ___ __
     _{___{__}\
    {_}      `\)
   {_}        `            _.-''''--.._
   {_}                    //'.--.  \___`.
    { }__,_.--~~~-~~~-~~-::.---. `-.\  `.)
     `-.{_{_{_{_{_{_{_{_//  -- 8;=- `
        `-:,_.:,_:,_:,.`\\._ ..'=- ,
            // // // //`-.`\`   .-'/
           << << << <<    \ `--'  /----)
            ^  ^  ^  ^     `-.....--'''"""
slime_img = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠻⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡀⠈⠛⢿⣿⣿⣁⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡟⢡⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⣀⣉⣤⣤⣤⡀⣤⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠻⣿⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⣽⣿⣷⣄⠀⠀⠀⠀
⠀⠀⣾⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣷⣄⠀⠀
⠀⢀⣼⡀⠀⠀⠈⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⠃⠀
⠀⠘⠟⠁⠀⠀⠀⠀⢿⣿⣿⡿⠟⠋⠉⠉⠉⠙⢿⣿⣿⣿⡟⠁⠀⠀⢠⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢿⣿⣿⡦⠀⠙⠻⠟⠁⠀⠀⠀⠈⠛⠃⠀"""
goblin_img = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠢⣤⣀⡀⠀⠀⠀⢿⣧⣄⡉⠻⢿⣿⣿⡿⠟⢉⣠⣼⡿⠀⠀⠀⠀⣀⣤⠔⠀
⠀⠀⠈⢻⣿⣶⠀⣷⠀⠉⠛⠿⠶⡴⢿⡿⢦⠶⠿⠛⠉⠀⣾⠀⣶⣿⡟⠁⠀⠀
⠀⠀⠀⠀⠻⣿⡆⠘⡇⠘⠷⠠⠦⠀⣾⣷⠀⠴⠄⠾⠃⢸⠃⢰⣿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠋⢠⣾⣥⣴⣶⣶⣆⠘⣿⣿⠃⣰⣶⣶⣦⣬⣷⡄⠙⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢋⠛⠻⠿⣿⠟⢹⣆⠸⠇⣰⡏⠻⣿⠿⠟⠛⡙⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢧⡀⠠⠄⠀⠈⠛⠀⠀⠛⠁⠀⠠⠄⢀⡼⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢻⣦⡀⠃⠀⣿⡆⢰⣿⠀⠘⢀⣴⡟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⡀⠘⠇⠸⠃⢀⣴⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣷⣄⣠⣾⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
zombie_img = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠊⠉⠉⠉⠉⢉⠝⠉⠓⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡴⣋⠀⠀⣤⣒⡠⢀⠀⠐⠂⠀⠤⠤⠈⠓⢦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⢋⢬⠀⡄⣀⠤⠄⠀⠓⢧⠐⠥⢃⣴⠤⣤⠀⢀⡙⣆⠀⠀⠀⠀
⠀⠀⠀⠀⢠⡣⢨⠁⡘⠉⠀⢀⣤⡀⠀⢸⠀⢀⡏⠑⠢⣈⠦⠃⠦⡘⡆⠀⠀⠀
⠀⠀⠀⠀⢸⡠⠊⠀⣇⠀⠀⢿⣿⠇⠀⡼⠀⢸⡀⠠⣶⡎⠳⣸⡠⠃⡇⠀⠀⠀
⢀⠔⠒⠢⢜⡆⡆⠀⢿⢦⣤⠖⠒⢂⣽⢁⢀⠸⣿⣦⡀⢀⡼⠁⠀⠀⡇⠒⠑⡆
⡇⠀⠐⠰⢦⠱⡤⠀⠈⠑⠪⢭⠩⠕⢁⣾⢸⣧⠙⡯⣿⠏⠠⡌⠁⡼⢣⠁⡜⠁
⠈⠉⠻⡜⠚⢀⡏⠢⢆⠀⠀⢠⡆⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⣼⠾⢬⣹⡾⠀⠀
⠀⠀⠀⠉⠀⠉⠀⠀⠈⣇⠀⠀⠀⣴⡟⢣⣀⡔⡭⣳⡈⠃⣼⠀⠀⠀⣼⣧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⣸⣿⣿⣿⡿⣷⣿⣿⣷⠀⡇⠀⠀⠀⠙⠊⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣠⠀⢻⠛⠭⢏⣑⣛⣙⣛⠏⠀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠠⠜⠓⠉⠉⠀⠐⢒⡒⡍⠐⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠢⠤⣀⣀⣀⣀⣘⠧⠤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
ghost_img = r"""
            .--,
           /  (
          /    \
         /      \ 
        /  0  0  \
((()   |    ()    |   ()))
\  ()  (  .____.  )  ()  /
 |` \_/ \  `""`  / \_/ `|
 |       `.'--'.`       |
  \        `""`        /
   \                  /
    `.              .'    ,
     |`             |  _.'|
     |              `-'  /
     \                 .'
      `.____________.-'"""
vampire_img = r"""                  -.                       .-
              _..-'(                       )`-.._
           ./'. '||\\.      _ _ /|       .//||` .`\.
        ./'.|'.'||||\\|..   \'o.O' /  ..|//||||`.`|.`\.
     ./'..|'.|| |||||\``````=(___)=''''''/||||| ||.`|..`\.
   ./'.||'.|||| ||||||||||||.  U  .|||||||||||| ||||.`||.`\.
  /'|||'.|||||| |||||||||||||     ||||||||||||| ||||||.`|||`\
 '.|||'.||||||| |||||||||||||     ||||||||||||| |||||||.`|||.`
'.||| ||||||||| |/'   ``\||``     ''||/''   `\| ||||||||| |||.`
|/' \./'     `\./         \!|\   /|!/         \./'     `\./ `\|
V    V         V          }' `\ /' `{          V         V    V
`    `         `               V               '         '    '"""
werewolf_img = r"""
                      .-+--:%%=:-.       
                -#%%*%@@@@@%%@@@@@#.     
          -%@@@@@@@@@@@@@@@@@@@@@@@@@@*  
      .+@%@@@%#-:%@@@@@@@@@@@@@@@@%++=.  
    .=@@@-        .%@@@@@@@@@@%%%@%:.    
    #@%*%%.       *@@@@@@@@@#+    +#     
  .%*+..#-. .:.   +@@@@@@@@@%-           
    . ......%@@@-*@@@@@@#: .=#%+.        
  :%*%+%#@@@@%.%@@@@@@@@=      .@*       
  .#%%@@@@%..*@@@@@@@@@@@%.    +#%+.     
    =#%=@+.*@@@@@@@@@@@@@@*    ..+%*     
     ..   :#@@@%-:=+=:=@@%.      ...     
    .#@@@@@@@%:     :%@%:                
    #@+ .#@@#.      .#@:                 
  .#@@-              %@%:..              
  .%%*#.             .#%%+=              
    ..                 ..   """
dragon_img = r"""
                                                            @      @                                
                                               @@            @@@@@@       @@                           
                                            @@@@@           @@@@@@@    @@@@@@@@@                      
                                          @@@@@            @@@@@@@@@    @   @@@@@@@                   
                                    @@@@@@@@@@@          @@@@@@@ @@@        @ @@@@@@@                 
                                @@@@@@@@@@@@@@@           @@@@@@ @@@        @@@ @@@@@@                
                            @@@@@@@@  @@@@@@@@@           @@@@@  @@@         @@@@@@@@@@@              
                         @@@@@@@@@ @@@@@@@@@@@@            @@   @@@@         @@@@@@@@@@@@@            
                      @@@@@@@@@@ @@@@@@@@@@@@@@            @@   @@@           @@@ @@@@@@@@@           
                    @@@@@@@@@@ @@@@@@@@@@@@@@@                @@@@@          @@@@@@@@@@@@@@@@         
                  @@@@@@@@@@@ @@@@@@@@@@@@@@@@               @@@@@           @@@@@@@@@@@@@@@@@        
               @@@@@@@@ @ @ @@@@@@@@@@@@@@@@@@@            @@@@@@           @@@@@@@@@@@@@@@@@@@       
             @@@@ @@@@ @@@ @@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@@@@      
            @@@ @@@@@ @@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@     
          @@@ @@ @@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@ @@@@@@   @@@@ @@@@@@@@@@@@@    
         @@ @@@@@@@ @@@@@@@@@ @@@@@@@@   @@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@   @@@@@@@@@@@@@@   
       @@@ @@@ @@@ @@@@@@@@@   @@@@@      @@    @@  @@@@@@@@@@@@@@@@ @@@@@@@@@ @@   @@@@@@@@@@@@@@@   
      @@  @@@@@@@ @@    @@@     @@@        @     @   @@@@ @@@@@@@@@@   @@@@@@@@@    @@@@@@@@@@@@@ @@  
     @@  @@@@ @@@      @@@      @@                     @     @@@@@@@@@        @@   @@@@@@@@@@@@@@  @  
    @    @@@@@@@       @@       @                              @@@@@@@@@          @@@@@@@@@@  @@@   @ 
   @    @@@@ @@@      @@                                       @@@@@@@@@@        @@@@@@@@@@@  @@@     
  @    @@@   @@       @                                        @@@@@@@@@ @      @@@@@  @@@@    @@     
       @@    @@       @                                        @@@@@@@@@@@@@@@@@@@@@@@@@@@     @@     
      @@      @                                                 @@@ @ @@@@@ @@@@@@    @@@@     @@     
      @       @                                                 @@@      @@@@@@@     @@  @@    @      
     @@       @                                                  @@@@     @@@@       @   @@    @      
     @                                                             @   @@@@@        @   @@            
                                                                  @@@@@@@@             @@             
                                                                 @@@@@@              @@@              
                                                              @@@@ @                 @@               
                                                                @@@                 @@         @@     
                                                                                    @@        @@      
                                                                                      @@@@@@@         
"""

monsters = [
    Monster("Råtta", 3, 1, rat_img),
    Monster("Scorpion", 5, 2, scorpion_img),
    Monster("Slime", 10, 3, slime_img),
    Monster("Goblin", 25, 7, goblin_img),
    Monster("Zombie", 50, 10, zombie_img),
    Monster("Spöke", 75, 12, ghost_img),
    Monster("Vampyr", 100, 15, vampire_img),
    Monster("Varulv", 150, 20, werewolf_img),
    Monster("Drake", 500, 100, dragon_img)
]

def choose_door():
    print("Du står framför tre dörrar. Vilken vill du öppna?")
    time.sleep(1)
    print("1. Dörr 1")
    print("2. Dörr 2")
    print("3. Dörr 3")
    
    while True:
        choice = input("Skriv numret på dörren du vill öppna (1, 2 eller 3): ").strip()
        if choice in ["1", "2", "3"]:
            print(f"Du öppnar dörr {choice}...")
            time.sleep(2)
            return
        else:
            print("Ogiltigt val, försök igen.")


choose_door()

current_monster = random.choice(monsters)

time.sleep(2)
print(current_monster) 
time.sleep(0.5)
print(f"Du stöter på level {current_monster.lvl} {current_monster.name}.")
time.sleep(0.5)
print(f"{current_monster.name} har {current_monster.hp} HP.")
time.sleep(2)


def monster_attack(current_monster, player):
    damage = random.randint(2, 5) * current_monster.lvl // 2
    print(f"{current_monster.name} attackerar dig och gör {damage} skada!")
    time.sleep(1)
    player.hp = max(0, player.hp - damage)
    if player.hp > 0:
        print(f"Du överlever med {player.hp} HP kvar.")
    else:
        print(f"Du dog!")
        exit()

def player_attack(player, current_monster):
    damage = random.randint(3, 4) * player.lvl * 2
    print(f"Du attackerar {current_monster.name} och gör {damage} skada!")
    time.sleep(1)
    current_monster.hp = max(0, current_monster.hp - damage)
    if current_monster.hp > 0:
        print(f"{current_monster.name} överlever med {current_monster.hp} HP kvar.")
    else:
        print(f"Du dödade {current_monster.name}, som droppar {current_monster.lvl} guld.")
        player.gold += current_monster.lvl
        print(f"Du har nu {player.gold} guld.")

def continue_fight(player, current_monster):
    while current_monster.hp > 0 and player.hp > 0:
        monster_attack(current_monster, player)

        if player.hp > 0:
            svar1 = input("Vill du attackera? Svara Ja/Nej: ").strip().lower()

            if svar1 == "ja":
                player_attack(player, current_monster)
            elif svar1 == "nej":
                print(f"Du står över din tur. {current_monster.name} attackerar igen.")
            else:
                print("Ogiltigt svar, försök igen.")
                continue

            if current_monster.hp > 0:
                monster_attack(current_monster, player)
        else:
            print("Du dog!")
            exit()

    if current_monster.hp <= 0:
        print(f"Du har dödat {current_monster.name}.")
        choose_door()

continue_fight(player, current_monster)
