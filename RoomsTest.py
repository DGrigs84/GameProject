#!/usr/bin/env python3

def ShowInstructions():
    print('''
__________    _____ _____________________        __________    _____    _________.____________          ____________________  ________ 
\______   \  /  _  \\\\______   \_   _____/        \______   \  /  _  \  /   _____/|   \_   ___ \         \______   \______   \/  _____/ 
 |    |  _/ /  /_\  \|       _/|    __)_   ______ |    |  _/ /  /_\  \ \_____  \ |   /    \  \/   ______ |       _/|     ___/   \  ___ 
 |    |   \/    |    \    |   \|        \ /_____/ |    |   \/    |    \/        \|   \     \____ /_____/ |    |   \|    |   \    \_\  \\
 |______  /\____|__  /____|_  /_______  /         |______  /\____|__  /_______  /|___|\______  /         |____|_  /|____|    \______  /
        \/         \/       \/        \/                 \/         \/        \/             \/                 \/                  \/
                                                BARE-BASIC-RPG

                                         ╔═════════╗                                                           ╔════════════════╗ 
                                         ║ ACTIONS ║                                                           ║ HELPFUL HINTS! ║
                                         ╚═════════╝                                                           ╚════════════════╝
  ╔══════════════════════════════════════╗         ╔════════════════════════════════════════╗
  ║             MAP ACTIONS              ║         ║             BATTLE ACTIONS             ║    ~ Type 'menu' at anytime while in the
  ╠══════════════════════════════════════╣         ╠════════════════════════════════════════╣       map to bring up the list of map actions! 
  ║ GO [ EX: "GO <DIRECTION>" ]          ║         ║ ATTACK                                 ║
  ╠══════════════════════════════════════╣         ║  - Your basic action. No AP required.  ║    ~ Careful! Items are scarce! If you don't think
  ║ USE [ EX: "USE <ITEM>" ]             ║         ╠════════════════════════════════════════╣       you're strong enough...GRIND!
  ╠══════════════════════════════════════╣         ║ SKILL [ EX: "SKILL <NAME>" ]           ║
  ║ EQUIP [ EX: "EQUIP <ITEM>" ]         ║         ║  - Use any skills you may know.        ║    ~ Your only means of healing is your
  ╠══════════════════════════════════════╣         ║    * Some skills are learned through   ║       'First Aid' ability which you learned during
  ║ INTERACT [ EX: "INTERACT <OBJECT>" ] ║         ║      reading scrolls!                  ║       training. 
  ╠══════════════════════════════════════╣         ╠════════════════════════════════════════╣
  ║ INVENTORY / INV                      ║         ║ ITEM  [ EX: "ITEM <NAME>" ]            ║    ~ Some items provide AP, while a few others give 
  ╠══════════════════════════════════════╣         ║  - Use an item you may have            ║       a stat boost
  ║ STATUS                               ║         ╠════════════════════════════════════════╣
  ╠══════════════════════════════════════╣         ║ RUN                                    ║    ~ All skills require AP. Even HEALING! Prioritize 
  ║ QUIT / Q                             ║         ║  - Escape the battle. May not succeed. ║       so you can conserve enough AP to stay alive! 
  ╚══════════════════════════════════════╝         ╚════════════════════════════════════════╝

SUMMARY:
--------
After a long march north you awaken in your tent after your battalion hd set up camp for the night.
 You're near the base of the Dark Wizard's castle. Your raid on the castle is about to begin! ''')

def ShowStatus():
    # Displays the player's current location
    print('\n╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗')
    print(' ● ' + rooms[CurrentRoom]['desc'])
    # Also display any items in the room, including seperation lines 
    if "invitem" in rooms[CurrentRoom]:
        print('╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣')
        print(' ‣ ' + rooms[CurrentRoom]['item'])
    if "eqitem" in rooms[CurrentRoom]:
        print('╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣')
        print(' ⁍ ' + rooms[CurrentRoom]['gear'])
    if "envitem" in rooms[CurrentRoom]:
        print('╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣')
        print(' ➼ ' + rooms[CurrentRoom]['engage'])
    print('╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝')

# Player's Inventory
inventory = []
# Player's Equipment
equipment = []

# The dictionary used to link the rooms together
rooms = {
        'Tent': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Camp',
                'desc': 'There is a pile of old blankets infused with your sweat and blood. There is some light shining into the tent through the opening in the \'North\'.',
                'invitem': 'breakfast',
                'item': 'You notice your BREAKFAST lying on the ground next to the sheets. It\'s probably a good idea to eat it now.\n      ~ [Use the \'get BREAKFAST\' command to add the item to your inventory, followed by \'use BREAKFAST\' to eat it]'
                },
        'Camp': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Drawbridge',
                'desc': 'You muster with the rest of the knights. After an uninspiring speech by your commander, you\'re told to move out.\n     You prepare to march further \'North\' to the Dark Wizard\'s castle.\n       ...All hopes rest on this last attack. There\'s no turning back now.'
                },
        'Drawbridge': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Courtyard_Main',
                'desc': 'As you and your comrades approach the castle, you notice the drawbridge has already been lowered. \n     \"Good fortunes men!\" the Commander shouts. \"Our previous raids must have destroyed the counterbalance! These demons are wide open for a frontal assault!\"\n                                                     \"CCCHHHAAAAAAAAARRRGGGEEE!!!\"\n   You feel something is amiss, but orders are orders. You rush forward across the bridge, laid out over a chasm which looks as though it leads down to Hell itself.\n     Just as your battalion reaches halfway across the bridge, your greeted by the sound of laughter so cold you can see your breath.\n   Screams of agony errupt behind you. Looking back, you see some of your comerades engulfed in what appears to be black flames.\n     You also take note the drawbridge had caught fire as well, blocking your only escape.\n   Your comerades rush into the the castle, swords drawn, ready to use skills they trained so hard to master.\n     Your only option is to follow suit and rush \'North\' to the inner walls of the castle.\n  '
                },
        'Courtyard_Main': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Castle_Entrance',
                'east': 'Courtyard_East',
                'west': 'Courtyard_West',
                'desc': 'There\'s no going back, your only escape is now nothing but ash. You\'re standing in the main area of the castle courtyard.\n     Dead trees. Dead grass. A premonition of things to come? \n  ~ North: Looks as though the entrance to the castle is up ahead. \n  ~ West: You once heard screaming coming from that direction. You can see something glistening from a nearby tree that caught fire. \n  ~ East: You see nothing but more dead foliage.',
                'eqitem': 'sword',
                'gear': 'You dropped your SWORD. Mind still racing. Heart beating so hard it seems as though it will burst out of your chest.\n     Just being in the Dark Wizard\'s presence instilled you with a fear unlike any you\'ve felt before.\n   But this is no time to be weak! Pick up your SWORD and fight! For everlasting peace!\n     Use the \'equip\' command to pick up weapons and armor. Type \'equip SWORD\' to grab your sword!',
                'equip': 'You pick your sword up off the ground and sheathe it. It\'s slighly chipped, but still sharp as ever. It\'s been the most reliable companion you\'ve had this journey.\n    No way you\'re leaving it behind.'
                },
        'Courtyard_West': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Courtyard_Midwest',
                'east': 'Courtyard_Main',
                'desc': 'Body parts are scattered everywhere. Human and monster alike. Blood-soaked armor glistens off the fire like a dragon\'s eye. \n  ~ North: Looks like more evidence a battle took place.  You don\'t notice any movement. \n  ~ East: The main area of the courtyard.  Feels more like the entrance to a nightmare.'
                },
        'Courtyard_Midwest': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Courtyard_Northwest',
                'south': 'Courtyard_West',
                'desc': 'Signs of another battle. What else would there be? It looks as though it ended in a draw.  Both man and monster lay dead near a lever.\n     ....The monster appears to be missing a hand.... \n  ~ North: There appears to be nothing but rotting trees. Evidence of an old orchard. Was this castle once overtaken? \n  ~ South: You once heard screaming coming from that direction. You can see something glistening from a nearby tree that caught fire.',
                'envitem': 'lever',
                'engage': 'You notice a LEVER slightly hidden behind a pile of rocks. A demon\'s hand maintaining a death grip on it. It\'s separated at the wrist.\n     Type \' interact LEVER\' to interact with the environment',
                'interact': 'You take the hand off the lever and throw it to the ground with a heavy thud. You pull the lever and hear gears grinding in the distance.'
                },
        'Courtyard_Northwest': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Courtyard_Midwest',
                'desc': 'Just as you suspected. A dead orchard. You are surrounded by dead trees, symbolizing dead titans reaching down to grab you. \n  ~ South: Looks like more evidence a battle took place.  You don\'t notice any movement.',
                'invitem': 'apple',
                'item': 'You notice one shiny red APPLE hanging from a branch. A sign of life amidst all this death.  It\'s somehow...hopeful.'
                },
        'Courtyard_East': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Courtyard_Mideast',
                'west': 'Courtyard_Main',
                'desc': 'No signs of life here either. The vegetation looks ready to crumble to dust if you touch it. \n  ~ North: You see evidence of one of our previous attacks. Stone tumbling into the courtyard, proof of an outside attack. \n  ~ West: The main area of the courtyard. Feels more like the entrance to a nightmare.'
                },
        'Courtyard_Mideast': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Courtyard_East',
                'desc': 'Large stones poured into the courtyard. A failed attack from one of our previous raids. \n  ~ South: You see nothing but more dead foliage.',
                'eqitem': 'helmet',
                'gear': 'You see a perfectly good HELMET about your size. The head still inside.',
                'equip': 'You reach down and grab the helmet.\n   You match eyes with the previous owner and say the word \"Sorry.\" in an apologetic tone before shaking the head out and down to the floor.\nYou take a deep breath and put it on.'
                },
        'Castle_Entrance': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Courtyard_Main',
                'desc': 'You stand before a large door at least three times your height. There are spikes jutting out, some adorning human skulls. Intimidating? Yes.\n     You don\'t notice a way to open it from here. \n  ~ South: The main area of the courtyard. Feels more like the entrance to a nightmare.'
                },
       'Castle_Entrance2': {
                'inv': inventory,
                'inventory': inventory,
               'north': 'Corridor',
               'south': 'Courtyard_Main',
               'desc': 'You stand at the entrance to the castle. The opening to the main hall resembling a mouth ready to swallow you, never to see the light again.  \n  ~ North: The corridor th the castle\'s main hall lies before you.  \n  ~ South:  The main area of the courtyard. Feels more like the entrance to a nightmare.'
                },
        'Corridor': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Hall',
                'desc': 'The door slams behind you! There\'s no way to open it from here. The only way to go is forward. Great.  \n  ~ North: There is a hallway leading to the main hall of the castle.' 
                },
        'Hall': {
# Would like to trigger an "into" battle/tutorial. Need a "scene" triggering before and after fight.
        ## May need to use other description if that isn't doable. 
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Hall_South',
                'desc': 'You walk slowly into the hall, guard up. Again, you hear that cold laughter. You instinctly look behind you to notice the black flames again.\n     You get out of the range of the fire as a goblin jumps down from the ceiling behind you. Trying for a sneak attack!'
# After tut. >   'descafter': 'You weaken the goblin as it staggers backwards. One of the wicks of its explosives catch fire.\n      You need to get out before the explosives go off!  \n  ~ North: The castle\'s main hall is dead ahead!'
# 2nd scenario > 'desc2': 'You walk slowly into the hall, guard up. Again, you hear that cold laughter.  You instinctly look behind you to notice the black flames again.\n      It begin to creep forward, you know you need to get out of here before the flames surround you!  \n  ~ North: The castle\'s main hall is dead ahead!'
                },
        'Main_Hall_South': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Hall_Center',
                'east': 'Main_Hall_Southeast',
                'west': 'Main_Hall_Southwest',
                'desc': 'The hallway had collapsed from the explosion. Every move you seem to make, you find yourself further ensnared in some sort of trap.  \n  ~ North: The center of the main hall. You notice a dark but beautiful light in the distance.  \n  ~ West: A corner of the main hall.  Wait...is that a. ..hole there?  \n  ~ East: A corner of the main hall. You notice some furniture and candles flickering in the distance.'
# 2nd scenario > 'descalt': 'You make it out of the hallway as it fully engulfs in flames.  For some reason, it refulses to spread into the main hall.\n      You aren\'t sure why, but you know you\'re safe from the flames.\  \n  ~ North: The center of the main hall. You noticed a dark but beautiful light in the distance.  \n  ~ West: A corner of the main hall.  Wait...is that a. ..hole there?  \n  ~ East: A corner of the main hall. You notice some furniture and candles flickering in the distance.'
                },
        'Main_Hall_Southwest': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Hall_West',
                'east': 'Main_Hall_South',
                'down': 'Jailroom1',
                'desc': 'This corner of the main hall seems \'extra\' dark. You barely make out a hole that contains stairs leading down.  \n  ~ North: A pool of bood blood leading from the stairs to a door on the other end of the main hall.  \n  ~ East: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ Down: A set of stairs decending into an unknown horror. Nothing bad ever happens in a cellar, right?'
                },
        'Main_Hall_West': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Kitchen',
                'south': 'Main_Hall_Southwest',
                'east': 'Main_Hall_Center',
                'west': 'West_Wing',
                'desc': 'You stand in the western portion of the main hall.  \n  ~ North: There\'s a door with a pool of blood under it.  \n  ~ South: A corner of the main hall.  Wait...is that a. ..hole there?  \n  ~ West: There is a pathway leading to the western tower.  \n  ~ East: The center of the castle\'s main hall. You notice a dark but beautiful light in the distance.',
#                'desc2': 'The trail of blood is thicker here. Looks to be a small pool under the edge of the door.  \n  ~ North: There\'s a door with a pool of blood under it.  \n  ~ South: A corner of the main hall.  Wait...is that a. ..hole there?  \n  ~ West: There is a pathway leading to the western tower.  \n  ~ East: The center of the castle\'s main hall.',
                'invitem': 'flint',
                'item': 'You see a piece of FLINT rock under one of the torches by the door.'
                },
        'Kitchen': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Meat_Locker',
                'south': 'Main_Hall_West',
                'desc': 'You\'re in the castle\'s kitchen. Who would\'ve guessed that monsters cook their food?  \n  ~ North: There\'s a door. Maybe the castle\'s pantry?  \n  ~ South: A door back to the castle\'s main hall.',
                'invitem': 'fire',
                'item': 'You notice a scroll to learn the FIRE spell. Maybe they use it to cook with?'
# Scenario >     'scenario': Needs THIGH, FLINT + POISON = BAIT
                },
        'Meat_Locker': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Kitchen',
                'desc': 'You notice a bunch of people hanging from meat hooks, some of them have limbs hacked off.\n     You now understand why you were all led here.  \n  ~ South: Back to the Kitchen',
                'invitem': 'thigh',
                'item': 'You notice a person\'s THIGH in a bin. Probably set aside to be eaten. The thought of being food for these..things.. makes you sick.\n      You know there\'s no chance to give these people a proper burial, but this is one piece these bastards won\'t get.' 
                },
        'Main_Hall_Southeast': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Hall_East',
                'west': 'Main_Hall_South',
                'desc': 'There\'s a painting of the Dark Wizard on the wall. You feel like you\'re being watched.  \n  ~ North: The other end of the main hall. You can make out a door from here.   \n  ~ West: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.'
#                'invitem': 'map',
#                'item': 'There\'s a table under the painting. There\'s a MAP sitting on the table between two lit candlesticks.' 
                },
        'Main_Hall_East': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Barracks',
                'south': 'Main_Hall_Southeast',
                'east': 'East_Wing',
                'west': 'Main_Hall_Center',
                'desc': 'You\'re standing in the eastern portion of the main hall.  \n  ~ North: You see a door. You don\'t understand monster language, but you think you see a picture of a bed?  \n  ~ South: A corner of the main hall. You notice some furniture and candles flickering in the distance.  \n  ~ West: The center of the main hall. You notice a dark but beautiful light in the distance.  \n  ~ East: There is a pathway leading to the eastern tower.'
#                'desc2': 'You\'re standing in the eastern portion of the main hall.  \n  ~ North: You see a door. You don\'t understand monster language, but you think you see a picture of a bed?  \n  ~ South: A corner of the main hall. You notice some furniture and candles flickering in the distance.  \n  ~ West: The center of the main hall.  \n  ~ East: There is a pathway leading to the eastern tower.
                },
        'Barracks': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Armory',
                'south': 'Main_Hall_East',
                'desc': 'This must be the monster\'s barracks. \"They\'re more like us than I realized.\" You think to yourself.  \n  ~ North: You see a door with a picture of two swords crossed over a shield.  \n  ~ South: This way leads you back to the main hall.',
                'invitem': 'd.key',
                'item': 'You notice a key hanging on one of the beds. It has a picture of a jailcell etched into it. Maybe it\'s the dungeon key? You debate over taking the D.KEY with you.'
                },
        'Armory': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Barracks',
                'desc': 'You found the castle\'s armory! There are no weapons but plenty of armor. These do seem like the type of creatures to focus more on attack than defense...  \n  ~ South: This will take you back to the barracks.',
                'eqitem': 'boots',
                'gear': 'Your eyes glance all across the armory. So many different shapes and sizes! Your eyes catch a pair of BOOTS that are probably your size...',
                'equip': 'You throw on the armored boots. Nobody\'s stepping on your toes anymore!'
                },
        'Main_Hall_Center': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Hall_North',
                'south': 'Main_Hall_South',
                'east': 'Main_Hall_East',
                'west': 'Main_Hall_West',
                'desc': 'There\'s a wall of green and purple flames that prevent you from going towards the main tower.\n     You notice two pillars, one on each side of the wall, corresponding with the colors of the flames. It looks like you could place an ORB on the top of each one.  \n  ~ South: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ West: This way will lead you to the western part of the main hall.  \n  ~ East: This way will lead you to the eastern part of the main hall.'
#  Green ORB     'descA': 'The GREEN ORB sits atop its rightful place.\n    There\'s a wall of purple flames that prevent you from going towards the main tower, meaning only the PURPLE ORB remains.  \n  ~ South: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ West: This way will lead you to the western part of the main hall.  \n  ~ East: This way will lead you to the eastern part of the main hall.'
#  Purple ORB    'descB': 'The PURPLE ORB sits atop its rightful place.\n    There\'s a wall of green flames that prevent you from going towards the main tower, meaning only the GREEN ORB remains.  \n  ~ South: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ West: This way will lead you to the western part of the main hall.  \n  ~ East: This way will lead you to the eastern part of the main hall.'
#  BOTH          'desc2': 'Both ORBS sit atop their respective pillars. witht he flames gone, you are now able to make it up the main tower and take on the Dark Wizard.  \n  ~ North: This leads you to the bottom of the main tower.  \n  ~ South: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ West: This way will lead you to the western part of the main hall.  \n  ~ East: This way will lead you to the eastern part of the main hall.'                
                },
        'Main_Hall_North': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Belmont',
                'south': 'Main_Hall_Center',
                'up': 'Main_Tower1',
                'desc': 'You made it. You\'re at the base of the main tower. The Dark Wizard must be somewhere up top.\n     You notice the state of the room and realize that you must have missed one hell of a fight before the flame wall was cast.\n   There\'s monster parts, fallen brothers in arms, bomb residue, broken gear, eviscerated flesh, teeth... Memories you won\'t soon forget.\n     You notice claw marks and sword slashes on the walls. The northern wall is has a huge crack in it.  \n  ~ South: This will put you back into the main hall.  \n  ~ Up: Begin ascending the spiral staircase of the final tower!'
#   Somehow see if its possible to USE the OLDWHIP in room and have a script to "open" the wall to get in                
                },
        'Belmont': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Main_Hall_North',
                'desc': 'What is a man?! A miserable little pile of secrets! But enough talk! Have at you!\n     You notice a lone treasure chest in this hidden room. You kick it open as hard as you can and spilled whatever contents it contained onto the cold, stone floor.   \n  ~ South: With your new super secret items and skills, you\'re ready to get up that tower!',
                'invitem': 'p.chop',
# Other items   'invitemAB': 'btears', 'rope',
                'item': 'Who cooks a pork chop and hides it in a wall?!\n     Before you can even begin to ponder the answer, you notice a ROPE and the BELMONT scroll with the words \"Bloody Tears\" inscribed on the top.\n   You look over this weird haul of a P.CHOP, ROPE and BELMONT scroll, debating on whether or not to take them.\n     I mean, really? Who\'s idea was it to put a pork chop in a wall?'
# Grabbed PCHOP  'itemA': 'You grabbed the pork chop! You put health above power. Nothing wrong with power though... Don\'t forget the BELMONT scroll and your ROPE!'
# Got BTEARS     'itemB': 'You grabbed the scroll first! You must lust for power.  But wall food may come in handy too! Don\'t forget to take the PCHOP! and your ROPE'
# Got ROPE       'itemC': 'You took the rope. Saving the best for last? What\'s next? the BELMONT scroll or the PCHOP?'
# Got P+B        'itemD': 'All that remains to take is the ROPE.'
# Got P+R        'itemE': 'All that remains to take is the BELMONT scroll.'
# Got B+P        'itemF': 'All that remains to take is the ROPE.'
# Got B+R        'itemG': 'All that remains to take is the PCHOP.'  
# Got R+P        'itemH': 'All that remains to take is the BELMONT scroll.'  
# Got R+B        'itemI': 'All that remains to take is the PCHOP.'  
                },
        'West_Wing': {
                'inv': inventory,
                'inventory': inventory,
                'east': 'Main_Hall_West',
                'up': 'West1_Main',
                'desc': 'You\'re standing at the base of the western tower.  \n  ~ East: This direction will lead you back into the main hall.  \n  ~ Up: A set of stairs leading up into the west tower.'
                },
        'East_Wing': {
                'inv': inventory,
                'inventory': inventory,
                'west': 'Main_Hall_East',
                'up': 'East1_Main',
                'desc': 'You\'re standing at the base of the eastern tower.  \n  ~ West: This direction will lead you back into the main hall.  \n  ~ Up: A set of stairs leading up into the east tower.'
                },
        'Jailroom1': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Jailroom2',
                'up': 'Main_Hall_Southwest',
                'desc': 'You\'re standing in the entrance to the castle\'s dungeon. Who would have guessed that they actually keep prisoners?\n     There is a door to the \'North\' that requires a key to enter.  \n  ~ Up: A set of stairs leading back up into the main hall.'
#                 'desc2': 'desc': 'You\'re standing in the enterance to the castle\'s dungeon. Who would have guessed that they actually keep prisoners?  \n  ~ North: A door that leads you further into the dungeon.  \n  ~ Up: A set of stairs leading back up into the main hall.'
## north needs DKEY
                },
        'Jailroom2': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Jailroom3',
                'south': 'Jailroom1',
                'desc': 'You arrive in a wide open room resembling a small colosseum. The Guardian Beast lies sleeping. A pile of bones lay before it. Some meat chunks still attached.\n     You don\'t believe it heard you enter, but you swear you\'d seen it\'s ear twitch.  \n  ~ North: head further into the dungeon.  \n  ~ South: Head back towards the stairs.'
#                'desc2': 'You arrive in a wide open room resembling a small colosseum. The beasts corpse lies dead from poison. You swear you saw it move, but it must have just been your nerves.'
#                'desc3': 'You arrive in a wide open room resembling a small colosseum. The beast is back on it\'s feet?! The poison didn't seem to have the deired effect on it after all. It stands between you and the exit, but luckilly it does appear to be weakened. You have no choice but to fight!'
#                'desc4': 'You arrive in a wide open room resembling a small colosseum. The Gurdian Beast's corpse lies in a pile near the center of the room.\n    Proof of a hard faught victory.'
#                'interact' 'The beast awakens, smelling the cooked thigh. It charges at you, excited for its treat.  Before it gets to close you throw th BAIT at the creature.  It swallows it without even chewing.  THe poison takes affect almost instantly.  The beast dry heaves and you can see it struggles to breathe. In mere moments its body becomes upright and stiff before falling onto its side like a broom falling to the floor.' 
                },
        'Jailroom3': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Jailroom4',
                'south': 'Jailroom2',
                'east': 'Jailcell2',
                'west': 'Jailcell1',
                'desc': 'You\'re in the middle of a cross-way. There\'s two jail cells here and another door which leads you further in.  \n  ~ North: A door similar to the others. It must lead further into the dungeon.  \n  ~ South: It will lead you back to the room where the beast was dwelling.  \n  ~ West: There\'s a jail cell here.  \n  ~ East: There\'s a jail cell here.'
                },
        'Jailcell1': {
                'inv': inventory,
                'inventory': inventory,
                'east': 'Jailroom3',
                'desc': 'A small jail cell. Not even enough room for a normal sized person to lay down.  \n  ~ East: Leads you back to the dungeons cross-way.',
                'invitem': 'lockpick',
                'item': 'You notice a LOCKPICK on the ground near the entrance. You wonder if this person had escaped, or if that pile of bones by the beast belonged to them.'
                },
        'Jailcell2': {
                'inv': inventory,
                'inventory': inventory,
                'west': 'Jailroom3',
                'desc': 'A small jail cell. Not even enough room for a normal sized person to lay down.  \n  ~ West: Leads you back to the dungeons cross-way.',
                'invitem': 'lastmeal',
                'item': 'You see a tray lying on the floor with something that barely resembles food for human consumption.\n    Looks as though the person was forcefully dragged out.  Must of been thier LASTMEAL...'
                },
        'Jailroom4': {
# Need to use lockpick to go north. make it so it unlocks the door but breaks after being used.              
                'inv': inventory,
                'inventory': inventory,
                'north': 'Jailroom5',
                'south': 'Jailroom3',
                'desc': 'This looks like an office of some sort. You hear moaning coming from the room to the north. Sounds like someone\'s hurt.\n     The door appears to be locked.',
# Scripted fight 'desc': 'This looks like an office of some sort. You hear moaning coming from the room to the north. Sounds like someone\'s hurt.\n     You approach the door slowly, not knowing what awaits you on the other side.\n  Just as you begin your approach towards the door, a pig-like creature emerges from it. It notices you and gives off an inhuman shriek all the while matching your gaze.\n    It quickly locks the door it emerged from and throws the key into a gutter that you believe is supposed to be a latrine.\n  It gives of a noise that sounds like a confident laugh. It unravels a whip and prepares to give you a proper greeting.'
# After fight    'desc2': 'The warden gives a death squeal so ear piercingly high, you check to make sure your ears aren\'t bleeding. It drops the OLDWHIP before dropping to the ground.  \n  ~ North: That\'s the door the warden came out from! The air feels colder the closer you are to it.  \n  ~ South: Takes you back to the dungeons crossway.'
# Using lockpick 'desc3': 'You decide to try the LOCKPICK you found to open the door. You aren\t the most experieneced when it comes to this.  After much trial an error, you finally get it! Unfortunately you broke the LOCKPICK in the process!'
# Nrml room fite 'desc4': 'You\'re in the office belong to the warden of the castle\'s dungeon. That pig bastard lying dead on the floor. You picture somehow finding a way to stuff his corpse into the latrine to be witht he rest of his kind.  A dry grin washes across your face.  \n  ~ North: That\'s the door the warden came out from! The air feels colder the closer you are to it.  \n  ~ South: Takes you back to the dungeons crossway.'
# Nrml room -fite'desc5': 'You\'re in what appears to be an office like space. Is someone in charge of this dungeon? The room is pretty well lit compared to the other rooms.  \n  ~ There is an arched wooden door. While picking the lock, you noticed the air coming from it was significantly colder.  \n  ~ South: Takes you back to the dungeons crossway.'
                'invitem': 'oldwhip',
                'item': 'The warden\'s favorite weapon, an OLDWHIP lays next to its corpse. It looks very beat up. It must of used it a lot in it\'s lifetime.'
# If can't fite  'item2': 'There is an OLDWHIP hanging on the wall. It looks incredibly worn. Must have been used a lot. Something tells you you shoudl take it.'                
                },
        'Jailroom5': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Jailroom4',
                'desc': 'The room is freezing. Through your breath, you see a knight chained up -no. HANGING on the wall. He\'s still alive!\n     He\'s missing both of his legs and one of his arms from the elbow down. His body has a light blue hue. You hear gentle sobbing.\n   You don\'t believe he even notices you\'re there.\n     \"How long has he been here?\" you wonder. He\'s not from your battalion. You walk closer, not knowing what to say, or how to react.\n   The gentle sobbing you hear slowly turns into words you can start making out: \"Kill me...Kill..me..\" he says.\n     \"What?!\" "Kill Me!!Kill Me Kill MeKillMeKillMeKillMeKIlLMEkIlLMeKILLMEKILLMEKILLMEKI-\"\n   You grant his wish. Slowly pulling your sword out of this chest, you try to come up with a means of justifying you actions.\n     If he hadn\'t shut up, he may have brought attention down here. You would of been trapped, possibly having the same fate as him.\n   You keep telling youself it was the right thing to do...It was the right thing to do...It was the right thing to do...',
# after 1st desc/"cutscene"                'desc2': 'You look af the poor bastard hanging there and pay your respects.  \n  ~ South: The beginning of the way out of the dungeon. You don\'t like being in this room longer than necessary.'
                'invitem': 'blizzard',
                'item': 'You see a spell scroll. The scroll reads BLIZZARD on it. Must have been used to keep the room so cold.',
                'eqitem': 'breastplate',
                'gear': 'The poor bastards armor lies in a pile in the corner. It\'s all cracked and dented. No longer fit for use.\n     But wait! you notice the BREASTPLATE is relatively untouched. It\'s freezing, but will warm up with your body heat.',
                'equip': 'You throw on the breastplate. it\'s cold enough to hurt your skin a little. You look forward to getting out of this room to warm it up.'
# scroll first   'item2': 'The poor bastards armor lies in a pile in the corner. It\'s all dented or cracked. No longer fit for use.\n     But wait! you notice the BREASTPLATE is relatively untouched. It is freezing, but will warm up with you body heat.'
# Armor first    'item3': 'There\'s a BLIZZARD scroll lying by the remaning pieces of the poor bastards busted armor.'
                },
        'West1_Main': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'West1_North',
                'south': 'West1_South',
                'east': 'West1_East',
                'west': 'West1_West',
                'up': 'West2_Main',
                'down': 'West_Wing',
                'desc': 'After using the stairs, you\'re standing in the main room of the western tower. \n   Maybe you\'ll get lucky and catch the Dark Wizard off-guard.  \n  ~ North: There is a door lying on the floor. It was kicked open. There is a room wide open. You can see a body in there wearing your kingdom\'s colors.  \n  ~ South: There is a walkway that looks to lead outside.  \n  ~ West: There is a doorway.  \n  ~ East: There is a doorway. There is a dead monster neraby. Possibly a guard?  \n  ~ Up: There\'s a set of stairs leading further up the tower.  \n  ~ Down: There\'s a set of stairs leading back down to the main floor of the castle.'
                },
        'West1_North': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'West1_Main',
                'desc': 'There is a knight impaled into the wall with a spear. The power behind that thrust must\'ve been incredible.  \n  ~ South: Go back into the main room.',
                'eqitem': 'gloves',
                'gear': 'The knight is grasping tightly to the spear. Was he trying to pull the spear out, or pull himself all the way through? \n  You\'ll never know. The GLOVES look about your size though...',
                'equip': 'You take the knight\'s gloves. They\'re still warm on the inside. A small shiver rolls down your spine.'
                },
        'West1_South': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'West1_Main',
                'desc': 'You step out to the balcony and take in the sights. You feel heat on your face and the smell of iron is thick in the air. It\'s a depressingly mmelancholyview.  \n  ~ North: Go back into the main room.'
                },
        'West1_East': {
                'inv': inventory,
                'inventory': inventory,
                'west': 'West1_Main',
                'desc': 'You walk into the room, stepping over the guard in the process. You\'re standing in a bedchamber. It looks exquite.\n  More than a typical soldier would sleep in. Is this the bedchamber of the Dark Mage?  \n  ~ West: Go back into the main room.'
                },
        'West1_West': {
                'inv': inventory,
                'inventory': inventory,
                'east': 'West1_Main',
                'desc': 'A room full of potions and vials. Alchemy was performed here.  \n  ~ East: Go back to the main room',
                'invitem': 'poison',
                'item': 'You take note of...well a note. It reads:\n     \"That damn guardian beast! It\'s too damn picky! It won\'t even eat its meat raw.\n   It\'s below me to be in charge of taking care of such a lowley creature! I\'ll take care of it once and for all!!\"\n   A vial of POISON sits closeby the note. It\'s been knocked over, but is still intact and sealed tightly.'
                },
        'West2_Main': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'West2_Treasure',
                'down': 'West1_Main',
                'desc': 'You\'re standing in the entryway at the top of the tower. You peek out the window. It\'s a long way down from here.  \n  ~ North: There is a door before you. It leads further into the upper floor.  \n  ~ Down: A set of stairs leading back down the tower, towards the main area of the castle itself.'
                },
        'West2_Treasure': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'West2_Main',
                'desc': 'A treasure room sits atop the western tower. There\'s everything from gold to magic armor. Spells you can\'t even begin to read, weapons too heavy to wield.\n     You are more impressed to find something in this castle that actually shines to counteract the encompassing bleakness.  \n  ~ South: The main room of the top floor.',
                'invitem': 'p.orb',
                'item': 'You see a purple orb siting atop a pillar. Its light is both blinding and welcoming. Terrifying, yet comforting.\n     The P.ORB shines brightly, yet somehow the light barely stretches for more than a meter.\n   However, there seems to be a thread of light that seems to point in the direction on the castle, as if telling you where it wants to go.'
# Trigger after get P.ORB 'desc2': 'The room begins to dim whiel the treasures surronding you begin to shake. The armor you couldn\'t weild begin to come together to form some type of man-creature hybrid put to gether with an amalgam of different body parts. \"TRESSPASSER!\" You think it loudly in your head rather than hear it. With barely a moment to react, it lunges towards you!'
# The armor begins to shave violently, as though trapped with in a tremor only it can feel. You can see the air around it begin to waver as it lets out a noise like a snake taking a deep sigh. Vapor exiting from every orifice you donated to the armored shell. It stops for only a moment and crashes to the ground.  You know you won.'
                },
        'East1_Main': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'East1_North',
                'south': 'East1_South',
                'west': 'East1_West',
                'up': 'East2_Main',
                'down': 'East_Wing',
                'desc': 'You\'re standing in the main room of the east tower. There\'s multiple rooms around you.  \n  ~ North: There is a door. You see light bleeding out from beneath.  \n  ~ South: There is a walkway that looks to lead outside.  \n  ~ West: You see a door. A small trail of blood leads your eye to it.   \n  ~ Up: Stairs leading to the upper area of the east tower.  \n  ~ Down: There\'s a set of stairs leading back down to the main floor of the castle.'
                },
        'East1_North': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'East1_Main',
                'desc': 'It\'s a room containing a multitude of shimmering stones! It\'s nigh impossible to discern their purpose.  \n  ~ South: Go back to the main room.',
                'invitem': 'crystal',
                'item': 'As your eyes wander, you feel as if one is talking to you. You\'re eyes strain to locate the mysterious voice.\n    You fixate on a single CRYSTAL. It looks no different from the others.\n          "Kees uoy tahw uoy teg lliw I dna rorrim eht ot em ekat...", It whispers seductively.'
                },
        'East1_South': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'East1_Main',
                'desc': 'You step out to the balcony and take in the sights. You feel heat on your face and the smell of iron is thick in the air. It\'s a drepressingly meloncholy view.  \n  ~ North: Go back into the main room.'
                },
        'East1_West': {
                'inv': inventory,
                'inventory': inventory,
                'east': 'East1_Main',
                'desc': 'You open the door to a room no bigger than a closet. The trail of blood outside leading to a soldier who leaves you baffled.\n    He sits there, lifeless. Likely dragged himself in here to to barricade himself until help arrived.\n  There is no sign of poisoning ar any type of spell. From the looks of him, his apparent death was caused by an arrow to the knee.  \n  ~ East: Go back to the main room',
                'eqitem': 'leggings',
                'gear': 'More baffling still, next to the man sits a pair of perfectly good LEGGINGS. Seemingly untouched from the man\'s injuries.\n    You\'re confused, but hope fortunes continue to slime upon you for a while longer.',
                'equip': 'These leggings might not have given it\'s previous owner any luck, but hopefully they will for you.'
                },
        'East2_Main': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'East2_Duality',
                'down': 'East1_Main',
                'desc': 'You stand atop the east tower hall. The air is thick with magic.\n     You taste a slight sweetness in the air accompanied with a minuet burning on your tongue with every breath.  \n  ~ North: There is a door. It seems like a seal. Doing its best to prevent whatever magic is inside from leaking out.  \n  ~ Down: A set of stairs leading back down the tower, towards the main area of the castle itself.'
                },
        'East2_Duality': {
# Need script to use CRYSTAL and open Northern path
                'inv': inventory,
                'inventory': inventory,
                'north': 'East2_Treasure',
                'south': 'East2_Main',
                'desc': 'It\'s a reflective room. Shimmering crstals all around you. As you look around the room, you see no less than 20 you staring in every which direction.\n     The wall at the \'North\' end of the room is distinct from the others. It is one giant mirror, and it\'s reflection give off a darker tint than the rest.  \n  ~ South: It\'s the main hall of the top of the eastern tower.'
#                'desc': 'It\'s a refective room. Shimmering crstals all around you.\n    As you look around the room, you see no less than 20 yous staring in every which direction.\n  The wall at the \'North\' end of the room is distinct from the others. It is one giant mirror, and it\'s reflection give off a darker tint than the rest.  \n  ~ North: You touch the north wall. It is now more liquid than solid. You can likely pass through.  \n  ~ South: It\'s the main hall of the top of the eastern tower.'
#                'event': You hold the CRYSTAL against the northern wall. The reflections seemingly merging into one. The CRYSTAL sinks into the wall as it begins to waver. You poke the wall in confusion, leaving a rippling effect that spreads to all reaches of the wall.'
                },
        'East2_Treasure': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'East2_Duality',
                'desc': 'You jump into the mirror. The taste of magic here is exponentially stronger. You taste icing with every inhale and feel as though you breathe fire with every exhale.  \n  ~ South: Head back out of the reflection, back into the real world.',
#                'event': Another mirror wall is adjacent to your position. You see a similar off color reflection of you. Somehow it gives off the impression that it\'s walking towards you.\n    Wait! It IS walking towards you!\n  It\'s eyes staringy ou down, One a dark red, the other illuminating a dark green light, it unsheathes it\'s sword and beckons you to prepare to fight.'
#                'event2': It sounds as though it screams in reverse. It falls to the ground. Defeated.\n    As it\'s head hits the ground, it\'s green eye pops out and rolls across the floor towards you. You look down and notice the thing rolling before you is much to big to be an eye. It looks like an orb!\n  You take one last look back at the immitation, but it is already gone. Back in the walls, mimicing your every move. Back where it belongs.'
                'invitem': 'g.orb',
                'item': 'The green orb lies at you feet. Was the G.ORB using that manifestation to test you? If so, you\'ve more than proven your worth.'
                },
        'Main_Tower1': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Main_Tower2',
                'down': 'Main_Hall_North',
                'desc': 'You stand at the base of the spiral staircase. You sense the end of your journey is at hand. You see trails of blood flowing down like a river, creating a small lake of anguish beneath your feet  \n  ~ South: You will begin to ascend stairs.  \n  ~ Down: This will take you back to the main area of the castle. In case you want to look around once more.'
                 },
        'Main_Tower2': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Tower1',
                'east': 'Main_Tower3',
                'desc': 'The bottom of the steps. There\'s nothing strange here beyond the normal horrors of this wretched place.  \n  ~ North: You will return to the base of the tower.  \n  ~ East: You will continue your journey upward.'
                },
        'Main_Tower3': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Tower4',
                'west': 'Main_Tower2',
                'desc': 'Just stairs, stairs, and more stairs.  \n  ~ North: Keep moving up!  \n  ~ West: Go back!'
                },
        'Main_Tower4': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Tower5',
                'south': 'Main_Tower3',
                'desc': 'At least in this part of the tower, there\'s a window for a slight change of scenery. A lifeless monster hangs off the side.  \n  ~ North: Keep Going!  \n  ~ South: Turn Back!'
                },
        'Main_Tower5': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Main_Tower4',
                'west': 'Main_Tower6',
                'desc': 'You swear, if the Dark Wizard doesn\'t kill you, these stairs will.  \n  ~ South: I can\'t go any higher, my legs are killing me!  \n  ~ West: No! They have to end sometime! I have to keep going!'
                },
        'Main_Tower6': {
                'inv': inventory,
                'inventory': inventory,
                'east': 'Main_Tower5',
                'west': 'Main_Tower7',
                'desc': 'You see the top! You almost made it! Just a few more steps!  \n  ~ West: The top of the stairs!  \n  ~ East: Going down?'
                },
        'Main_Tower7': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Library',
                'south': 'Main_Tower8',
                'east': 'Main_Tower6',
                'desc': 'You stand at the top of the staircase. You look down for a moment to admire your accomplishment.  \n  ~ North: A door with two torches on each side. They look freshly lit. You see a flicker of light from under the door.  \n  ~ South: Your eyes follow the pattern of a carpet as it slowly changes from an orange and greenish hue to a deep crimson. A fight happened here.  \n  ~ East: You\'ll go back down the stairs'
                },
        'Library': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Main_Tower7',
                'desc': 'This room is a library! A vast contrast from any other room in this castle! It looks like one you would find in the castle back home.\n     There are books strewn everywhere. Ripped, burned, some even look half eaten. Even a place of scholars isn\'t during a fight.  \n  ~ South: You will return to the top of the stairs.',
                'invitem': 'scroll',
                'item': 'You come across another corpse of a fallen comrade. He is clutching a SCROLL and a parchment. The parchment reads:\n     "Read the incantation on the SCROLL aloud in the Dark Wizard\'s presence to weaken him."\n   The note appears to be written in his own blood.'
                },
        'Main_Tower8': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Tower7',
                'south': 'Main_Tower9',
                'desc': 'As you walk on the carpet, you here a squishing sound. The rug is not meant to be crimson. It had beed bathed in blood.  \n  ~ North: Go back to the top of the stairs  \n  ~ South: Continue to the end of the hall.'
                },
        'Main_Tower9': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Tower8',
                'up': 'Main_Tower_F2R1',
                'desc': 'You come to the end of the hall only to face the most abhorrent foe of all: more stairs.  \n  ~ North: You decide to turn back.  \n  ~ Up: Curse these damnable things. There\'s no point in complaining. This way leads you closer to the Dark Wizard.'
                },
        'Main_Tower_F2R1': {
                'inv': inventory,
                'inventory': inventory,
                'east': 'Main_Tower_F2R2',
                'down': 'Main_Tower9',
                'desc': 'You are in a rather nice hall. Opposite of everything below.  \n  ~ East: Looking down the corridor, you see a rather large room. From here it looks to keep a similar aesthetic to this room.  \n  ~ Down: You can hean back down to the previous floor.'
                },
        'Main_Tower_F2R2': {
# Event after desc leading to fight
#                'event': '\"What?! How could I lose?!\" He shouts at you in angry bewilderment. He takes a moment to compose himselt.\n    \"Ah yes. I see...Now I see why you made it this far.  There\'s a fire in you I haven\'t seen in the others.\n  But you know... I have a fire too. LET\'S SEE WHOSE BURNS BRIGHTEST!!\"\n    His body engulfs in flames as he begins cackling meniaclly. His body begins expanding and he looks like he\'s about to explode.\n   Wait...!  Explode! The son of a bitch is going to try to take you both out!\n    You grab the thickest table you can and drag it to the furthest corner of the room. You kick it on its side and hide behind it.\n  You hear a thunderous BOOM! Flames erupt onto the ceiling and begin spreading. You make a judgement call and get up behind the table.\n Hes gone... but there\'s also a pit across the floor and it\'s too wide to jump over.\n       You see a rafter still in tact up in the ceiling. If only you had something to use to swing across...'
# USE whip       'event': You take out the old whip and immediately use it to try and gain a proper hold of the rafter above.\n Luckilly you get it on the first try! You hurry to swing across before it catches fire, praying it can hold your weight.\n    It rips just as you cross the hole\'s threshold. You\'re safe, well, safe-ish. But there\'s no going back now.  \n  ~ East: There\'s only one way left to go.'
# use rope       'event': You take out the rope and immediately use it to try and gain a proper hold of the rafter above.\n Luckilly you get it on the first try! You hurry to swing across before it catches fire, praying it can hold your weight.\n    It rips just as you cross the hole\'s threshold. You\'re safe, well, safe-ish. But there\'s no going back now.  \n  ~ East: There\'s only one way left to go.'
                'inv': inventory,
                'inventory': inventory,
                'east': 'Main_Tower_F2R3',
                'desc': 'You arrive in a gigantic room. Much bigger than you expected. Before you get a chance to admire the scenery, A dark figure emerges from the shadows.\n     It\'s the Dark Wizard\'s most powerful lackey...the Dark Mage!\n   \"Oh? Another one? How many more of you rats are scurrying about? No matter.\n     You did well to make it this far. I do commend you, but you will go no further.\"\n   He crouches down slightly, both hands by his sides. Palms up. It looks as though he\'s holding shadows in the palms of his hands.\n     You unsheathe your sword, take a big gulp, and rush forward. Theres no point playing defensive against an opponent like this!'
                },
        'Main_Tower_F2R3': {
                'inv': inventory,
                'inventory': inventory,
                'up': 'Main_Tower_Final1',
                'desc': 'After everything you\'ve been through. Of course there had to be more stairs...  \n  ~ Up: The Dark Wizard must be close!'
                },
        'Main_Tower_Final1': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Tower_Final2',
                'down': 'Main_Tower_F2R2',
                'desc': 'The Dark Wizard is close by. You feel that same chill from back when you first stepped foot on the drawbridge.\n    You\'re too nervous to notice your surroundings now.  \n  ~ North: He\'s here. You can feel it.'
                },
        'Main_Tower_Final2': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Tower_Final3',
                'desc': 'The Dark Wizard is here. He turns around. He\'s looking more in your general direction then at you.\n     Up close, he just looks like a floating robe with to small white flames for eyes. He doesn\'t speak. Maybe he can\'t speak...?\n   The left side of his robe flutters for a brief moment, and once again the room is surrounded by black fire. He begins making that cold laugh again.\n     He floats up and out the balcony. Flying in the direction of the kingdom. His army will feast tonight. and you will burn.'
#                'desc': 'The Dark Wizard is here. He turns around. He\'s looking more in your general direction then at you. Up close, he just looks like a floating robe with to small white flames for eyes. He doesn\'t speak. Maybe he can\'t speak...? The left side of his robe flutters for a brief moment, and once again the room is surrounded by black fire. He begins making that cold laugh again. He beginst to float towards the balcony, but amidst your panic, a moment of clarity arrives. The scroll!! You take in out and unravel it as fast as you can and shout at the top of your lungs \"KLAATU VERATA NIKTO!!!\" The Dark Wizard stops hovering and falls to the ground in pain. Arms and legs manifest from the robe, but barely. You can still see through them, but it looks as thought he has a physical form. You only have one shot at this. you better make it count. This is it. The final battle. Give it your all!!!'
#                'desc2': 'You won! The Dark Wizard is vanquished as the world around you is devoured flames. Theres only one area of the room that has yet to be ravaged by fire.  \n  ~ North: Your only option.'
                },
        'Main_Tower_Final3': {
                'desc': 'Ths is the Dark Wizard\'s chambers. You can only focus on the bed. Thre is no way out. Nowhere to go. You\'re so tired.\n     You fought the Dark Wizard and won. Nobody will know what you did. No bards will sing songs of your legendary feats.\n   You are just a man. A man that overcame adversity to protect all he holds dear. You don\'t care. You just want to sleep.\n     You earned that much at least. You fall face first onto the bed and close your eyes. It was the best sleep of your entire life.'
                }
        }

# Players Starting Point
CurrentRoom = 'Tent'

# Displays only during first run
ShowInstructions()

# The forever loop
while True:
    
    ShowStatus()
    
    # This gets player's next move.
    # .split() breaks it up into a list array.
    # EX: Typing 'move east' would give the list ['move','east'].
    move = ''
    while move == '':
        move = input('> ')
    
    # .split allows items to have a space on them.
    # EX: 'get key' is returned ['get', 'key']
    move = move.lower().split(" ", 1)
    
    # If player types 'go' first
    if move[0].lower() == 'go':
        # Check to see if player is allowed to go wherever they want
        if move[1] in rooms[CurrentRoom]:
            # Sets current room to the new room
            CurrentRoom = rooms[CurrentRoom][move[1]]
        # Displays if no exit (link) in a direction
        else:
            print('Amidst your panic and exhaustion, you were lost for a moment. Please input a valid move.')
    
    # If player types 'get' first
    if move[0].lower() == 'get':
        # If the room contains an item, and they want to add it to their inventory
        if 'invitem' in rooms[CurrentRoom] and move[1] in rooms[CurrentRoom]['invitem']:
            # Add item to player's inventory
            inventory += [move[1]]
            # Display a confirmation message
            print('You added ' + move[1] + ' to your inventory!')
            # Removes item from the room itself
            del rooms[CurrentRoom]['invitem']
        # If there is no item to get
        else:
            print('Your mind must be playing tricks on you. There\'s no ' + move[1] + ' there!')

    # If player types 'interact' first
    if move[0].lower() == 'interact':
        # If the room contains an interactive element
        if 'envitem' in rooms[CurrentRoom] and move[1] in rooms[CurrentRoom]['envitem']:
            # Display a confirmation message
            print(rooms[CurrentRoom]['interact'])
            # Removes element from the room itself
            del rooms[CurrentRoom]['envitem']
        # If there is no item to interact with
        else:
            print('There\'s no ' + move[1] + ' to interact with!')

    # If player types 'equip' first
    if move[0].lower() == 'equip':
        # If the room contains any armor/weapons, and they want to equip it
        if 'eqitem' in rooms[CurrentRoom] and move[1] in rooms[CurrentRoom]['eqitem']:
            # Add item to player's inventory
            equipment += [move[1]]
            # Display a confirmation message
            print(rooms[CurrentRoom]['equip'])
            # Removes item from the room itself
            del rooms[CurrentRoom]['eqitem']
        # If there is no item to get
        else:
            print('Your mind must be playing tricks on you. There\'s no ' + move[1] + ' there!')

    # If player types 'inv' or 'inventory'
    if move[0].lower() == 'inventory' or 'inv':
        if 'inv' or 'inventory' in rooms[CurrentRoom]:
            print(inventory)

    ## later
    # If player types 'status'
    #if move[0].lower() == 'status':

    # If player types 'quit' or 'q'
#    if move[0].lower() == 'quit' or 'q':
#        print('Are you sure you want to exit (y/n)?:')
#        quit_query = input('> ')
#        if quit_query.lower() == "yes" or "y":
#            sys.exit(0)
#        elif quit_query.lower() == "no" or "n":
#            print('Good luck!')
#        else:
#            print('What do you mean by that?')

    if not "envitem" in rooms['Courtyard_Midwest'].keys():
        rooms["Courtyard_Main"]["north"] = "Castle_Entrance2"



