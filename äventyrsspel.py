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
        self.showstats()
        
    def showstats(self):
        time.sleep(0.1)
        print()
        time.sleep(0.05)
        print("     Spelar Stats     ")
        time.sleep(0.05)
        print("══════════════════════")
        print(f"Player Name: {self.name}")
        time.sleep(0.05)
        print(f"Level: {self.lvl}")
        time.sleep(0.05)
        print(f"Player HP: {self.hp}")
        time.sleep(0.05)
        print(f"Armor: {self.armor}")
        time.sleep(0.05)
        print(f"Guld: {self.gold}")
        print("══════════════════════")

player = Player(name, 1, 100, 0, 5)

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
    Monster("Skorpion", 5, 2, scorpion_img),
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


def get_custom_monster(name, monsters):
    for monster in monsters:
        if name.lower() == monster.name.lower():
            return monster
    return random.choice(monsters)

current_monster = get_custom_monster(name, monsters)

time.sleep(2)
print(current_monster) 
time.sleep(0.5)
print(f"Du stöter på level {current_monster.lvl} {current_monster.name}.")
time.sleep(0.5)
print(f"{current_monster.name} har {current_monster.hp} HP.")
time.sleep(2)


def monster_attack(player, current_monster):
    while current_monster.hp > 0 and player.hp > 0:
        # Monstrets attack
        damage = random.randint(2, 5) * current_monster.lvl // 2
        print(f"{current_monster.name} attackerar dig och gör {damage} skada!")
        time.sleep(1)
        player.hp = max(0, player.hp - damage)

        if player.hp > 0:
            print(f"Du överlever med {player.hp} HP kvar.")
        else:
            print("""
                                                                                                                                                                                                    [0m
                                                                                                                                                                                    [0m
                                                                                                                      [38;2;255;162;162m*[38;2;255;27;27m0[38;2;255;9;9m0[38;2;255;1;1m0[38;2;255;0;0m0[38;2;255;6;6m0[38;2;255;18;18m0[38;2;255;93;93mo                          [38;2;255;158;158m*[38;2;255;67;67mO[38;2;255;57;57mO[38;2;255;30;30m0[38;2;255;57;57mO[38;2;255;85;85mo[38;2;255;148;148m*                     [0m
   [38;2;255;103;103mo[38;2;255;9;9m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;56;56mO           [38;2;255;162;162m*[38;2;255;75;75mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;35;35mO              [38;2;255;71;71mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0              [38;2;255;131;131m+[38;2;255;9;9m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;32;32m0                  [38;2;255;75;75mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;32;32m0[38;2;255;118;118m+  [38;2;255;151;151m*[38;2;255;40;40mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;52;52mO                [38;2;255;43;43mO[38;2;255;1;1m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;34;34mO      [38;2;255;140;140m+[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0              [0m
     [38;2;255;30;30m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO         [38;2;255;133;133m+[38;2;255;10;10m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;17;17m0           [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;36;36mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;52;52mO          [38;2;255;10;10m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;16;16m0             [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;14;14m0            [38;2;255;10;10m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;10;10m0            [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;4;4m0              [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [0m
     [38;2;255;34;34mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO             [38;2;255;1;1m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0         [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;40;40mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;52;52mO             [38;2;255;4;4m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0         [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                [38;2;255;2;2m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0         [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;9;9m0                 [38;2;255;21;21m0[38;2;255;0;0m0[38;2;255;71;71mo    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;14;14m0      [0m
     [38;2;255;34;34mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO               [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0       [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;40;40mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;52;52mO               [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;19;19m0                  [38;2;255;53;53mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;109;109m+      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;156;156m*                   [38;2;255;0;0m0     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;68;68mO      [0m
     [38;2;255;34;34mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;40;40mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;52;52mO                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                    [38;2;255;108;108m+[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;86;86mo                          [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;144;144m*      [0m
     [38;2;255;34;34mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                 [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;64;64mO     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;40;40mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;52;52mO                 [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0  [38;2;255;103;103mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;115;115m+                     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0   [38;2;255;5;5m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                           [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0       [0m
     [38;2;255;34;34mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                 [38;2;255;20;20m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;40;40mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;52;52mO                 [38;2;255;125;125m+[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                      [38;2;255;123;123m+[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                           [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0       [0m
     [38;2;255;34;34mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;40;40mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;52;52mO                  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                       [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;31;31m0  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                           [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0       [0m
     [38;2;255;34;34mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;29;29m0     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;40;40mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;52;52mO                  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;157;157m*                      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0    [38;2;255;89;89mo[38;2;255;0;0m0[38;2;255;0;0m0       [0m
     [38;2;255;34;34mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                 [38;2;255;117;117m+[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;115;115m+     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;40;40mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;52;52mO                  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;27;27m0                     [38;2;255;156;156m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;154;154m*  [38;2;255;135;135m+[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;4;4m0                  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0     [38;2;255;0;0m0[38;2;255;0;0m0       [0m
     [38;2;255;34;34mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                 [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;40;40mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;52;52mO                 [38;2;255;34;34mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                     [38;2;255;16;16m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;83;83mo                 [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0     [38;2;255;0;0m0[38;2;255;6;6m0       [0m
     [38;2;255;34;34mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                [38;2;255;51;51mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0       [38;2;255;30;30m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;40;40mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;52;52mO                 [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;106;106m+     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;148;148m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;16;16m0                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [38;2;255;121;121m+       [0m
     [38;2;255;34;34mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO               [38;2;255;24;24m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0         [38;2;255;3;3m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;9;9m0              [38;2;255;11;11m0[38;2;255;0;0m0[38;2;255;0;0m0                  [38;2;255;40;40mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;52;52mO               [38;2;255;25;25m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0        [38;2;255;18;18m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;79;79mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0        [38;2;255;4;4m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;152;152m*              [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0     [38;2;255;5;5m0[38;2;255;18;18m0       [0m
     [38;2;255;34;34mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;28;28m0             [38;2;255;18;18m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;83;83mo           [38;2;255;72;72mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0            [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;40;40mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;25;25m0             [38;2;255;58;58mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;38;38mO           [38;2;255;7;7m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;8;8m0              [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0            [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;99;99mo            [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [0m
     [38;2;255;2;2m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;92;92mo      [38;2;255;117;117m+[38;2;255;10;10m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;28;28m0                [38;2;255;112;112m+[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;7;7m0[38;2;255;141;141m*    [38;2;255;112;112m+[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                     [38;2;255;3;3m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;72;72mo      [38;2;255;133;133m+[38;2;255;26;26m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;12;12m0                [38;2;255;55;55mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;14;14m0       [38;2;255;160;160m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;96;96mo                [38;2;255;12;12m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;49;49mO[38;2;255;95;95mo[38;2;255;134;134m+[38;2;255;120;120m+[38;2;255;82;82mo[38;2;255;9;9m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;42;42mO     [38;2;255;151;151m*[38;2;255;141;141m*       [0m
   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;47;47mO                        [38;2;255;99;99mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;147;147m*                     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;21;21m0[38;2;255;162;162m*                       [38;2;255;144;144m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;90;90mo                        [38;2;255;13;13m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;19;19m0                  [0m
                                                                                                                                                                                    [0m
                                                                                                                                                                                    [0m

                  """)
            exit()

        # Spelarens attack (valfri)
        svar = input("Vill du attackera? Svara Ja/Nej: ").strip().lower()
        if svar == "ja":
            damage = random.randint(3, 4) * player.lvl * 2
            print(f"Du attackerar {current_monster.name} och gör {damage} skada!")
            time.sleep(1)
            current_monster.hp = max(0, current_monster.hp - damage)
            
            if current_monster.hp > 0:
                print(f"{current_monster.name} överlever med {current_monster.hp} HP kvar.")
            else:
                print(f"Du dödade {current_monster.name}, som droppar {current_monster.lvl} guld.")
                print(f"Du överlever med {player.hp} HP")
                player.gold += current_monster.lvl
                print(f"Du har nu {player.gold} guld.")
                break
        elif svar == "nej":
            print(f"Du står över din tur. {current_monster.name} attackerar igen.")
        else:
            print("Ogiltigt svar, monstret attackerar.")


monster_attack(player, current_monster)
