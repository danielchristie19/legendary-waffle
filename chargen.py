from random import *
import time
#CHARACTER CREATION FUNCTIONS
#JOB SELECT
def choose_job():
        job = raw_input("Please choose a class:\n -Voidweaver\n -Weaponmaster\n -Awakened\n").lower() #ADD NEW CLASSES TO THIS LIST...
        while job not in ["voidweaver", "1", "weaponmaster", "2", "awakened", "3", "time traveller", "4", "tiana"]: #...AND THIS ONE
                time.sleep(1)
                job = raw_input("\nPlease choose a valid class.\n").lower()
        if job == "1":
                job = "voidweaver"
        if job == "2":
                job = "weaponmaster"
        if job == "3":
                job = "awakened"
        if job == "4":
                job = "time traveller" #MAKE SURE TO CONVERT
        return job

def roll_stats(job, main_weapon):
        if job == "voidweaver":
                STR = randint(1, 5)
                DEX = randint(1, 5)
                INT = randint(3, 6)
                MaxHP = 8 + STR
        elif job in ["weaponmaster", "time traveller"]:
            if main_weapon in ["longsword", "an actual fucking gun"]:
                STR = randint(3, 5)
                DEX = randint(2, 5)
            elif main_weapon == "rapier":
                STR = randint(2, 5)
                DEX = randint(3, 5)
            INT = randint(1, 5)
            MaxHP = 12 + STR
        elif job == "awakened":
            STR = randint(1, 5)
            DEX = randint(1, 5)
            INT = randint(1, 5)
            MaxHP = 10 + STR
        return [STR, DEX, INT, MaxHP]

def equip_player(job):
    spell_1 = ""#
    spell_2 = ""
    spell_3 = ""
    if job == "voidweaver":
        main_weapon = "fists"
        armour = "void uniform"
        print " -Scorch\n -Singularity\n -Victory Fist\n -Rejuvinate\n -Spirit Barrier\n (type the names, don't use numbers. Sorry)"
        tmp_list = ["scorch", "singularity", "victory fist", "rejuvinate", "spirit barrier"]
        while spell_1 not in tmp_list:
            spell_1 = raw_input("\nChoose your first spell.\n").lower()
        while spell_2 not in tmp_list:
            spell_2 = raw_input("\nChoose your second spell.\n").lower()
        while spell_3 not in tmp_list:
            spell_3 = raw_input("\nChoose your third spell.\n").lower()



    elif job == "weaponmaster":
        main_weapon = ""
        armour = "plate mail"
        while main_weapon not in ["longsword", "rapier", "1", "2"]:
            main_weapon = raw_input("Choose your weapon:\n -Longsword\n -Rapier\n").lower()
            if main_weapon == "1":
                main_weapon = "longsword"
            elif main_weapon == "2":
                main_weapon = "rapier"

    elif job == "awakened":
            main_weapon = "longsword"
            armour = "leather"

    elif job == "time traveller":
            main_weapon = "an actual fucking gun"
            armour = "cool future armour"

    back_weapon = "no backup weapon"
    if main_weapon != "fists":
        print main_weapon,  "added to inventory!"
        time.sleep(1)
    print armour, "added to inventory!"
    time.sleep(1)
    return [main_weapon, armour, back_weapon, spell_1, spell_2, spell_3]

def level_up(STR, DEX, INT, MaxHP, level, player_exp, job, avatar, artifact, awaken):
        level += 1
        if level == 3:
            if job == "voidweaver":
                print "Your Avatar will now answer your summon!"
            elif job == "weaponmaster":
                artifact = True
                print "Your Artifact has been unleashed!"
            if job == "awakened":
                awaken = True
                print "Your true form has awakened!"
            time.sleep(1)
        print "Level Up! Level", level, "\nPlease Choose an Attribute to Enhance:"
        choice = raw_input(" - STR\n - DEX\n - INT\n").lower()
        time.sleep(1)
        stats = ["str", "1", "dex", "2", "int", "3"]
        while choice not in stats:
                print "please choose a valid attribute."
                choice = raw_input().lower()
        if choice in stats:
                MaxHP += 5
                if choice == "str" or choice == "1":
                        STR += 1
                        MaxHP = MaxHP + 1
                        print "STR increased to", STR, "!"
                if choice == "dex" or choice == "2":
                        DEX += 1
                        print "DEX increased to", DEX, "!"
                if choice == "int" or choice == "3":
                        INT += 1
                        print "INT increased to", INT, "!"
                time.sleep(1)
                print "Max HP increased to", MaxHP, "!"
        return [STR, DEX, INT, MaxHP, level, avatar, artifact, awaken]
        