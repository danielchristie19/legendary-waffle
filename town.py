from random import *
import time
######### SHOP LOOP ######################################################################

def visit(player_gold, main_weapon, back_weapon, armour, potions, antidotes, MaxHP):
        shopping = ""
        item_name = ""

        if main_weapon != "greatsword" and back_weapon != "greatsword":
                MaxHP = MaxHP + 5

        print "Welcome to the shop!\n"
        time.sleep(1)
        while shopping != "exit":
                print "You have", player_gold, "gold.\n"
                time.sleep(1)
                shopping = raw_input("what would you like to buy?\n - ITEMS -\n - healing potion - 15g\n - antidote - 30g\n\n - WEAPONS -\n -rapier - 20 gold\n -greatsword - 50g\n -bow - 60g\n -flame wand - 80g\n\n - ARMOUR -\n - chainmail - 75g\n").lower()
                item_cost = 0
                if shopping == "exit":
                        break

                elif shopping == "healing potion":
                        potions += 1
                        item_cost = 15
                elif shopping == "antidote":
                    antidotes += 1
                    item_cost = 30
                elif shopping == "rapier":
                    item_cost = 20

                elif shopping == "greatsword":
                        item_cost = 50

                elif shopping == "bow":
                        item_cost = 60

                elif shopping == "flame wand":
                        item_cost = 80

                elif shopping == "chainmail":
                    armour = "chainmail"
                    item_cost = 75
                else:
                        print "sorry, we don't have any of those."
                        time.sleep(1)
                if  player_gold >= item_cost:
                    player_gold = player_gold - item_cost
                    if item_cost != 0:
                        print shopping, "added to inventory!"
                        time.sleep(1)

                    if shopping in ["rapier", "greatsword", "bow", "flame wand"]:
                        weapon_slot = ""
                        while weapon_slot not in ["yes", "y", "no", "n"]:
                            weapon_slot = raw_input("Would you like to equip it now? Y/N\n").lower()
                            if weapon_slot in ["yes", "y"]:
                                tmp = main_weapon
                                main_weapon = shopping
                                back_weapon = tmp
                                print main_weapon, "equipped!"
                            elif weapon_slot in ["no", "n"]:
                                back_weapon = shopping
                                print back_weapon, "set as backup weapon!"



                elif player_gold < item_cost:
                        print "sorry, you cannot afford that!"
                        time.sleep(1)
        print
        print "Thank you for shopping! Come again!"
        time.sleep(1)


        if main_weapon != "greatsword" and back_weapon != "greatsword":
                MaxHP = MaxHP - 5
        return [player_gold, main_weapon, armour, potions, antidotes, back_weapon]


def hub(PlayerHP, player_gold, pre_battle_gold, startup):
    if startup:
        print "A new adventure! You arrive in the town of Vale, ready to start your career as a hunter."
    elif PlayerHP <= PlayerHP/2:
        print "You return to town, bruised and weary..."
    elif player_gold > pre_battle_gold:
        print "You make your way back to town, ready to spend your new treasure."
