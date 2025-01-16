import time
import random

name = input("Vad heter du?--> ")


class Player:
    def __init__(self, name, lvl, xp, hp, armor, gold):
        self.name = name.capitalize()       #namnet får automatiskt stor bokstav
        self.hp = hp
        self.lvl = lvl
        self.xp = xp
        self.armor = armor
        self.gold = gold
                
        
        print("""
              
              """)
        print("Välkommen " + self.name + " till grottkravlare.")
        print("Du vaknar i mörkret, omgiven av kalla stenväggar.")
        time.sleep(0.5)
        print("Framför dig ser du tre massiva dörrar, var och en med märkliga symboler inristade.")
        time.sleep(1)
        print("Minnet är blankt, men något säger dig att valet du gör här kommer forma ditt öde.")
        time.sleep(1)
        self.showstats()                    #
        
    def showstats(self):        #Funktion för att visa stats
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
        player.xp += amount             #Lägger till XP till spelaren
        print(f"\033[38;5;34mDu har fått {amount} XP!\033[0m")
        player.check_level_up()         #Kollar om man ska levla upp

    def check_level_up(self):           #Kollar om man ska levla upp
        xp_needed = 100 + 0.8 * (self.lvl ** 2)     #Det krävs 100 XP + 0.8(level)^2 där
        while self.xp >= xp_needed:                 #Loop som kollar om man har nog med XP för att levla upp
            self.xp -= xp_needed                        #Om man levlar upp så tar den bort allt xp man behöver för den nya leveln
            self.xp = round(self.xp)                    #Nya XPn rundas till heltals
            self.lvl += 1                               #Man går upp en level
            xp_needed = 100 + 0.8 * (self.lvl ** 2)
            print(f"\033[38;5;213mGrattis {self.name}, du har nått Level {self.lvl}!\033[0m")
        self.showstats()
        
    def update_armor(self, equipped_armor):             #Funktion för att lägga till armor stats när man tar på sig armor
        total_defense = 0                               #Man börjar med 0 Defense
        for slot, item in equipped_armor.items():       #Loop som kollar efter rustningsdelar
            if item is not None:                        
                total_defense += item.defense           #Lägger till armor stats
        self.armor = total_defense

        
        
player = Player(name, 1, 0, 100, 0, 5)                  #Spelares namn, lvl, xp, hp, armor, guld

def player_command():                                   #Menyn som öppnas när man dödat ett monster eller flytt där man väljer vad man vill göra
    while True:
        command = input(
"""
Vad vill du göra? 
1. Gå vidare (fortsätt)
2. Visa stats (stats)
3. Visa inventory (inventory)
4. Hantera föremål i inventoriet (föremål)
5. Visa equippade föremål 
""").strip().lower()
        if command in ["fortsätt", "1"]:                #Första valet, gå vidare genom att öppna en ny dörr
            choose_door()
            break                                       # Tillbaks till spel-loopen
        elif command in ["stats", "2"]:                 #Andra valet, visa spelarens stats
            player.showstats()
        elif command in ["inventory", "3"]:             #Tredje valet, visa inventoryt
            player_inventory.show_inventory()
        elif command in ["hantera", "4"]:               #Fjärde valet, ta på sig rustning och svärd
        
            print("\nDitt inventory:")
            items = list(player_inventory.items.keys()) #Skapar en lista av namnen på allt i inventoryt
            index = 1                                   #Gör så att listan börjar på 1
            for item in items:                  #Loop som skriver ut en lista av alla föremål i spelarens inventory
                print(f"{index}. {item}")
                index += 1

            choice = input("\nVälj ett föremål med dess nummer: ").strip()      #Här väljer man vilket föremål man vill använda
            if choice.isdigit():                                                #Ser till så att man skrev en siffra
                choice = int(choice) - 1                                        #Konvertera till nollbaserat index eftersom pythonlistor börjar på 0
                if 0 <= choice < len(items):                                    #Ser till så att numret som spelaren skriver inte är mindre (negativ) eller mer än listan
                    item_name = items[choice]                                   
                    action = input(f"Vill du 1. Equippa eller 2. Slänga {item_name}?").strip().lower()
                    if action in ["1", "equip", "equippa", "e"]:
                        print()
                        print(f"Försöker equippa {item_name}...")
                        item = player_inventory.items[item_name]                #Kopplar föremålet man väljer till inventoryt 
                        player_inventory.equip_item(item_name)                  #Startar equip-funktionen för det föremålet man valt

                    elif action in ["2", "släng", "slänga", "s"]:
                        print(f"Slänger {item_name}...")
                        player_inventory.remove_item(item_name)                 #Man kan också välja att göra sig av med föremålet
                    else:
                        print("Ogiltigt val.")
                else:
                    print("Ogiltigt val.")
            else:
                print("Ange ett giltigt nummer.")
        elif command in ["5"]:                                                  #Femte valet, visa alla rustningsdelar som spelaren har tagit på sig
            print("Equippade föremål:")
            for slot, item in player_inventory.equipped_armor.items():          #Loop som skriver ut alla rustnings-slots och vad som finns i dem
                if item:
                    print(f"{slot.capitalize()}: {item.name}, ({item.defense} försvar)")        #Skriver ut rustningsdel och hur mycket armor stats den har
                else:
                    print(f"{slot.capitalize()}: Ingen")                                        #Om man inte har något i en rustnings-slot så skriver den det.
     
        else:
            print("Ogiltigt kommando. Försök igen.")



class Inventory:
    def __init__(self):
        self.items = {}  #Lagra föremål i ett dictionary
        self.equipped_armor = {     #Lagra armorn som är på kroppen i ett dictionary
            "helmet": None,
            "chest": None,
            "legs": None,
        }
        
    def add_item(self, item, quantity=1):       #Funktion för att lägga till föremål i inventoryt
        if item.name in self.items:                         #Om föremålet redan finns i inventoryt så ökar dess kvantitet med 1 istället för att läggas till igen som ett nytt föremål
            self.items[item.name]['quantity'] += quantity 
        else:
            self.items[item.name] = {'item': item, 'quantity': quantity}        #Dictionary för föremål i inventoryt
        print(f"Lade till {quantity} {item.name} till inventariet.")

    def remove_item(self, item_name, quantity=1):   #Funktion för att ta bort föremål från inventoryt
        if item_name in self.items:         #Kollar om föremålet finns så att man kan ta bort det
            if self.items[item_name]['quantity'] > quantity:        #Kollar så att det finns fler föremål än vad man vill ta borts
                self.items[item_name]['quantity'] -= quantity       #Minskar kvantiteten av föremålet i inventoryt med värdet "quantity"
                print(f"{quantity} {item_name} togs bort.")         
            elif self.items[item_name]['quantity'] == quantity:     #Om antalet föremål i inventoryt i listan är lika stort som man vill ta bort så raderas den istället för att kvantiteten minskas
                del self.items[item_name]                           #Raderar föremålet
                print(f"{quantity} {item_name} togs bort och finns inte längre i inventariet.")
            else:
                print(f"För få {item_name} för att ta bort. Bara {self.items[item_name]['quantity']} är tillgängliga.")     #Om man vill ta bort fler föremål än vad som finns så säger den till
        else:
            print(f"{item_name} hittades inte i inventariet.") #Ifall föremålet inte finns så säger den till

    def show_inventory(self):                                   #Funktion för att visa inventoryt inom player_command
        if not self.items:                                      #Om self.items (inventoryt) inte finns så säger den det
            print("Ditt inventory är tomt.")
        else:
            print("\nDitt inventory innehåller:")               
            for item_name, data in self.items.items():          #Loop som går igenom alla items i self.items. "Data" används för att koppla till kvantiteten
                print(f"- {item_name}: {data['quantity']}x")    #Printar alla items och deras kvantitet

    def equip_item(self, item_name):            #Funktion för att ta på sig armor-delar
        if item_name not in self.items:         #Om ett föremål man försöker equippa inte finns så kan man inte equippa den
            print(f"{item_name} finns inte i ditt inventory.")
            return                              #Avsluta equip_item och återvänd till player_command


        item = self.items[item_name]['item']        #Hämta föremålet

        if hasattr(item, 'defense'):         #Kontrollera om det är rustning genom att kolla om det är ett item och leta efter 'defense'
            slot = None                                     
            if "hjälm" in item.name.lower():                #Om föremålet har "hjälm" i namnet så är det en hjälm och kan sättas på huvudet  
                slot = "helmet"                             
            elif "bröstplåt" in item.name.lower():          #Om föremålet har "bröstplåt" i namnet så är det en bröstplåt och kan sättas på bröstet
                slot = "chest"                              
            elif "benskydd" in item.name.lower():           #Om föremålet har "benskydd" i namnet så är det ett par benskydd och kan sättas på benen
                slot = "legs"

            if not slot:                                                                    #Om föremålet inte hör till en armorslot kan man inte equippa den
                print(f"{item.name} är inte en giltig rustning och kan inte equippas.")
                return

            if self.equipped_armor[slot]:
                print(f"{self.equipped_armor[slot].name} togs av och ersattes med {item.name}.")
            else:
                print(f"{item.name} equippades.")

            self.equipped_armor[slot] = item                    #Armor equippas
            self.remove_item(item_name)                         #Armor tas bort från spelarens inventory eftersom den hamnar i armor slotten
            player.update_armor(self.equipped_armor)            #Efter att man tar på sig rustningen uppdateras spelarens armor-stat
        else:
            print(f"{item_name} är inte ett giltigt föremål för utrustning.")



player_inventory = Inventory()

class Monster:
    def __init__(self, name, hp, lvl, img,):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.img = img                  #Monstrena har bilder utav ASCII-konst
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
    def __init__(self, name, damage):
        self.name = name                    #Svärdets namn
        self.dmg = damage                   #Svärdets skada

    def __str__(self):
        return f"{self.name}: Damage {self.dmg}"


class Armor:                                #Alla individuella armordelar ingår i class Armor
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
    Sword("Excalibur", 100)
]


helmets = [
    Helmet("Järnhjälm", 5),
    Helmet("Silverhjälm", 10),
    Helmet("Gyllene Hjälm", 15),
    Helmet("Stormhjälm", 20),
    Helmet("Drakhjälm", 30),
]


chest_armors = [
    ChestArmor("Järnbröstplåt", 10),
    ChestArmor("Silverbröstplåt", 15),
    ChestArmor("Gyllene Bröstplåt", 20),
    ChestArmor("Stormbröstplåt", 30),
    ChestArmor("Drakbröstplåt", 40),
]


leg_armors = [
    LegArmor("Järnbenskydd", 8),
    LegArmor("Silverbenskydd", 12),
    LegArmor("Gyllene Benskydd", 18),
    LegArmor("Stormbenskydd", 25),
    LegArmor("Drakbenskydd", 35),
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
            
            #Skapa nytt monster
            global current_monster
            current_monster = get_custom_monster(name, monsters)
            print(current_monster)
            print(f"Du stöter på level {current_monster.lvl} {current_monster.name}.")
            print(f"{current_monster.name} har {current_monster.hp} HP.")
            time.sleep(1)

            #Tillbaks till spel-loopen
            break
        else:
            print("Ogiltigt val, försök igen.")

def get_custom_monster(name, monsters): 
    for monster in monsters:
        if name.lower() == monster.name.lower(): #Debug-tillägg så att vi kan välja vilket monster som ska spawnas
            return Monster(monster.name, monster.hp, monster.lvl, monster.img)
    chosen_monster = random.choice(monsters)
    return Monster(chosen_monster.name, chosen_monster.hp, chosen_monster.lvl, chosen_monster.img)


choose_door()


death_screen = """                                                                                                                                                                                                        [0m
                                                                                                                                                                                                        [0m
                                                                                                                                                                                                        [0m
   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;26;26m0[38;2;255;103;103mo[38;2;255;114;114m+[38;2;255;114;114m+[38;2;255;114;114m+[38;2;255;114;114m+[38;2;255;96;96mo[38;2;255;48;48mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;87;87mo              [38;2;255;33;33m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;139;139m+           [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;162;162m*             [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;25;25m0[38;2;255;102;102mo[38;2;255;114;114m+[38;2;255;114;114m+[38;2;255;114;114m+[38;2;255;114;114m+[38;2;255;97;97mo[38;2;255;49;49mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;55;55mO                         [38;2;255;70;70mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;112;112m+                      [38;2;255;9;9m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;18;18m0                [0m
     [38;2;255;134;134m+[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;107;107m+    [38;2;255;133;133m+[38;2;255;22;22m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;38;38mO             [38;2;255;154;154m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;57;57mO                 [38;2;255;68;68mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;107;107m+    [38;2;255;133;133m+[38;2;255;22;22m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;17;17m0                  [38;2;255;2;2m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;18;18m0         [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;1;1m0                [38;2;255;49;49mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;103;103mo           [38;2;255;29;29m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0        [38;2;255;4;4m0       [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO            [38;2;255;107;107m+[38;2;255;1;1m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;19;19m0           [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;122;122m+                 [38;2;255;142;142m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0            [38;2;255;109;109m+[38;2;255;1;1m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;18;18m0            [38;2;255;37;37mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;43;43mO               [38;2;255;11;11m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0            [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;121;121m+                 [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0     [38;2;255;127;127m+[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0       [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO               [38;2;255;3;3m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;42;42mO         [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;122;122m+                 [38;2;255;142;142m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0               [38;2;255;11;11m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;12;12m0         [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;143;143m*        [38;2;255;96;96mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;63;63mO                    [38;2;255;0;0m0[38;2;255;0;0m0     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0       [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                 [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0        [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;122;122m+                 [38;2;255;142;142m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;100;100mo     [38;2;255;84;84mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                     [38;2;255;10;10m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;60;60mO      [38;2;255;17;17m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                      [38;2;255;8;8m0[38;2;255;150;150m*     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0       [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;160;160m*      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;122;122m+                 [38;2;255;142;142m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;155;155m*    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                       [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0     [38;2;255;54;54mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;131;131m+                             [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;38;38mO       [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;122;122m+                 [38;2;255;142;142m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0   [38;2;255;76;76mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                        [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;7;7m0                              [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;142;142m*       [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                   [38;2;255;57;57mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;151;151m*     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;122;122m+                 [38;2;255;142;142m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;60;60mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;146;146m*  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;152;152m*                        [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;147;147m*  [38;2;255;104;104mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;69;69mo                              [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0        [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;136;136m+     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;122;122m+                 [38;2;255;142;142m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;130;130m+  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                         [38;2;255;47;47mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;44;44mO  [38;2;255;2;2m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;84;84mo                              [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0        [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;148;148m*     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;122;122m+                 [38;2;255;142;142m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;142;142m*  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                         [38;2;255;74;74mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;3;3m0  [38;2;255;30;30m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;44;44mO                 [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;61;61mO  [38;2;255;39;39mO[38;2;255;0;0m0[38;2;255;0;0m0        [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;122;122m+                 [38;2;255;142;142m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;23;23m0                        [38;2;255;65;65mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;16;16m0   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                    [38;2;255;109;109m+[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0     [38;2;255;138;138m+[38;2;255;0;0m0[38;2;255;0;0m0        [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;122;122m+                 [38;2;255;142;142m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0   [38;2;255;27;27m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                        [38;2;255;19;19m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;86;86mo   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;3;3m0                    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [38;2;255;0;0m0[38;2;255;0;0m0        [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                   [38;2;255;17;17m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;110;110m+      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;122;122m+                 [38;2;255;142;142m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;4;4m0                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                   [38;2;255;18;18m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;107;107m+    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;33;33m0                       [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;43;43mO                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [38;2;255;2;2m0[38;2;255;0;0m0        [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                  [38;2;255;97;97mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;14;14m0       [38;2;255;61;61mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;70;70mo                 [38;2;255;64;64mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;113;113m+                   [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                  [38;2;255;101;101mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;73;73mo                     [38;2;255;40;40mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [38;2;255;124;124m+[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;20;20m0                  [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0       [38;2;255;23;23m0        [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;58;58mO                 [38;2;255;45;45mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;43;43mO         [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;30;30m0                    [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                 [38;2;255;46;46mO[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0        [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;98;98mo                   [38;2;255;31;31m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0         [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;149;149m*                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0      [38;2;255;129;129m+[38;2;255;122;122m+        [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;48;48mO               [38;2;255;161;161m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0            [38;2;255;11;11m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0               [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;8;8m0                     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                [38;2;255;1;1m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;85;85mo          [38;2;255;116;116m+[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;5;5m0                 [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;67;67mO           [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0               [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0       [0m
      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0            [38;2;255;139;139m+[38;2;255;9;9m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0                [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;1;1m0[38;2;255;156;156m*         [38;2;255;69;69mo[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;96;96mo                      [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;140;140m+           [38;2;255;141;141m*[38;2;255;9;9m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;161;161m*               [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;100;100mo            [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;123;123m+               [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;8;8m0[38;2;255;91;91mo          [38;2;255;4;4m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0     [38;2;255;109;109m+[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0       [0m
     [38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;24;24m0                     [38;2;255;24;24m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;142;142m*                       [38;2;255;19;19m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;11;11m0[38;2;255;151;151m*                    [38;2;255;33;33m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;49;49mO[38;2;255;86;86mo[38;2;255;99;99mo[38;2;255;85;85mo[38;2;255;52;52mO[38;2;255;7;7m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;121;121m+                    [38;2;255;153;153m*[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;18;18m0                 [0m
                                                    [38;2;255;99;99mo[38;2;255;29;29m0[38;2;255;0;0m0[38;2;255;44;44mO[38;2;255;128;128m+                                                                           [38;2;255;69;69mo[38;2;255;16;16m0[38;2;255;0;0m0[38;2;255;0;0m0[38;2;255;64;64mO                                                               [0m
                                                                                                                                                                                                        [0m
                                                                                                                                                                                                        [0m
"""


def get_loot(current_monster):
    loot_chance = random.randint(1, 100)
    item = None

    # Definiera en loot-tabell för varje monster
    loot_tables = {
        "Råtta": {
            "common": None,  # Ingen loot
        },
        "Skorpion": {
            "common": ["Träsvärd", "Läderhjälm", "Läderbröstplåt", "Läderbenskydd"],
            "chance": [10],  # 10%
        },
        "Slime": {
            "common": ["Träsvärd", "Läderhjälm"],
            "uncommon": ["Stensvärd", "Läderbröstplåt"],
            "rare": ["Rostigt järnsvärd", "Läderbenskydd"],
            "chance": [20, 30, 40],  # 20% common, 10% uncommon, 10% rare
        },
        "Goblin": {
            "common": ["Träsvärd", "Läderhjälm"],
            "uncommon": ["Stensvärd", "Läderbröstplåt"],
            "rare": ["Rostigt järnsvärd", "Läderbenskydd"],
            "chance": [30, 60, 75],  # 30%, 30%, 15%
        },
        "Zombie": {
            "common": ["Rostigt järnsvärd", "Järnhjälm"],
            "uncommon": ["Järnsvärd", "Järnbröstplåt"],
            "rare": ["Finslipat järnsvärd", "Järnbenskydd"],
            "chance": [20, 60, 75],  # 20%, 40%, 15%
        },
        "Spöke": {
            "common": ["Järnsvärd", "Järnhjälm"],
            "uncommon": ["Järnbenskydd", "Järnbröstplåt"],
            "rare": ["Silversvärd", "Finslipat Järnsvärd"],
            "chance": [30, 70, 85],  # 30%, 40%, 15%
        },
        "Vampyr": {
            "common": ["Silversvärd", "Silverhjälm"],
            "uncommon": ["Helvetets skrik", "Silverbröstplåt"],
            "rare": ["Gyllene Hjälm", "Gyllene Bröstplåt"],
            "chance": [40, 55, 70],  # 40%, 15%, 15%
        },
        "Varulv": {
            "common": ["Helvetets skrik", "Stormhjälm"],
            "rare": ["Blodherrens rapir", "Stormbröstplåt"],
            "chance": [70, 80],  # 70%, 10%
        },
        "Drake": {
            "common": ["Blodherrens rapir", "Drakhjälm"],
            "rare": ["Excalibur", "Drakbröstplåt", "Drakbenskydd"],
            "chance": [50, 100],  # 50%, 50%
        },
    }

    loot_table = loot_tables.get(current_monster.name)
    
    if loot_table:
            for category, chance_limit in zip(["common", "uncommon", "rare"], loot_table.get("chance", [])):
                if loot_chance <= chance_limit:
                    if loot_table.get(category):
                        item_name = random.choice(loot_table[category])

                        # Skapa rätt typ av objekt baserat på namnet
                        if "svärd" in item_name.lower():
                            item = Sword(item_name, random.randint(5, 15))  # Exempel: skapa ett svärd
                        elif "hjälm" in item_name.lower():
                            item = Helmet(item_name, random.randint(3, 8))  # Exempel: skapa en hjälm
                        elif "bröstplåt" in item_name.lower():
                            item = ChestArmor(item_name, random.randint(5, 12))  # Exempel: skapa bröstplåt
                        elif "benskydd" in item_name.lower():
                            item = LegArmor(item_name, random.randint(4, 10))  
                    break

    return item 



def monster_attack(player, current_monster):
    while current_monster.hp > 0 and player.hp > 0:
        # Monstrets attack
        damage = random.randint(2, 5) * current_monster.lvl // 2 - player.armor//2
        print(f"{current_monster.name} attackerar dig och gör {damage} skada!")
        time.sleep(1)
        player.hp = max(0, player.hp - damage)

        if player.hp > 0:
            print(f"Du överlever med {player.hp} HP kvar.")
            time.sleep(0.2)
        else:
            print(death_screen)
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
                item_loot = get_loot(current_monster)

                print(f"Du dödade {current_monster.name}, som droppar \033[38;5;226m{gold_loot} guld\033[0m.")
                if item_loot:
                    print(f"{current_monster.name} droppar också {item_loot.name}!")  # Visa föremålets namn
                    player_inventory.add_item(item_loot)  # Lägg till föremålet i inventoriet
                else:
                    print(f"{current_monster.name} droppar inga föremål.")

                # Lägg till XP och guld
                player.gold += gold_loot
                player.gain_xp(xp_loot)
                break
        elif svar == "2" or svar == "fly":
            #Försök att fly
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
player_command()

# SPEL-LOOP
while True:
    if 'current_monster' not in globals() or current_monster.hp <= 0:
        choose_door()

    monster_attack(player, current_monster)

    if player.hp <= 0:
        print(death_screen)
        exit()

    player_command()
