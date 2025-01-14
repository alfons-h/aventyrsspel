import time
import random

name = input("Vad heter du?--> ")


class Player:
    def __init__(self, name, lvl, xp, hp, armor, gold):
        self.name = name.capitalize()
        self.hp = hp
        self.lvl = lvl
        self.xp = xp
        self.armor = armor
        self.gold = gold
        
        print("""
              
              """)
        print("Välkommen " + self.name + " till grottkravlare.")
        print("Du vaknar i mörkret, omgiven av kalla stenväggar.")
        time.sleep(1)
        print("Framför dig ser du tre massiva dörrar, var och en med märkliga symboler inristade.")
        time.sleep(2)
        print("Minnet är blankt, men något säger dig att valet du gör här kommer forma ditt öde.")
        time.sleep(2)
        self.showstats()
        
    def showstats(self):
        time.sleep(0.1)
        print()
        time.sleep(0.05)
        print("     Spelar Stats     ")
        time.sleep(0.05)
        print("══════════════════════")
        print(f"Spelarnamn: {self.name}")
        time.sleep(0.05)
        print(f"\033[38;5;213mLevel:\033[0m {self.lvl}")
        time.sleep(0.05)
        print(f"\033[38;5;34mXP:\033[0m {self.xp}")
        time.sleep(0.05)
        print(f"\033[38;5;196mHP:\033[0m {self.hp}")
        time.sleep(0.05)
        print(f"\033[38;5;153mArmor:\033[0m {self.armor}")
        time.sleep(0.05)
        print(f"\033[38;5;226mGuld:\033[0m {self.gold}")
        print("══════════════════════")

    def gain_xp(player, amount):
        player.xp += amount
        print(f"\033[38;5;34mDu har fått {amount} XP!\033[0m")
        player.check_level_up()

    def check_level_up(self):
        xp_needed = 100 + 0.8 * (self.lvl ** 2)
        while self.xp >= xp_needed:
            self.xp -= xp_needed
            self.lvl += 1
            xp_needed = 100 + 0.8 * (self.lvl ** 2)
            print(f"\033[38;5;213mGrattis {self.name}, du har nått Level {self.lvl}!\033[0m")
        self.showstats()
        
        
player = Player(name, 1, 0, 100, 0, 5)

def player_command():
    while True:
        command = input(
"""
Vad vill du göra? 
1. Gå vidare (fortsätt)
2. Visa stats (stats)
3. Något annat som vi inte lagt till (placeholder)
""").strip().lower()
        if command == "stats":
            player.showstats()
        elif command == "fortsätt":
            choose_door()
        elif command == "2":
            player.showstats()
        elif command == "1":
            choose_door()        
        elif command == "placeholder":
            print("Vi har inte fixat det här ännu")
            choose_door()
        elif command == "3":
            print("Vi har inte fixat det här ännu")
            choose_door()
        else:
            print("Ogiltigt kommando. Försök igen.")

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
    def __init__(self, name, hp, lvl, img,):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.img = img
        self.escape_threshold = 6

    def __str__(self):
        return f"{self.name}: HP {self.hp}, Level {self.lvl}\n{self.img}"


rat_img = r"""
                       ,     .
                       (\,;,/)
                        (o o)\//,
                         \ /     \,
                         `+'(  (   \    )
                            //  \   |_./
                          '~' '~----'    
"""
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
            ^  ^  ^  ^     `-.....--'''
"""
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢿⣿⣿⡦⠀⠙⠻⠟⠁⠀⠀⠀⠈⠛⠃⠀
"""
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠢⠤⣀⣀⣀⣀⣘⠧⠤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
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
      `.____________.-'
"""
vampire_img = r"""
                  -.                       .-
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
`    `         `               V               '         '    '
"""
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
    ..                 ..   
"""
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


class Sword:
    def init(self, name, damage):
        self.name = name
        self.dmg = damage

    def str(self):
        return f"{self.name}: damage{self.dmg}"
    

class Armor:
    def init(self, name, armor):
        self.name = name
        self.arm = armor

    def str(self):
        return f"{self.name}: armor{self.arm}"

class Sword:
    def __init__(self, name, damage):
        self.name = name
        self.dmg = damage

    def __str__(self):
        return f"{self.name}: Damage {self.dmg}"


class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def __str__(self):
        return f"{self.name}: Defense {self.defense}"


class Helmet(Armor):
    def __init__(self, name, defense):
        super().__init__(name, defense)


class ChestArmor(Armor):
    def __init__(self, name, defense):
        super().__init__(name, defense)


class LegArmor(Armor):
    def __init__(self, name, defense):
        super().__init__(name, defense)



swords = [
    Sword("Träsvärd", 1),
    Sword("Stensvärd", 2),
    Sword("Rostigt Järnsvärd", 4), 
    Sword("Järnsvärd", 7),
    Sword("Finslipat Järnsvärd", 12),
    Sword("Silversvärd", 15),
    Sword("Helvetets Skrik", 35),
    Sword("Blodherrens Rappir", 60),
]


helmets = [
    Helmet("Järnhjälm", 5),
    Helmet("Silverhjälm", 10),
    Helmet("Gyllene Hjälm", 15),
    Helmet("Stormhjälm", 20),
    Helmet("Demonhjälm", 30),
]


chest_armors = [
    ChestArmor("Järnbröstplåt", 10),
    ChestArmor("Silverbröstplåt", 15),
    ChestArmor("Gyllene Bröstplåt", 20),
    ChestArmor("Stormbröstplåt", 30),
    ChestArmor("Demonbröstplåt", 40),
]


leg_armors = [
    LegArmor("Järnbenskydd", 8),
    LegArmor("Silverbenskydd", 12),
    LegArmor("Gyllene Benskydd", 18),
    LegArmor("Stormbenskydd", 25),
    LegArmor("Demonbenskydd", 35),
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
            return Monster(monster.name, monster.hp, monster.lvl, monster.img)
    chosen_monster = random.choice(monsters)
    return Monster(chosen_monster.name, chosen_monster.hp, chosen_monster.lvl, chosen_monster.img)


choose_door()
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
            time.sleep(0.2)
        else:
            print("""
---------------------
        DU DOG
---------------------
                  """)
            exit()

         # Spelarens attack eller flykt
        svar = input("""Vad vill du göra?
1. Attackera
2. Fly
""").strip().lower()
        if svar == "1" or svar == "attackera" or svar == "attack":
            damage = random.randint(3, 4) * player.lvl * 2
            print(f"Du attackerar {current_monster.name} och gör {damage} skada!")
            time.sleep(1)
            current_monster.hp = max(0, current_monster.hp - damage)
            
            if current_monster.hp > 0:
                print(f"{current_monster.name} överlever med {current_monster.hp} HP kvar.")
                time.sleep(0.3)
            else:
                #Räknar ut loot
                gold_loot = int(current_monster.lvl // 2) ** 2 + 1
                xp_loot = int((current_monster.lvl) ** 1.5) + 3
                print(f"💀 Du dödade {current_monster.name}, som droppar \033[38;5;226m{int(current_monster.lvl/2)**2+1} guld\033[0m.")
                print(f"Du överlever med {player.hp} HP")
                #Lägger till loot till spelaren
                player.gold += gold_loot
                player.gain_xp(xp_loot)
                break
        elif svar == "2" or svar == "fly":
            # Försök att fly
            dice_roll = random.randint(1, 18) - ((current_monster.lvl) // 2) + player.lvl
            print(f"Du försöker fly från {current_monster.name}...")
            time.sleep(0.5)
            if dice_roll > current_monster.escape_threshold:
                print(f"Du lyckades fly från {current_monster.name}!")
                break
            else:
                print(f"Du misslyckades att fly från {current_monster.name}.")
                time.sleep(0.4)
        else:
            print("Ogiltigt svar, monstret attackerar.")

monster_attack(player, current_monster)

while True:  # Evig spel-loop
    choose_door()
    current_monster = get_custom_monster(name, monsters)
    print(f"Du stöter på level {current_monster.lvl} {current_monster.name}.")
    time.sleep(0.5)
    print(f"{current_monster.name} har {current_monster.hp} HP.")
    time.sleep(2)

    monster_attack(player, current_monster)  # Spelaren slåss eller flyr från det nya monstret

    if player.hp <= 0:
        print("""
---------------------
        DU DOG
---------------------
""")
        exit()
