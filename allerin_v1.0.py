import os, random

run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False
witch = False
pendant = False

HP = 50
HPMAX = HP
ATK = 50
pot = 10
elix = 10
gold = 100
x = 3
y = 3



#        x = 0        x = 1       x = 2       x = 3       x = 4       x = 5       x = 6
map = [["desert",   "desert",   "desert",   "desert",   "mountain", "mountain", "beach"],      # y = 0
       ["desert",   "desert",   "desert",   "plains",   "river",    "river",    "beachRiver"], # y = 1
       ["desert",   "plains",   "plains",   "bridge",    "plains",   "mountain", "cliff"],      # y = 2
       ["plains",   "plains",   "river",    "town",     "shop",     "mountain", "cave"],       # y = 3
       ["plains",   "river",    "fields",   "castle",   "garden",   "mountain", "beach"]]      # y = 4

yLen = len(map)-1
xLen = len(map[0])-1

biom = {
    "desert": {
        "t": "DESERT",
        "e": True},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "beach": {
        "t": "BEACH",
        "e": False},
    "plains": {
        "t": "PLAINS",
        "e": True},
    "river": {
        "t": "RIVER",
        "e": False},
    "beachRiver": {
        "t": "RIVER INTAKE",
        "e": False},
    "cliff": {
        "t": "CLIFF",
        "e": False},
    "town": {
        "t": "TOWN CENTER",
        "e": False},
    "bridge": {
        "t": "BRIDGE",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "cave": {
        "t": "CAVE",
        "e": True},
    "fields": {
        "t": "FIELDS",
        "e": False},
    "castle": {
        "t": "CASTLE",
        "e": False},
    "garden": {
        "t": "GARDEN",
        "e": False,
    }
}

eList = ["Wolf", "Skeleton", "Goblin", "Orc"]

mobs = {
    "Wolf": {
        "hp": 20,
        "at": 4,
        "go": 10
    },
    "Skeleton": {
        "hp": 25,
        "at": 6,
        "go": 15
    },
    "Goblin": {
        "hp": 15,
        "at": 3,
        "go": 5
    },
    "Orc": {
        "hp": 30,
        "at": 8,
        "go": 20
    },
    "Evil King": {
        "hp": 100,
        "at": 12,
        "go": 100
    },
    "Old Witch": {
        "hp": 200,
        "at": 20,
        "go": 500
    }
}

def clear():
    os.system("cls")

def draw():
    print("Xx----------------------xX")

def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key),
        str(pendant)
    ]
        
    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX
    print(name + "'s HP is replenished to " + str(HP) + "!")

def battle():
    global fight, play, run, HP, pot, elix, gold, boss, witch

    if boss:
        enemy = "Evil King"
    elif witch:
        enemy = "Old Witch"
    else:
        enemy = random.choice(eList)

    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        draw()
        print("You are attacked! Fight the " + enemy + "!")
        draw()
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(name + "'s HP: " + str(HP) + "/" + str(HPMAX))
        print("POTIONS: " + str(pot))
        print("ELIXIR: " + str(elix))
        draw()
        print("1 - ATTACK")
        if pot > 0:
            print("2 - USE POTION (30HP)")
        if elix > 0:
            print("3 - USE ELIXIR (50HP)")
        draw()

        choice = input(">> ")

        if choice == "1":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damage to the " + enemy + ".")
            if hp > 0:
                HP -= atk
                print(enemy + " hits " + name + " for " + str(atk) + ".")
            input("# ")
        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(enemy + " hits " + name + " for " + str(atk) + ".")
            else:
                print(name + " doesn't have any potions!")
            input("# ")
        elif choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                HP -= atk
                print(enemy + " hits " + name + " for " + str(atk) + ".")
            else:
                print(name + " doesn't have any elixirs!")
            input("# ")

        if HP <= 0:
            print(enemy + " defeated " + name + "...")
            draw()
            fight = False
            play = False
            print("GAME OVER")
            input("# ")
            quit()

        if hp <= 0:
            print(name + " has defeated the " + enemy + "!")
            draw()
            fight = False
            gold += g
            print(name + " picked up " + str(g) + " gold from the " + enemy + "!")
            if random.randint(0, 100) < 20:
                pot += 1
                print(name + " found a potion!")
            if enemy == "Evil King":
                draw()
                print("...What?")
                input("# ")
                print("What am I doing here?")
                input("# ")
                print("What happened to me?")
                input("# ")
                print("What have I done...")
                input("# ")
                print("I am deeply ashamed for the dread I have brought upon my kingdom...")
                input("# ")
                print("An evil witch whom I used to trust has betrayed me and cast her spells on me.")
                input("# ")
                print("She has likely fled the castle by now. I don't know where she'd go.")
                input("# ")
                print("Ask around for her whereabouts and take care of her.")
                input("# ")
                print("I here the Shopkeep sells good information.")
                input("# ")
                print("Leave me now. I need to be alone, for I am no king...")
                input("# ")
                boss = False
                pendant = True
                save()
                quit()
                
                
            if enemy == "Old Witch":
                draw()
                print("How could you defeat me?!")
                input("# ")
                print("I am all powerfull!")
                input("# ")
                print("I am all knowing!")
                input("# ")
                print("I am.....")
                input("# ")
                print(".................")
                input("# ")
                print("The witch is dead. You, " + name + " have saved the Kingdom of Allerin once and for all!")
                input("# ")
                print("THANK YOU FOR PLAYING!")
                draw()
                save()
                quit()

            input ("# ")
            clear()

def shop():
    global buy, gold, pot, elix, ATK, pendant, HPMAX

    while buy:
        if pendant:
            clear()
            print(" SHOP~~~~~~~SHOP~~~~~~~SHOP")
            print("|..........................|")
            print("|POTION..............5 GOLD|")
            print("|ELIXIR.............10 GOLD|")
            print("|VISIT BLACKSMITH...20 GOLD|")
            print("|HEARTY MEAL........20 GOLD|")
            print("|..........................|")
            print("|SECRET.............15 GOLD|")
            print(" SHOP~~~~~~~SHOP~~~~~~~SHOP")
            draw()
            print("GOLD: " + str(gold))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elix))
            print("ATK: " + str(ATK))
            draw()
            print("1 - BUY POTION (30HP)")
            print("2 - BUY ELIXIR (MAXHP)")
            print("3 - VISIT BLACKSMITH (+2ATK)")
            print("4 - HEARTY MEAL (+20MAXHP)")
            print("5 - SECRET")
            print("0 - LEAVE")
            draw()

            choice = input(">> ")
    
            if choice == "1":
                if gold >= 5:
                    pot += 1
                    gold -= 5
                    print("The Shopkeep hands you a potion.")
                    input("# ")
                else:
                    print("The Shopkeep shakes his head and points to the sign.")
                    input("# ")
                    print(name + " does not have enough gold.")
                    input("# ")
            elif choice == "2":
                if gold >= 10:
                    elix += 1
                    gold -= 10
                    print("The Shopkeep hands you an elixir.")
                    input("# ")
                else:
                    print("The Shopkeep shakes his head and points to the sign.")
                    input("# ")
                    print(name + " does not have enough gold.")
                    input("# ")
            elif choice == "3":
                if gold >= 20:
                    ATK += 2
                    gold -= 20
                    print("The Shopkeep takes " + name + "'s sword.")
                    input("# ")
                    print("A loud hammering can be heard from the back of the shop.")
                    input("# ")
                    print("The Shopkeep returns " + name + "'s sword. It looks sharper.")
                    input("# ")
                else:
                    print("The Shopkeep shakes his head and points to the sign.")
                    input("# ")
                    print(name + " does not have enough gold.")
                    input("# ")
            elif choice == "4":
                if gold >= 20:
                    HPMAX += 20
                    gold -= 20
                    print("The Shopkeep places a large plate of meat in front of " + name + ".")
                    input("# ")
                    print(name + " devours the plate. They feel stronger.")
                else:
                    print("The Shopkeep shakes his head and points to the sign.")
                    input("# ")
                    print(name + " does not have enough gold.")
                    input("# ")

            elif choice == "5":
                if gold >= 15:
                    gold -= 15
                    print("The Shopkeep leans over the counter and gestures to come closer.")
                    input("# ")
                    print("He tells of rumors of an old witch living in a cave off to the east.")
                    input("# ")
            elif choice == "0":
                buy = False
                
        else:
            clear()
            print(" SHOP~~~~~~~SHOP~~~~~~~SHOP")
            print("|..........................|")
            print("|POTION..............5 GOLD|")
            print("|ELIXIR.............10 GOLD|")
            print("|VISIT BLACKSMITH...20 GOLD|")
            print("|..........................|")
            print("|..........................|")
            print(" SHOP~~~~~~~SHOP~~~~~~~SHOP")
            draw()
            print("GOLD: " + str(gold))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elix))
            print("ATK: " + str(ATK))
            draw()
            print("1 - BUY POTION (30HP)")
            print("2 - BUY ELIXIR (MAXHP)")
            print("3 - VISIT BLACKSMITH (+2ATK)")
            print("0 - LEAVE")
            draw()

            choice = input(">> ")
    
            if choice == "1":
                if gold >= 5:
                    pot += 1
                    gold -= 5
                    print("The Shopkeep hands you a potion.")
                    input("# ")
                else:
                    print("The Shopkeep shakes his head and points to the sign.")
                    input("# ")
                    print(name + " does not have enough gold.")
                    input("# ")
            elif choice == "2":
                if gold >= 10:
                    elix += 1
                    gold -= 10
                    print("The Shopkeep hands you an elixir.")
                    input("# ")
                else:
                    print("The Shopkeep shakes his head and points to the sign.")
                    input("# ")
                    print(name + " does not have enough gold.")
                    input("# ")
            elif choice == "3":
                if gold >= 20:
                    ATK += 2
                    gold -= 20
                    print("The Shopkeep takes " + name + "'s sword.")
                    input("# ")
                    print("A loud hammering can be heard from the back of the shop.")
                    input("# ")
                    print("The Shopkeep returns " + name + "'s sword. It looks sharper.")
                    input("# ")
                else:
                    print("The Shopkeep shakes his head and points to the sign.")
                    input("# ")
                    print(name + " does not have enough gold.")
                    input("# ")
            elif choice == "0":
                buy = False

def mayor():
    global speak, key, ATK, pendant

    while speak:

        if not pendant:
            clear()
            draw()
            print("Hello traveler! May I ask your name?")
            input("# ")
            if ATK > 10:
                print("Wellmet, " + name + "! You look like a capable adventurer.")
                input("# ")
                print("I have a request of you.")
                input("# ")
                print("The kingdom of Allerin is in terrible trouble as of late.")
                input("# ")
                print("The King has gone mad! Some terrible evil has overcome him!")
                input("# ")
                print("If you could defeat him in battle, maybe he will come to his senses.")
                input("# ")
                print("I will give you the key to the castle.")
                input("# ")
                print("I beg of you to help us save our king!")
                key = True
            else:
                print("Hello, " + name + ". I suggest you pass through quickly. Dark times are upon us.")
                input("# ")
                print("Perhaps if you were stronger, you could help us...")
                key = False

            draw()
            print("1 - LEAVE")
            draw()

            choice = input(">> ")

            if choice == "1":
                speak = False

        else:
            clear()
            draw()
            print("You've freed the King!")
            input("# ")
            print("Sorry, but I've never heard of any witch around here.")
            input("# ")
            print("Maybe you could ask the Shopkeep. He knows everything that goes on around the kingdom.")
            draw()
            print("1 - LEAVE")
            draw()

            choice = input(">> ")

            if choice == "1":
                speak = False


def castle():
    global boss, key, fight

    while boss:
        clear()
        draw()
        print(name + " approaches the steps to the castle.")
        draw()
        if key:
            print("1 - ENTER CASTLE")
        print("2 - TURN BACK")
        draw()


        choice = input(">> ")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False


def cave():
    global witch, fight, pendant

    while witch:
        clear()
        draw()
        print(name + " approaches the mouth of a cave. Cackling can be heard deep inside.")
        draw()
        if pendant:
            print("1 - ENTER CAVE")
        print("2 - TURN BACK")
        draw()


        choice = input(">> ")

        if choice == "1":
            if pendant:
                fight = True
                battle()
        elif choice == "2":
            witch = False


while run:
    while menu:
        clear()
        print("Xx--------ALLERIN--------xX")
        print("1.) NEW GAME")
        print("2.) LOAD GAME")
        print("3.) RULES")
        print("4.) EXIT PROGRAM")
        print("Xx-----------------------xX")
        print("           v1.0")


        if rules:
            clear()
            print("~.................................WELCOME TO ALLERIN....................................~")
            print(" ")
            print("Allerin is a text-based RPG coded by one person over the span of a few days.")
            print("While it is pretty bare bones at the moment, there are plans to update Allerin with more")
            print("features in coming updates to make it larger and have more to do. So far, it consists of")
            print("a traversable 7x5 grid map, random battles, two boss fights, a shop, and four NPCs.")
            input(" ")
            print("~.....................................HOW TO PLAY.......................................~")
            print("MAIN MENU")
            print("           1.) NEW GAME....................creates a new save file in the game directory")
            print("           2.) LOAD GAME.............loads an existing save file from the game directory")
            print("           3.) RULES................................................displays this screen")
            print("           4.) EXIT PROGRAM.....................closes the program and quits to terminal")
            print(" ")
            print("STATUS")
            print("           HP/MAX................................your current health/your maximum health")
            print("           ATK............................your attack power a.k.a how much damage you do")
            print("           POTIONS.......................the amount of potions you have, they heal 20 HP")
            print("           ELIXIRS..............the amount of elixirs you have, they heal you to full HP")
            print("           GOLD........................amount of gold you have, can be spent at the shop")
            print("           COOR: [x][y]................................your location on the 7x5 grid map")
            input(" ")
            print("To upgrade your stats, you can visit the shop located to the east of the Town Center and")
            print("see what the Shopkeep has in stock.")
            input(" ")
            print("To earn gold to spend at the shop, you need to hunt monsters, be it skeletons, wolves,")
            print("or orcs. These enemies spawn randomly and can be found in the desert, plains, and ")
            print("mountains of Allerin.")
            input(" ")
            print("To keep track of where you are and where you're going, I reccomend drawing a map of each")
            print("of the tiles you go to. You should also keep notes of things people mention. It might be")
            print("important later in your quest!")
            input(" ")
            print("Allerin does autosave upon movement and exit of the game. You don't have to worry about")
            print("your progress being lost!")
            input(" ")
            print("Happy questing, traveler! And good luck.")
            input(" ")
            print("Created by Jesse Manchester")
            rules = False
            choice = ""
            input("# ")
        else:
            choice = input(">> ")

        if choice == "1":
            name = input(">> What is your name, traveler? ")
            menu = False
            play = True
        elif choice == "2":

            try: 

                f = open("load.txt.", "r")
                loadList = f.readlines()
                if len(loadList) == 10:
                    name = loadList[0][:-1]
                    HP = int(loadList[1][:-1])
                    ATK = int(loadList[2][:-1])
                    pot = int(loadList[3][:-1])
                    elix = int(loadList[4][:-1])
                    gold = int(loadList[5][:-1])
                    x = int(loadList[6][:-1])
                    y = int(loadList[7][:-1])
                    key = bool(loadList[8][:-1])
                    pendant = bool(loadList[9][:-1])
                    print("Welcome back, " + name + "!")
                    input("# ")
                    menu = False
                    play = True
                else:
                    print("Corrupt save file!")
                    input("# ")
            except OSError:
                print("No save file detected!")
                input("# ")

        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()
        

    while play:
        save()  # autosave
        clear()

        if not standing:
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) <= 20:
                    fight = True
                    battle()

        if play:    
            draw()
            print("LOCATION: " + biom[map[y][x]]["t"])
            draw()
            print("NAME: " + name)
            print("HP: " + str(HP) + "/" + str(HPMAX))
            print("ATK: " + str(ATK))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elix))
            print("GOLD: " + str(gold))
            print("COORD: [" + str(x) + "]-[" + str(y) + "]")
            draw()
            print("0 - SAVE AND QUIT")
            if y > 0:
                print("1 - NORTH")
            if x < xLen:
                print("2 - EAST")
            if y < yLen:
                print("3 - SOUTH")
            if x > 0:
                print("4 - WEST")
            if pot > 0:
                print("5 - USE POTION (30HP)")
            if elix > 0:
                print("6 - USE ELIXIR (50hp)")
            if map[y][x] == "shop" or map[y][x] == "town" or map[y][x] == "castle" or map[y][x] == "cave":
                print("7 - ENTER")
            draw()

            dest = input(">> ")

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False
            elif dest == "2":
                if x < xLen:
                    x += 1
                    standing = False
            elif dest == "3":
                if y < yLen:
                    y += 1
                    standing = False
            elif dest == "4":
                if x > 0:
                    x -= 1
                    standing = False
            elif dest == "5":
                if pot > 0:
                    pot -= 1
                    heal(30)
                else:
                    print(name + " doesn't have any potions!")
                input("# ")
                standing = True
            elif dest == "6":
                if elix > 0:
                    elix -= 1
                    heal(50)
                else:
                    print(name + " doesn't have any elixirs!")
                input("# ")
                standing = True
            elif dest == "7":
                if map[y][x] == "shop":
                    buy = True
                    shop()
                if map[y][x] == "town":
                    speak = True
                    mayor()
                if map[y][x] == "castle":
                    boss = True
                    castle()
                if map[y][x] == "cave":
                    witch = True
                    cave()
            else:
                standing = True
