from random import *
import combat

def enemy_attack(EnemyName, enemy_weak_attack, enemy_med_attack, enemy_strong_attack):
    attack_strength = randint(1, 5)
    if attack_strength in [1, 2]:
        attack_text = enemy_weak_attack
    elif attack_strength in [3, 4]:
        attack_text = enemy_med_attack
    elif attack_strength == 5:
        attack_text = enemy_strong_attack

    if EnemyName == "wolf":
        if attack_strength in [1, 2]:
            damage = randint(1, 4) + 1
            grab = False
            poison = False
        if attack_strength in [3, 4]:
            damage = randint(1, 6) + 2
            grab = False
            poison = False
        if attack_strength == 5:
            damage = randint(3, 6) + 2
            poison = False
            grab = True

    elif EnemyName == "barbarian":
        if attack_strength in [1, 2]:
            damage = randint(1, 4) + 1
            grab = False
            poison = False
        if attack_strength in [3, 4]:
            damage = randint(1, 8) + 3
            grab = False
            poison = False
        if attack_strength == 5:
            damage = randint(5, 8) + 3
            poison = False
            grab = True

    elif EnemyName == "basilisk":
        if attack_strength in [1, 2]:
            damage = randint(1, 4) + 1
            grab = False
            poison = False
        if attack_strength in [3, 4]:
            damage = randint(1, 6) + 2
            grab = False
            poison = False
        if attack_strength == 5:
            damage = randint(1, 8) + 2
            grab = False
            poison = True

    return [damage, attack_text, grab, poison]

def encounter(level):
    boys = ["wolf", "barbarian", "basilisk"]
    StatBlock = choice(boys)
    # WOLF
    if StatBlock == "wolf":
        EnemyName = "wolf"
        EnemyHP = 5 * level
        EnemyBlock = 2
        gold_reward = randint(20, 50)
        exp_reward = randint(15, 25)
        enemy_weak_attack = "The wolf gives you a shallow bite."
        enemy_med_attack = "The wolf tears at you with its jaws!"
        enemy_strong_attack = "The wolf's jaws latch onto your arm!!"
    # BARB  
    elif StatBlock == "barbarian":
        EnemyName = "barbarian"
        EnemyHP = 7 * level
        EnemyBlock = 5
        gold_reward = randint(50, 80)
        exp_reward = randint(25, 50)
        enemy_weak_attack = "The barbarian's axe grazes you."
        enemy_med_attack = "The barbarian's axe rips your flesh!"
        enemy_strong_attack = "The barbarian's axe lodges in your torso'!!"

    # MONSTER 
    elif StatBlock == "basilisk":
        EnemyName = "basilisk"
        EnemyHP = 10 * level
        EnemyBlock = 5
        gold_reward = randint(100, 200)
        exp_reward = randint(50, 75)
        enemy_weak_attack = "The basilisk's sharp tail lashes you."
        enemy_med_attack = "The basilisk lunges and bites you!"
        enemy_strong_attack = "The basilisk's poisoned fangs sink into your skin!!"

    return [EnemyName, EnemyHP, EnemyBlock, gold_reward, exp_reward, enemy_weak_attack, enemy_med_attack, enemy_strong_attack]