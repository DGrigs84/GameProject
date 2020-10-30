#!/usr/bin/env python3

# Hero's stats including leveling information, strength, dexterity, and Intelligence
hero_lvl = 1
hero_xp = 21
hero_lvlnext = 20

hStr = 0
hDex = 0
hInt = 0

# While loop used to increase player's level
while hero_xp >= hero_lvlnext: 
    hero_lvl += 1   # Hero's level +1
    hero_xp = hero_xp - hero_lvlnext # Most likely xp will surpass required xp 
    hero_lvlnext = round(hero_lvlnext*1.6) # Will take herolvlnext variable, multiply it by 1.6, and round it if there's a decimal.

if hero_xp < hero_lvlnext:
    print(hero_lvlnext - hero_xp, 'experience points until a level up!')
else:
    print('Level:', hero_lvl)
    print('Exp:  ', hero_xp)
    print('Next: ', hero_lvlnext)