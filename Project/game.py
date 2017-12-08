#! usr/bin/env python
from random import *
import time
import chargen
import combat
import town
import bestiary
##############################################################################################################################################
startup = True
if startup:
    PlayerName = raw_input("Greetings adventurer, what is your name?\n")
    job = chargen.choose_job()
    tmp_list = chargen.equip_player(job)
    main_weapon = tmp_list[0]
    armour = tmp_list[1]
    back_weapon = tmp_list[2]
    spell_1 = tmp_list[3]
    spell_2 = tmp_list[4]
    spell_3 = tmp_list[5]
    tmp_list = chargen.roll_stats(job, main_weapon)
    STR = tmp_list[0]
    DEX = tmp_list[1]
    INT = tmp_list[2]
    MaxHP = tmp_list[3]
    avatar = False
    artifact = False
    awaken = False
    awakening_scene = True
    PlayerHP = MaxHP
    level = 1
    grab = False
    poison = False
    poisoned = False
    burn = False
    potions = 5
    antidotes = 1
    player_gold = 9999999
    pre_battle_gold = 0
    player_exp = 0

while PlayerHP >= 0:
    if startup:
        print "A new adventure! You arrive in the town of Vale, ready to start your career as a hunter."
    elif PlayerHP <= PlayerHP/2:
        print "You return to town, bruised and weary..."
    elif player_gold > pre_battle_gold:
        print "You make your way back to town, ready to spend your new treasure."
    else:
        print "what's the point, man? Nothing even happened that time..."
    travel = ""
    travel = raw_input("Where would you like to visit?\n-Blacksmith\n-Apothecary\n-Inn\n-Arena\n-Guild\n").lower()
    if travel in ["1", "blacksmith"]:
        tmp_list = town.blacksmith(player_gold, main_weapon, back_weapon, armour, MaxHP)
        player_gold = tmp_list[0]
        main_weapon = tmp_list[1]
        armour = tmp_list[2]        
        back_weapon = tmp_list[3]

    if travel in ["2"]:
        exit()


















    elif travel in ["5", "guild"]:
        print "Welcome to the guild! Here is the quest we have for you today:"
        tmp_list = bestiary.encounter(level)
        EnemyName = tmp_list[0]
        EnemyHP = tmp_list[1]
        EnemyBlock = tmp_list[2]
        gold_reward = tmp_list[3]
        exp_reward = tmp_list[4]
        enemy_weak_attack = tmp_list[5]
        enemy_med_attack = tmp_list[6]
        enemy_strong_attack = tmp_list[7]
        print "Hunt 1", EnemyName
        raw_input = ("...")
#        quest_accept = ""
#        quest_accept = raw_input("Will you accept the quest? Y/N\n").lower()
#        if quest_accept in ["y", "yes", "1"]:
        if True:
            print "You leave town in search of your quarry..."
            time.sleep(1)
            print EnemyName, "appears!"
            time.sleep(1)
            pre_battle_gold = player_gold
            tmp_list = combat.scene(awakening_scene, avatar, artifact, awaken, player_exp, bestiary.enemy_attack, main_weapon, back_weapon, PlayerName, EnemyName, PlayerHP, MaxHP, EnemyHP, combat.attack, combat.heal, combat.enemy_choice, potions, antidotes, gold_reward, exp_reward, player_gold, combat.spell_properties, armour, level, EnemyBlock, STR, DEX, INT, job, enemy_weak_attack, enemy_med_attack, enemy_strong_attack, grab, poison, spell_1, spell_2, spell_3, poisoned)
            PlayerHP = tmp_list[0]
            potions = tmp_list[1]
            player_gold = tmp_list[2]
            player_exp = tmp_list[3]
            antidotes = tmp_list[4]

            while player_exp >= 100:
                player_exp -= 100
                tmp_list = chargen.level_up(STR, DEX, INT, MaxHP, level, player_exp, job, avatar, artifact, awaken)
                STR = tmp_list[0]
                DEX = tmp_list[1]
                INT = tmp_list[2]
                MaxHP = tmp_list[3]
                level = tmp_list[4]
                avatar = tmp_list[5]
                artifact = tmp_list[6]
                awaken = tmp_list[7]
    startup = False
    raw_input("Press enter to return to town")