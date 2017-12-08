from random import *
import time
#### COMBAT FUNCTIONS ###################################################################

def attack(STR, DEX, INT, main_weapon, artifact):   
    burn = False     
    if main_weapon == "fists":
            damage = randint(1, 4) + STR


    elif main_weapon == "longsword":
            damage = randint(1, 8) + ((STR * 3)/2)

    elif main_weapon == "avatar claws":
            damage = randint(1, 10) + INT + 10
            burn = True

    elif main_weapon == "divine sabre":
        damage = randint(1, 8) + (STR + DEX + INT)
        burn = True

    elif main_weapon == "rapier":
            damage = randint(1, 8) + DEX

    elif main_weapon == "greatsword":
            damage = randint(1, 6) + randint(1, 6) + ((STR * 3)/2)

    elif main_weapon == "bow":
            damage = (randint(1, 6)*2) + DEX

    elif main_weapon == "flame wand":
            damage = 1

    elif main_weapon == "an actual fucking gun":
            damage = 1000000
    elif main_weapon == "ciara's pathetic attempt at adding a gun":
            damage = 100000

    if artifact:
        if STR >= DEX and STR >= INT:
            damage = damage * 2
        elif INT >= DEX and INT >= STR:
            burn = True


    return [damage, burn]

def protection(armour, DEX, INT):
        if armour == "leather":
                defense = randint(1, 4) + (DEX / 2)
        
        elif armour == "plate mail":
                defense = randint(3, 6)

        elif armour == "void uniform":
                defense = randint(1, 2) + (DEX / 2)

        elif armour == "spirit barrier":
            defense = 2 + INT

        elif armour == "cool future armour":
                defense = 1000000
        elif armour == "sexy af":
                defense = 100000
        elif armour == "avatar":
            defense = randint(5,10) + INT
        elif armour == "cosmic warding field":
            defense = 8  
        elif armour == "chainmail":
                defense = randint(2, 5)

        return defense

def spell_properties(spell, INT, STR, level):
    spell_damage = 0
    own_damage = 0
    spell_text = ""
    spell_recoil_text = ""
    if spell == "scorch":
        spell_damage = randint(1, 6) + randint(1, 6) + INT
        spell_text = "You fire a bolt of dark fire from your palm!"
    if spell == "singularity":
        spell_damage = randint(5, 10) + randint(5, 10) + (INT * 2)
        spell_text = "Focusing your mind, you distort reality around your target, ripping the\nvery space apart between you and them."
        own_damage = spell_damage / 10
        spell_recoil_text = "You feel the exhaustion the spell has caused you."
    if spell == "victory fist":
        spell_damage = randint(10, 20) + (STR * 2)
        spell_text = "Focusing your will into your fist, you lash out and deliver an earth shattering punch!!"
        own_damage = 7 - INT
        spell_recoil_text = "Your feel your bones come close to snapping onimpact, but your magic\nholds you together... barely."
    if spell == "rejuvinate":
        spell_damage = randint(1, 5) * level
        spell_text = "You feel your wounds caressed by divine light from the avatar, and your pain fades."
    if spell == "spirit barrier":
        spell_damage = 2 + INT
        spell_text = "You surround yourself with an ethereal shield to ward off attack!"
    if spell == "summon avatar":
        spell_text = "Calling out to the void itself, you beckon the Avatar forthinto our world, and he\nrises before you, ready to do your bidding..."

    return [spell_damage, own_damage, spell_text, spell_recoil_text]

def heal(potions, level):
        gain = randint(1, 4) * level
        return gain

def enemy_choice():
        choice = randint(1, 10)
        if choice in [1, 2, 3, 4 ,5, 6, 7]:
                action2 = "attack"
        if choice in [8, 9]:
                action2 = "block"
        if choice in [10]:
                action2 = "surrender"
        return action2

###### COMBAT LOOP #######################################################################
def scene(awakening_scene, avatar, artifact, awaken, player_exp, enemy_attack, main_weapon, back_weapon, PlayerName, EnemyName, PlayerHP, MaxHP, EnemyHP, attack, heal, enemy_choice, potions, antidotes, gold_reward, exp_reward, player_gold, spell_properties, armour, level, EnemyBlock, STR, DEX, INT, job, enemy_weak_attack, enemy_med_attack, enemy_strong_attack, grab, poison, spell_1, spell_2, spell_3, poisoned):
        if awaken:
            if awakening_scene:
                print "You feel power surging within you, as you awaken to your true form!"
                raw_input("...")
                print "You ascend past your mortal body and summon forth your spiritual arms, ready for battle."
                raw_input("...")
            main_weapon = "divine sabre"
            back_weapon = "ethereal shield"
            armour = "cosmic warding field"
            PlayerHP += 10
            MaxHP += 10
            awakening_scene = False
        if main_weapon in ["bow"]:
            first_strike = raw_input("Get a first strike in with your bow? Y/N\n").lower()
            while first_strike not in ["y", "yes", "n", "no", "1", "2"]:
                first_strike = raw_input("Please choose yes or no.\n")
            if first_strike in ["y", "yes", "1"]:
                tmp_list = attack(STR, DEX, INT, main_weapon, artifact)
                damage = tmp_list[0]
                EnemyHP = EnemyHP - damage
                print PlayerName, "fires off a quick arrow and gets a first strike for", damage, "damage!"
            else:
                print PlayerName, "decides not to engage with a first strike."
            time.sleep(1)
                                
        turn_order = randint(0, 1)
        action1 = ""
        action2 = ""
        spell = ""
        use_item = ""
        burn = False

        while PlayerHP > 0 and EnemyHP > 0:
            turn_order = (turn_order + 1) % 2
            if spell == "exit" or use_item == "exit" or action1 in ["5", "stats"]:
                    turn_order = (turn_order + 1) % 2

            elif grab:
                print PlayerName, "has to break free!"
                grab = False
                turn_order = 0
                raw_input("...")

#PLAYER'S TURN-------------------------------------------------------------------------------------------------------------------------
            if turn_order == 1:
                if poison and spell != "exit" and use_item != "exit" and action1 not in ["5", "stats"]:
                    poisoned = True
                if poisoned and spell != "exit" and use_item != "exit" and action1 not in ["5", "stats"]:
                    PlayerHP-=1
                    print PlayerName, "takes 1 damage from the poison!"
                    if PlayerHP == 1:
                        poisoned = False
                        time.sleep(1)
                        print "The poison leaves your system..."
                    raw_input("...")


                action1 = ""
                action2 = ""
                spell = ""
                use_item = ""
                print PlayerName
                action1 = raw_input("What will you do?\n -Attack\n -Block\n -Magic\n -Items\n -Stats\n -Surrender\n").lower()
                actionlist = ["attack", "block", "items", "hp", "stats", "surrender", "magic", "1", "2", "3", "4", "5", "6"]


                while action1 not in actionlist:
                        print "\nsorry, that is not an action"
                        action1 = raw_input()


                                


                if action1 in ["attack", "1"]:
                        tmp_list = attack(STR, DEX, INT, main_weapon, artifact)
                        damage = tmp_list[0]
                        burn = tmp_list[1]
                        if damage < 0:
                                damage = 0
                        if action2 == "block":
                                damage = damage - EnemyBlock
                        EnemyHP = EnemyHP - damage
                        if damage == 0:
                                print EnemyName, "blocks the hit entirely!"
                        else:
                                print PlayerName, "hits", EnemyName, "for", damage, "damage!"
                                
                        if job == "weaponmaster" and main_weapon in ["bow", "rapier"]:
                            time.sleep(1)
                            tmp_list = attack(STR, DEX, INT, main_weapon, artifact)
                            damage = tmp_list[0]
                            if damage < 0:
                                    damage = 0
                            if action2 == "block":
                                    damage = damage - EnemyBlock
                            EnemyHP = EnemyHP - damage
                            if damage == 0:
                                    print EnemyName, "blocks the hit!"
                            else:
                                    print "Follow Up!", PlayerName, "hits", EnemyName, "for", damage, "damage!"
                        if job == "weaponmaster" and artifact and DEX >= STR and DEX >= INT:
                            time.sleep(1)
                            tmp_list = attack(STR, DEX, INT, main_weapon, artifact)
                            damage = tmp_list[0]
                            if damage < 0:
                                    damage = 0
                            if action2 == "block":
                                    damage = damage - EnemyBlock
                            EnemyHP = EnemyHP - damage
                            if damage == 0:
                                    print EnemyName, "blocks the hit!"
                            else:
                                    print "Artifact power!", PlayerName, "hits", EnemyName, "for", damage, "damage!"          
                                        
                        print
                        if EnemyHP < 0:
                                EnemyHP = 0
                        print EnemyName, "has", EnemyHP, "HP left!"
                        print
                        if EnemyHP == 0:
                                time.sleep(1)
                                break


                elif action1 in ["block", "2"]:
                        action1 = "block"
                        print PlayerName, "gets ready to block an attack!"

                elif action1 in ["magic", "3"]:
                        if job not in ["voidweaver", "tiana"] and main_weapon != "flame wand":
                                time.sleep(1)
                                print "...You try your hardest to conjure up some sort of magical\n energy, but alas, you are not a wizard and nothing happens..."


                        elif job in ["voidweaver", "tiana"]:

                                while spell not in [spell_1, spell_2, spell_3, "summon avatar"]:
                                    print "-Spell List-"
                                    print spell_1
                                    print spell_2
                                    print spell_3
                                    if avatar:
                                        print "summon avatar"
                                    spell = raw_input().lower()
                                    if spell == "1":
                                        spell = spell_1
                                    elif spell == "2":
                                        spell = spell_2
                                    elif spell == "3":
                                        spell = spell_3
                                    elif spell == "4":
                                        spell = "summon avatar"
                                    elif spell == "exit":
                                        break
                                    else:
                                        spell = raw_input("please pick a spell")
                                if spell in ["scorch", "victory fist", "singularity"]: #DAMAGING SPELLS

                                        tmp_list = spell_properties(spell, INT, STR, level)
                                        spell_damage = tmp_list[0]
                                        own_damage = tmp_list[1]
                                        spell_text = tmp_list[2]
                                        spell_recoil_text = tmp_list[3]
                                        EnemyHP = EnemyHP - spell_damage
                                        PlayerHP = PlayerHP - own_damage
                                        time.sleep(1)
                                        print spell_text
                                        if own_damage > 0:
                                            time.sleep(1)
                                            print spell_recoil_text
                                        if EnemyHP > 0:
                                            time.sleep(1)
                                            print "\n", EnemyName, "survives the attack!"
                                        else:
                                            time.sleep(1)
                                            print EnemyName, "is completely destroyed!"

                                elif spell in ["rejuvinate"]: #HEALING SPELLS
                                        tmp_list = spell_properties(spell, INT, STR, level)
                                        spell_damage = tmp_list[0]
                                        spell_text = tmp_list[2]
                                        PlayerHP += spell_damage
                                        if PlayerHP > MaxHP:
                                                PlayerHP = MaxHP
                                        print spell_text


                                elif spell in ["spirit barrier"]: #SHIELDING SPELLS
                                        tmp_list = spell_properties(spell, INT, STR, level)
                                        armour = "spirit barrier"
                                        spell_text = tmp_list[2]
                                        print spell_text

                                elif spell in ["summon avatar"]:
                                    tmp_list = spell_properties(spell, INT, STR, level)
                                    spell_text = tmp_list[2]
                                    print spell_text
                                    main_weapon = "avatar claws"
                                    back_weapon = "no backup weapon"
                                    armour = "avatar"

                        elif main_weapon == "flame wand" and spell != "exit":
                                spell = raw_input("Use the flame wand? Y/N\n").lower()
                                while spell not in ["yes", "no", "y", "n"]:
                                    spell = raw_input("Choose yes or no.\n")
                                if spell in ["yes", "y"]:
                                    spell = "scorch"
                                    tmp_list = spell_properties(spell, INT, STR, level)
                                    spell_damage = tmp_list[0]
                                    spell_text = tmp_list[2]
                                    print spell_text
                                    EnemyHP -= spell_damage

                                

                if action1 in ["items", "4"]:
                        while use_item != "exit":
                                print "\n--INVENTORY--\n", potions, "healing potions\n", antidotes, "antidotes\nmain weapon:", main_weapon, "\nbackup weapon:", back_weapon, "\narmour:", armour
                                use_item = raw_input("\nUse an item?\n").lower()
                                if use_item in ["healing potion", "1"] and potions > 0:
                                        gain = heal(potions, level)
                                        PlayerHP = PlayerHP + gain
                                        potions = potions -1
                                        if potions <0:
                                            potions = 0
                                        print PlayerName, "heals", gain, "HP!", potions, "healing potions left!"
                                        time.sleep(1)
                                        print
                                        if PlayerHP > MaxHP:
                                                PlayerHP = MaxHP
                                        print PlayerName, "is up to", PlayerHP, "HP!"
                                        break
                                elif use_item in ["healing potion", "1"] and potions == 0:
                                        print PlayerName, "has none of those left!"

                                if use_item in ["antidote", "2"] and antidotes > 0:
                                        poison = False
                                        antidotes = antidotes -1
                                        if antidotes <0:
                                            antidotes = 0
                                        print PlayerName, "cures their poison with an antidote!"
                                        time.sleep(1)
                                        break
                                elif use_item in ["antidote", "2"] and antidotes == 0:
                                        print PlayerName, "has none of those left!"

                                elif use_item in [main_weapon, "2"]:
                                    print "already equipped!"
                                elif use_item in [back_weapon, "3"]:
                                    if back_weapon == "no backup weapon":
                                        print "You have no weapon to equip!"
                                    if back_weapon in ["shield", "ethereal shield"]:
                                        print "It would be a bad idea to attack with a shield instead of an actual weapon."
                                    else:
                                        tmp = main_weapon
                                        main_weapon = back_weapon
                                        back_weapon = tmp
                                        print main_weapon, "equipped!"
                                else:
                                        if use_item != "exit":
                                                print "You cannot use that item right now."
                                time.sleep(1)
                elif action1 in ["stats", "5"]:
                        time.sleep(1)
                        print "Level:", level, "\nHP: ", PlayerHP, "/", MaxHP, "\nSTR: ", STR, "\nDEX: ", DEX, "\nINT: ", INT, "\n"

                elif action1 in ["surrender", "6"]:
                        PlayerHP = 0
                raw_input("...")
                print






    #ENEMY'S TURN--------------------------------------------------------------------------------------------------------------------------------------------
            if turn_order == 0:
                if burn:
                    EnemyHP -= 2
                    print EnemyName, "burns!"
                    raw_input("...")
                action2 = enemy_choice()

                if action2 == "attack":
                    tmp_list = enemy_attack(EnemyName, enemy_weak_attack, enemy_med_attack, enemy_strong_attack)
                    damage = tmp_list[0]
                    attack_text = tmp_list[1]
                    grab = tmp_list[2]
                    poison = tmp_list[3]
                    defense = protection(armour, DEX, INT)
                    if back_weapon in ["shield", "ethereal shield"]:
                        defense += 2
                    damage = damage - defense
                    if action1 == "block":
                        damage = damage - STR
                    if damage < 0:
                        damage = 0
                    PlayerHP = PlayerHP - damage 
                    if damage == 0 and action1 != "block" and armour != "mage armour":
                        print EnemyName, "'s attack is deflected by", PlayerName, "'s armour!"
                        grab = False
                        poison = False

                    elif damage == 0 and action1 != "block" and armour == "mage armour":
                        print PlayerName, "'s ethereal shield blocks ", EnemyName, "'s attack!"
                        grab = False
                        poison = False

                    elif damage == 0 and action1 == "block":
                        print EnemyName, "'s attack is blocked by", PlayerName, "!"
                        grab = False
                        poison = False

                    elif damage == 0 and armour == "avatar":
                        print EnemyName, "'s attack is blocked by the Avatar's huge form!"
                        grab = False
                        poison = False
                    else:
                            print attack_text
                            print
                            time.sleep(1)
                            if PlayerHP < 0:
                                    PlayerHP = 0
                            print PlayerHP, "HP left!"


                elif action2 == "block":
                        print EnemyName, "gets ready to block an attack!"





                elif action2 == "surrender":
                        print EnemyName, "turns and runs!"
                        EnemyHP = 0


                raw_input("...")


        if PlayerHP <= 0:
            print PlayerName, "falls to the ground, defeated..."
            time.sleep(2)
            print "\n\n G A M E    O V E R"
            exit()
        elif EnemyHP <=0:
            if action2 != "surrender":
                print PlayerName, "is victorious!"
                player_gold = player_gold + gold_reward
                player_exp += exp_reward
                time.sleep(1)
                print "Got", gold_reward, "gold!", player_gold, "gold in inventory!"
            raw_input("...")
        return [PlayerHP, potions, player_gold, player_exp, antidotes, awakening_scene]