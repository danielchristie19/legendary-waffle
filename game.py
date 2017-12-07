#! usr/bin/env python
from random import *
import time
import chargen
import combat
import shop
import bestiary
##############################################################################################################################################

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
burn = False
potions = 5
antidotes = 1
player_gold = 0
player_exp = 0
startup = True

while PlayerHP >= 0:

    tmp_list = bestiary.encounter(level)
    EnemyName = tmp_list[0]
    EnemyHP = tmp_list[1]
    EnemyBlock = tmp_list[2]
    gold_reward = tmp_list[3]
    exp_reward = tmp_list[4]
    enemy_weak_attack = tmp_list[5]
    enemy_med_attack = tmp_list[6]
    enemy_strong_attack = tmp_list[7]

    print EnemyName, "appears!"
    time.sleep(1)
    pre_battle_gold = player_gold
    tmp_list = combat.scene(awakening_scene, avatar, artifact, awaken, player_exp, bestiary.enemy_attack, main_weapon, back_weapon, PlayerName, EnemyName, PlayerHP, MaxHP, EnemyHP, combat.attack, combat.heal, combat.enemy_choice, potions, antidotes, gold_reward, exp_reward, player_gold, combat.spell_properties, armour, level, EnemyBlock, STR, DEX, INT, job, enemy_weak_attack, enemy_med_attack, enemy_strong_attack, grab, poison, spell_1, spell_2, spell_3)
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

    choice = ""
    while choice not in ["yes", "y", "no", "n"]:
            choice = raw_input("Enter the shop? Y/N\n").lower()
            if choice == "y" or choice == "yes":
                    tmp_list = shop.visit(player_gold, main_weapon, back_weapon, armour, potions, antidotes, MaxHP)
                    player_gold = tmp_list[0]
                    main_weapon = tmp_list[1]
                    armour = tmp_list[2]        
                    potions = tmp_list[3]
                    antidotes = tmp_list[4]
                    back_weapon = tmp_list[5]
            elif choice == "n" or choice == "no":
                    print "Come Again!\n"
            else:
                    print "Please choose yes or no."

    startup = False
    raw_input("Press enter to keep fighting.")