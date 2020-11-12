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
                                             ╔═════════╗                                                            ╔════════════════╗ 
                                             ║ ACTIONS ║                                                            ║ HELPFUL HINTS! ║
                                             ╚═════════╝                                                            ╚════════════════╝
                                                                    (Just kidding!)
  ╔══════════════════════════════════════════╗         ╔════════════════════════════════════════╗    ~ Type 'menu' at anytime while in the map to bring
  ║             MAP ACTIONS                  ║         ║             BATTLE ACTIONS             ║       up the list of map actions!
  ╠══════════════════════════════════════════╣         ╠════════════════════════════════════════╣ 
  ║ GO [ EX: "GO <DIRECTION>" ]              ║         ║ ATTACK                                 ║    ~ Careful! Items are scarce! If you don't think you're
  ╠══════════════════════════════════════════╣         ║  - Your basic action. No AP required.  ║       strong enough...GRIND! (Just kidding!)
  ║ GET [ EX: "GET <ITEM>" ]                 ║         ╠════════════════════════════════════════╣
  ╠══════════════════════════════════════════╣         ║ SKILL [ EX: "SKILL <NAME>" ]           ║    ~ Your only means of healing is your 'First Aid'
  ║ USE [ EX: "USE <ITEM>" ]                 ║         ║  - Use any skills you may know.        ║        ability which you learned during training. (Just kidding!)         
  ╠══════════════════════════════════════════╣         ║    * Some skills are learned through   ║
  ║ EQUIP [ EX: "EQUIP <ITEM>" ]             ║         ║      reading scrolls!                  ║    ~ Some items provide AP, while a few others give
  ╠══════════════════════════════════════════╣         ╠════════════════════════════════════════╣       a stat boost. (Just kidding!)      
  ║ INVENTORY / INV                          ║         ║ ITEM  [ EX: "ITEM <NAME>" ]            ║ 
  ╠══════════════════════════════════════════╣         ║  - Use an item you may have            ║    ~ All skills require AP. Even HEALING! Prioritize
  ║ STATUS                                   ║         ╠════════════════════════════════════════╣       so you can conserve enough AP to stay alive! (Just kidding!)
  ╠══════════════════════════════════════════╣         ║ RUN                                    ║
  ║ INTERACT/INT [ EX: "INT <SPEC ACTION>" ] ║         ║  - Escape the battle. May not succeed. ║    
  ╠══════════════════════════════════════════╣         ╚════════════════════════════════════════╝     
  ║ QUIT / Q                                 ║                          SUMMARY
  ╚══════════════════════════════════════════╝                         ---------
                                                                War. War never changes.
                                                                                                                                              
                            After a long march north you awaken in your tent after your battalion hd set up camp for the night.
                                You're near the base of the Dark Wizard's castle. Your raid on the castle is about to begin! 
                        
                         Quick note: Words marked in CAPITAL letters usually involve some interaction. It may be an item, equipment,
                                    or environmental interaction. Take note of the bullet to determine the proper action!''')

def ShowStatus():
    # Displays the player's current location
    print('\n╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗')
    print(' ● ' + rooms[CurrentRoom]['desc'])
    # Also display any items in the room, including separation lines
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
                'desc': 'There is a pile of old blankets infused with your sweat and blood. There is some light shining into the tent through the opening. \n  ~ North: Exit the tent.',
                'invitem': 'breakfast',
                'item': 'You notice your BREAKFAST lying on the ground next to the sheets. It\'s probably a good idea to eat it now.\n     [PLAYER TIP: Areas marked with a \'‣\' indicate an item. Type \"GET BREAKFAST\" to grab your breakfast!\n   You can check if you have your breakfast by typing \"INVENTORY\" or \"INV\".\n     You can eat your breakfast by typing in \"USE BREAKFAST\". Some items can only be used in specific areas!]',
                'envitem': 'splash',
                'engage': 'You\'re still a bit groggy. It may help to SPLASH some water on your face.\n     [PLAYER TIP: Areas marked with a  \'➼\' indicate an action. Type \"INTERACT SPLASH\" or \"INT SPLASH\" to wash your face!\n   WARNING! Not all interactions are beneficial! Think twice before you try an action!]',
                'interact': '\nYou splash some water on your face. You feel a little more refreshed.'
                },
        'Camp': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Drawbridge',
                'desc': 'You muster with the rest of the knights. After an uninspiring speech by your commander, you\'re told to move out.\n     You prepare to march further \'North\' to the Dark Wizard\'s castle.\n       ...All hopes rest on this last attack. There\'s no turning back now. \n  ~ North: March forward to the Dark Wizard\'s castle. Your adventure is about to begin!'
                },
        'Drawbridge': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Courtyard_Main',
                'desc': 'As you and your comrades approach the castle, you notice the drawbridge has already been lowered. \n     \"Good fortunes men!\" the Commander shouts. \"Our previous raids must have destroyed the counterbalance! These demons are wide open for a frontal assault!\"\n                                                     \"CCCHHHAAAAAAAAARRRGGGEEE!!!\"\n   You feel something is amiss, but orders are orders. You rush forward across the bridge, laid out over a chasm which looks as though it leads down to Hell itself.\n     Just as your battalion reaches halfway across the bridge, your greeted by the sound of laughter so cold you can see your breath.\n   Screams of agony erupt behind you. Looking back, you see some of your comrades engulfed in what appears to be black flames.\n     You also take note the drawbridge had caught fire as well, blocking your only escape.\n   Your comrades rush into the the castle, swords drawn, ready to use skills they trained so hard to master. \n  ~ North: Follow your comrades!',
                'envitem': 'wait',
                'engage': 'This feels like a trap... You decide to WAIT for a moment to come up with a plan of attack. ',
                'interact': ' '
                },
        'Courtyard_Main': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Courtyard_Main',
                'east': 'Courtyard_Main',
                'west': 'Courtyard_Main',
                'desc': 'There\'s no going back, your only escape is now nothing but ash. You\'re standing in the main area of the castle courtyard.\n     Dead trees. Dead grass. A premonition of things to come?',
                'eqitem': 'sword',
                'gear': 'You dropped your SWORD. Mind still racing. Heart beating so hard it seems as though it will burst out of your chest.\n     Just being in the Dark Wizard\'s presence instilled you with a fear unlike any you\'ve felt before.\n   But this is no time to be weak! Pick up your SWORD and fight! For everlasting peace!\n     [PLAYER TIP: Areas marked with a \'⁍\' indicate there\'s something you can equip. Type \"EQUIP SWORD\" to pick up your sword and take down the Dark Wizard!]',
                'equip': 'You pick your sword up off the ground and sheathe it. It\'s slightly chipped, but still sharp as ever. It\'s been the most reliable companion you\'ve had this journey.\n    No way you\'re leaving it behind.'
                },
        'Courtyard_Main2': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Castle_Entrance',
                'east': 'Courtyard_East',
                'west': 'Courtyard_West',
                'desc': 'You\'re standing in the main area of the castle courtyard. \n  ~ North: Looks as though the entrance to the castle is up ahead. \n  ~ West: You once heard screaming coming from that direction. You can see something glistening from a nearby tree that caught fire. \n  ~ East: You see nothing but more dead foliage.',
                },
        'Courtyard_West': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Courtyard_Midwest',
                'east': 'Courtyard_Main2',
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
                'west': 'Courtyard_Main2',
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
                'south': 'Courtyard_Main2',
                'desc': 'You stand before a large door at least three times your height. There are spikes jutting out, some adorning human skulls. Intimidating? Yes.\n     You don\'t notice a way to open it from here. \n  ~ South: The main area of the courtyard. Feels more like the entrance to a nightmare.'
                },
       'Castle_Entrance2': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Corridor',
                'south': 'Courtyard_Main2',
                'desc': 'You stand at the entrance to the castle. The opening to the main hall resembling a mouth ready to swallow you, never to see the light again.  \n  ~ North: The corridor th the castle\'s main hall lies before you.  \n  ~ South:  The main area of the courtyard. Feels more like the entrance to a nightmare.'
                },
        'Corridor': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Hall',
                'desc': 'The door slams behind you! There\'s no way to open it from here. The only way to go is forward. Great.  \n  ~ North: There is a hallway leading to the main hall of the castle.'
                },
        'Hall': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Hall_South',
                'desc': 'You walk slowly into the hall, guard up. Again, you hear that cold laughter. You instinct look behind you to notice the black flames again.\n     You get out of the range of the fire as a goblin jumps down from the ceiling behind you. Trying for a sneak attack!  \n  ~ North: You decide to run and fight another day. You decide fighting in a flaming hallway isn\'t the best idea.',
                'envitem': 'fight',
                'engage': 'You pull out your sword, ready to FIGHT.',
                'interact': ' '
                },
        'Main_Hall_South': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Hall_Center',
                'east': 'Main_Hall_Southeast',
                'west': 'Main_Hall_Southwest',
                'desc': 'The hallway had collapsed from the explosion. Every move you seem to make, you find yourself further ensnared in some sort of trap.  \n  ~ North: The center of the main hall. You notice a dark but beautiful light in the distance.  \n  ~ West: A corner of the main hall.  Wait...is that a. ..hole there?  \n  ~ East: A corner of the main hall. You notice some furniture and candles flickering in the distance.'
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
                'invitem': 'flint',
                'item': 'You see a piece of FLINT rock under one of the torches by the door.'
                },
        'Kitchen': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Meat_Locker',
                'south': 'Main_Hall_West',
                'desc': 'You\'re in the castle\'s kitchen. Who would\'ve guessed that monsters cook their food?  \n  ~ North: There\'s a door. Maybe the castle\'s pantry?  \n  ~ South: A door back to the castle\'s main hall.',
                'envitem': 'cook',
                'engage': 'There\'s a place to COOK here.',
                'interact': ' '
                },
        'KitchenA': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Meat_Locker',
                'south': 'Main_Hall_West',
                'desc': 'You\'re in the castle\'s kitchen. Who would\'ve guessed that monsters cook their food?  \n  ~ North: There\'s a door. Maybe the castle\'s pantry?  \n  ~ South: A door back to the castle\'s main hall.',
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
                },
        'Main_Hall_East': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Barracks',
                'south': 'Main_Hall_Southeast',
                'east': 'East_Wing',
                'west': 'Main_Hall_Center',
                'desc': 'You\'re standing in the eastern portion of the main hall.  \n  ~ North: You see a door. You don\'t understand monster language, but you think you see a picture of a bed?  \n  ~ South: A corner of the main hall. You notice some furniture and candles flickering in the distance.  \n  ~ West: The center of the main hall. You notice a dark but beautiful light in the distance.  \n  ~ East: There is a pathway leading to the eastern tower.'
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
                'invitem': 'fire',
                'item': 'There\'s a scroll of FIRE here.',
                'eqitem': 'boots',
                'gear': 'Your eyes glance all across the armory. So many different shapes and sizes! Your eyes catch a pair of BOOTS that are probably your size...',
                'equip': 'You throw on the armored boots. Nobody\'s stepping on your toes anymore!'
                },
        'Main_Hall_Center': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Main_Hall_South',
                'east': 'Main_Hall_East',
                'west': 'Main_Hall_West',
                'purple': ' ',
                'green': ' ',
                'desc': 'There\'s a wall of green and purple flames that prevent you from going towards the main tower.\n     You notice two pillars, one on each side of the wall, corresponding with the colors of the flames. It looks like you could place an ORB on the top of each one.  \n  ~ South: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ West: This way will lead you to the western part of the main hall.  \n  ~ East: This way will lead you to the eastern part of the main hall.'
                },
        'Main_Hall_Center1': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Main_Hall_South',
                'east': 'Main_Hall_East',
                'west': 'Main_Hall_West',
                'desc': 'There\'s a wall of green flames that prevent you from going towards the main tower.\n     Placing the green orb on the other pillar should rectify that!  \n  ~ South: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ West: This way will lead you to the western part of the main hall.  \n  ~ East: This way will lead you to the eastern part of the main hall.'
                },
        'Main_Hall_Center2': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Main_Hall_South',
                'east': 'Main_Hall_East',
                'west': 'Main_Hall_West',
                'desc': 'There\'s a wall of purple flames that prevent you from going towards the main tower.\n     Placing the purple orb on the other pillar should rectify that!  \n  ~ South: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ West: This way will lead you to the western part of the main hall.  \n  ~ East: This way will lead you to the eastern part of the main hall.'
                },
        'Main_Hall_Center3': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Main_Hall_South',
                'east': 'Main_Hall_East',
                'west': 'Main_Hall_West',
                'desc': 'There\'s a wall of green flames that prevent you from going towards the main tower.\n     Maybe there\'s another ORB somewhere here that can remove the green flames as well?  \n  ~ South: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ West: This way will lead you to the western part of the main hall.  \n  ~ East: This way will lead you to the eastern part of the main hall.'
                },
        'Main_Hall_Center4': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Main_Hall_South',
                'east': 'Main_Hall_East',
                'west': 'Main_Hall_West',
                'desc': 'There\'s a wall of purple flames that prevent you from going towards the main tower.\n     Maybe there\'s another ORB somewhere here that can remove the purple flames as well?  \n  ~ South: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ West: This way will lead you to the western part of the main hall.  \n  ~ East: This way will lead you to the eastern part of the main hall.'
                },
        'Main_Hall_Center5': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Hall_North',
                'south': 'Main_Hall_South',
                'east': 'Main_Hall_East',
                'west': 'Main_Hall_West',
                'desc': 'You\'re in the center of the main hall. With the flames gone you are free to venture up the main tower.  \n  ~ North: Go towards the main tower!  \n  ~ South: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ West: This way will lead you to the western part of the main hall.  \n  ~ East: This way will lead you to the eastern part of the main hall.'
                },
        'Main_Hall_North': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Main_Hall_Center5',
                'up': 'Main_Tower1',
                'desc': 'You made it. You\'re at the base of the main tower. The Dark Wizard must be somewhere up top.\n     You notice the state of the room and realize that you must have missed one hell of a fight before the flame wall was cast.\n   There\'s monster parts, fallen brothers in arms, bomb residue, broken gear, eviscerated flesh, teeth... Memories you won\'t soon forget.\n     You notice claw marks and sword slashes on the walls. The northern wall is has a huge crack in it.  \n  ~ South: This will put you back into the main hall.  \n  ~ Up: Begin ascending the spiral staircase of the final tower!'
                },
        'Main_Hall_North2': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Tepes',
                'south': 'Main_Hall_Center',
                'up': 'Main_Tower1',
                'desc': 'You made it. You\'re at the base of the main tower. The Dark Wizard must be somewhere up top.\n     You notice the state of the room and realize that you must have missed one hell of a fight before the flame wall was cast.\n   There\'s monster parts, fallen brothers in arms, bomb residue, broken gear, eviscerated flesh, teeth... Memories you won\'t soon forget.\n     You notice claw marks and sword slashes on the walls. The northern wall is has a huge crack in it.  \n  ~ North: ????  \n  ~ South: This will put you back into the main hall.  \n  ~ Up: Begin ascending the spiral staircase of the final tower!'
                },
        'Main_Hall_North3': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Tepes2',
                'south': 'Main_Hall_Center5',
                'up': 'Main_Tower1',
                'desc': 'You made it. You\'re at the base of the main tower. The Dark Wizard must be somewhere up top.\n     You notice the state of the room and realize that you must have missed one hell of a fight before the flame wall was cast.\n   There\'s monster parts, fallen brothers in arms, bomb residue, broken gear, eviscerated flesh, teeth... Memories you won\'t soon forget.\n     You notice claw marks and sword slashes on the walls. The northern wall is has a huge crack in it.  \n  ~ North: You found the easter egg!  \n  ~ South: This will put you back into the main hall.  \n  ~ Up: Begin ascending the spiral staircase of the final tower!'
                },
        'Tepes': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Main_Hall_North3',
                'desc': 'What is a man?! A miserable little pile of secrets! But enough talk! Have at you!\n     You notice a lone treasure chest in this hidden room. You kick it open as hard as you can and spilled whatever contents it contained onto the cold, stone floor.   \n  ~ South: With your new super secret items and skills, you\'re ready to get up that tower!',
                'invitem': ['p.chop', 'belmont', 'rope'],
                'item': 'Who cooks a pork chop and hides it in a wall?!\n     Before you can even begin to ponder the answer, you notice a ROPE and the BELMONT scroll with the words \"Bloody Tears\" inscribed on the top.\n   You look over this weird haul of a P.CHOP, ROPE and BELMONT scroll, debating on whether or not to take them.\n     I mean, really? Who\'s idea was it to put a pork chop in a wall?'
                },
        'Tepes2': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Main_Hall_North3',
                'desc': 'What is a man?! A miserable little pile of secrets! But enough talk! Have at you!\n     There\'s nothing else here.',
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
                'up': 'Main_Hall_Southwest',
                'desc': 'You\'re standing in the entrance to the castle\'s dungeon. Who would have guessed that they actually keep prisoners?\n     There is a door to the \'North\'...Dammit! It\'s locked!  \n  ~ Up: A set of stairs leading back up into the main hall.'
                },
        'Jailroom1a': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Jailroom2',
                'up': 'Main_Hall_Southwest',
                'desc': 'You\'re standing in the entrance to the castle\'s dungeon. Who would have guessed that they actually keep prisoners?  \n  ~ North: Go deeper into the dungeon!  \n  ~ Up: A set of stairs leading back up into the main hall.'
                },
        'Jailroom2': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Jailroom1a',
                'desc': 'You arrive in a wide open room resembling a small colosseum. The Guardian Beast lies sleeping. A pile of bones lay before it. Some meat chunks still attached.\n     You don\'t believe it heard you enter.  \n  ~ South: Head back towards the stairs.',
                'envitem': ['sneak', 'run', 'kill'],
                'engage': 'A giant wolf-like creature lies sleeping between you and your exploration deeper into the dungeon.  \n     You think you may be able to SNEAK past it...  \n   ...but making a RUN to the other side could also be a viable option...  \n     ...You could also try to KILL the beast while it sleeps.',
                'interact': ' '
                },
        'Jailroom2a': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Jailroom3',
                'south': 'Jailroom1a',
                'desc': 'You are in a large open room resembling a small colosseum. A beast\'s corpse lies off to the side. Perhaps poisoned to death by a crafty, yet handsome adventurer?  \n  ~ North: head further into the dungeon.  \n  ~ South: Head back towards the stairs.'
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
                'inv': inventory,
                'inventory': inventory,
                'south': 'Jailroom3',
                'desc': 'This looks like an office of some sort. You hear moaning coming from the room to the north. Sounds like someone\'s hurt.\n     The door appears to be locked.  \n  ~ South: Head back to the dungeons cross-way',
                'invitem': 'oldwhip',
                'item': 'The warden\'s favorite weapon, an OLDWHIP lays next to its corpse. It looks very beat up. It must of used it a lot in it\'s lifetime.'
                },
        'Jailroom4a': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Jailroom5',
                'south': 'Jailroom3',
                'desc': 'This looks like an office of some sort. You hear moaning coming from the room to the north. Sounds like someone\'s hurt.  \n  ~ North: Head into the room. THe handle was cold to the touch.   \n  ~ South: Head back to the dungeons cross-way',
                'invitem': 'oldwhip',
                'item': 'The warden\'s favorite weapon, an OLDWHIP lays next to its corpse. It looks very beat up. It must of used it a lot in it\'s lifetime.'
                },
        'Jailroom4b': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Jailroom5a',
                'south': 'Jailroom3',
                'desc': 'You\'re back in the Warden\'s office.  \n  ~ North: Head back in the poor bastard\'s room.   \n  ~ South: Go to the dungeons cross-way',
                'invitem': 'oldwhip',
                'item': 'The warden\'s favorite weapon, an OLDWHIP lays next to its corpse. It looks very beat up. It must of used it a lot in it\'s lifetime.'
                },
        'Jailroom4c': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Jailroom5b',
                'south': 'Jailroom3',
                'desc': '\"You\'re just weak! DO IT! DO IT DAMN YOU! YOU BELONG IN THIS CASTLE! YOU\'RE A DEMON! A DEMON!!!"\n     His voice fades as you walk out of the room unable to look up form the floor.\n   The last thing you hear before shutting the door are his desperate cries of anger and hopelessness. It cut deeper then any sword could.\n     You\'re back in the Warden\'s office.  \n  ~ North: Head back in the poor bastard\'s room.   \n  ~ South: Go to the dungeons cross-way',
                'invitem': 'oldwhip',
                'item': 'The warden\'s favorite weapon, an OLDWHIP lays next to its corpse. It looks very beat up. It must of used it a lot in it\'s lifetime.'
                },
        'Jailroom4d': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Jailroom5b',
                'south': 'Jailroom3',
                'desc': 'The poor bastard continues weeping as you walk back into the Warden\'s office. \n  ~ North: Head back in the poor bastard\'s room.   \n  ~ South: Go to the dungeons cross-way',
                'invitem': 'oldwhip',
                'item': 'The warden\'s favorite weapon, an OLDWHIP lays next to its corpse. It looks very beat up. It must of used it a lot in it\'s lifetime.'
                },
        'Jailroom5': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Jailroom4c',
                'mercy': 'Jailroom4b',
                'desc': 'The room is freezing. Through your breath, you see a knight chained up -no. HANGING on the wall. He\'s still alive!\n     He\'s missing both of his legs and one of his arms from the elbow down. His body has a light blue hue. You hear gentle sobbing.\n   You don\'t believe he even notices you\'re there.\n     \"How long has he been here?\" you wonder. He\'s not from your battalion. You walk closer, not knowing what to say, or how to react.\n   The gentle sobbing you hear slowly turns into words you can start making out: \"Kill me...Kill..me..\" he says.\n     \"What?!\" \"Kill Me!!Kill Me Kill MeKillMeKillMeKillMeKIlLMEkIlLMeKILLMEKILLMEKILLME!!!!!  ....please....\"\n  \n  ~ South:  "I...I can\'t..." Go back to the Warden\'s office and leave the poor bastard there.  \n  ~ Mercy:  "I...I\'ll do it..." The best thing to do for this man is to offer him the release he asks.',
                'invitem': 'blizzard',
                'item': 'You see a spell scroll. The scroll reads BLIZZARD on it. Must have been used to keep the room so cold.',
                'eqitem': 'breastplate',
                'gear': 'The poor bastards armor lies in a pile in the corner. It\'s all cracked and dented. No longer fit for use.\n     But wait! you notice the BREASTPLATE is relatively untouched. It\'s freezing, but will warm up with your body heat.',
                'equip': 'You throw on the breastplate. it\'s cold enough to hurt your skin a little. You look forward to getting out of this room to warm it up.'
                },
        'Jailroom5a': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Jailroom4b',
                'desc': 'The poor bastard looks like he died with a smile. \n  ~ South:  Go back to the Warden\'s office. You don\'t want to be here any longer than you need to.',
                'invitem': 'blizzard',
                'item': 'You see a spell scroll. The scroll reads BLIZZARD on it. Must have been used to keep the room so cold.',
                'eqitem': 'breastplate',
                'gear': 'The poor bastards armor lies in a pile in the corner. It\'s all cracked and dented. No longer fit for use.\n     But wait! you notice the BREASTPLATE is relatively untouched. It\'s freezing, but will warm up with your body heat.',
                'equip': 'You throw on the breastplate. it\'s cold enough to hurt your skin a little. You look forward to getting out of this room to warm it up.'
                },
        'Jailroom5b': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'Jailroom4d',
                'mercy': 'Jailroom4b',
                'desc': '\"...Please...\" He cries.  \n  ~ South:  "I...I can\'t..." Go back to the Warden\'s office and leave the poor bastard there.  \n  ~ Mercy:  "I...I\'ll do it..." The best thing to do for this man is to offer him the release he asks.',
                'invitem': 'blizzard',
                'item': 'You see a spell scroll. The scroll reads BLIZZARD on it. Must have been used to keep the room so cold.',
                'eqitem': 'breastplate',
                'gear': 'The poor bastards armor lies in a pile in the corner. It\'s all cracked and dented. No longer fit for use.\n     But wait! you notice the BREASTPLATE is relatively untouched. It\'s freezing, but will warm up with your body heat.',
                'equip': 'You throw on the breastplate. it\'s cold enough to hurt your skin a little. You look forward to getting out of this room to warm it up.'
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
                'desc': 'You\'re standing in the main room of the western tower.  \n  ~ North: There is a door lying on the floor. It was kicked open. There is a room wide open. You can see a body in there wearing your kingdom\'s colors.  \n  ~ South: There is a walkway that looks to lead outside.  \n  ~ West: There is a doorway.  \n  ~ East: There is a doorway. \n  ~ Up: There\'s a set of stairs leading further up the tower.  \n  ~ Down: There\'s a set of stairs leading back down to the main floor of the castle.',
                'envitem': 'check',
                'engage': 'There\'s a corpse of a monster lying on the ground clenching a spear. It\'s clad in armor. It was probably a guard. The armor seems relatively in tact.\n     Do you want to CHECK it?',
                'interact': 'As you approach closer, the monster takes a stab at you...............and misses!\n     You thrust your sword into an opening in the armor around the back of its neck. While the armor is in tact, no part of it will fit a human. Damn.'
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
                'desc': 'You step out to the balcony and take in the sights. You feel heat on your face and the smell of iron is thick in the air. It\'s a depressingly melancholy view.  \n  ~ North: Go back into the main room.'
                },
        'West1_East': {
                'inv': inventory,
                'inventory': inventory,
                'west': 'West1_Main',
                'desc': 'You walk into the room, stepping over the guard in the process. You\'re standing in a bedchamber. It looks exquisite.  \n  ~ West: Go back into the main room.',
                'invitem': 'note',
                'item': 'There\'s a NOTE that reads:\n     \"That damn guardian beast! Why in all hells am I tasked to take care of the cursed thing?! The damnable creature won\'t even eat it\'s meat raw unless I starve it!\n   I transported it to the dungeon for now. I don\'t even want to see it unless I have to.\n     It\'s below me to be that lowly creature\'s caretaker! I\'ll just be it\'s undertaker instead...\"\n   It looks as though there is a plan to try to poison the food of some sort of creature.\n     There are multiple ideas written here. You wonder if that beast is somewhere here...'
                },
        'West1_West': {
                'inv': inventory,
                'inventory': inventory,
                'east': 'West1_Main',
                'desc': 'A room full of potions and vials. Alchemy was performed here.  \n  ~ East: Go back to the main room',
                'invitem': 'poison',
                'item': ' A vial of POISON sits close by the note. It\'s been knocked over, but is still intact and sealed tightly.'
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
                'desc': 'A treasure room sits atop the western tower. There\'s everything from gold to magic armor. Spells you can\'t even begin to read, weapons too heavy to wield.\n     You are more impressed to find something in this castle that actually shines to counteract the encompassing bleakness. It\'s also unusually hot in here.  \n  ~ South: The main room of the top floor.',
                'invitem': 'p.orb',
                'item': 'You see a purple orb siting atop a pillar. Its light is both blinding and welcoming. Terrifying, yet comforting.\n     The P.ORB shines brightly, yet somehow the light barely stretches for more than a meter.\n   However, there looks to be a thread of light pointing in the direction on the castle, as if telling you where it wants to go.',
                },
        'West2_Treasure2': {
                'inv': inventory,
                'inventory': inventory,
                'desc': 'The purple orb feels warm in your hand. After putting it away, The pillar begins to crack, and purple flames begin to leak out.\n     Soon enough, the flames surround the pillar and burn it to nothingness. The flames take an almost human form.\n   It nods it\'s \"head\" back and forth, as if it was eying you up.  You don\'t exactly know what this thing is, but you know it\'s hostile.',
                'envitem': ['run', 'fight'],
                'engage': 'There\'s a living flame in the shape of a man.\n     It doesn\'t stand between you and the door. You could probably RUN for it!\n   Everything can bleed! FIGHT it!',
                'interact': ' '
                },
        'West2_Treasure3': {
                'inv': inventory,
                'inventory': inventory,
                'desc': 'The purple orb feels warm in your hand. After putting it away, The pillar begins to crack, and purple flames begin to leak out.\n     Soon enough, the flames surround the pillar and burn it to nothingness. The flames take an almost human form.\n   It nods it\'s \"head\" back and forth, as if it was eying you up.  You don\'t exactly know what this thing is, but you know it\'s hostile.',
                'envitem': ['run', 'fight'],
                'engage': 'There\'s a living flame in the shape of a man.\n     It doesn\'t stand between you and the door. You could probably RUN for it!\n   Everything can bleed! FIGHT it!\n    Or maybe you have something you can use....',
                'interact': ' '
                },
        'West2_Treasure4': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'West2_Main',
                'desc': 'The room is freezing. You can see you breath and almost everything in here is is so could it would hurt to touch your bare skin.',
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
                'inv': inventory,
                'inventory': inventory,
                'south': 'East2_Main',
                'desc': 'It\'s a reflective room. Shimmering crystals all around you. As you look around the room, you see no less than 20 you staring in every direction.\n     The wall at the \'North\' end of the room is distinct from the others. It is one giant mirror, and it\'s reflection give off a darker tint than the rest.  \n  ~ South: It\'s the main hall of the top of the eastern tower.'
                },
        'East2_Duality2': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'East2_Treasure',
                'south': 'East2_Main',
                'desc': 'It\'s a reflective room. Shimmering crystals all around you. As you look around the room, you see no less than 20 you staring in direction.  \n  ~ North: After poking the wall, it now seems more liquid than solid. You can likely pass through.  \n  ~ South: It\'s the main hall of the top of the eastern tower.'
                },
        'East2_Treasure': {
                'inv': inventory,
                'inventory': inventory,
                'desc': 'You walk through the mirror and are now standing in a mirror room almost completely similar to the one you were just in. There is no visible door. Instead, another\n     mirror wall is adjacent to your position.  You walk to the wall and you see that your reflection looks as though its walking towards you too...\n   ...Wait! It IS walking towards you! You stop. So does it. You raise your left hand and it simultaneously raises its right. You aren\'t sure what this means, but you\n     know it can\'t be good. You take out your sword, which was sheathed on your left hip, holding it in your right hand. You\'re ready for a fight. It unsheathes it\'s\n   sword from it\'s right hip and grasps its sword in its left hand. It\'s eyes are different colors. One a dark red, the other illuminating a dark green light.\n     "What the hells are you?" You say. It matches your lip movements, but no words come out. "Can you not speak?" It copies your mouth movements again in silence.\n                       You think to yourself that you many have an item to defeat it...',
                },
        'East2_Treasure2': {
                'inv': inventory,
                'inventory': inventory,
                'south': 'East2_Duality2',
                'desc': 'You now stand alone in an atmosphere of magic. There is an opening of light to the south leading out of here.  \n  ~ South: Head back into the real world.',
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
                'desc': 'You are in a rather nice hall. Opposite of everything below.  \n  ~ East: Looking down the corridor, you see a rather large room. From here it looks to keep a similar aesthetic to this room.  \n  ~ Down: You can head back down to the previous floor.'
                },
        'Main_Tower_F2R2': {
                'inv': inventory,
                'inventory': inventory,
                'desc': 'You arrive in a gigantic room. Much bigger than you expected. It\'s like a giant dining hall.\n     Before you get a chance to admire the scenery, a dark figure emerges from the shadows.\n   It\'s the Dark Wizard\'s most powerful lackey...the Black Mage!\n                  Type \'COMMENCE\' to start the fight!'
                },
        'Main_Tower_F2R2a': {
                'inv': inventory,
                'inventory': inventory,
                'west': 'Main_Tower_F2R1',
                'desc': 'The room is up in flames. Everything is falling apart. The Dark Wizard lies ahead, but there is a giant hole in the floor that\'s impossible to jump across. There\'s a rafter that still looks sturdy enough. If you only had something to swing across with.  \n  ~ West: You need to run back down! You have nothing to swing across with!',
                },
        'BM_Battlea': {
                'desc': 'He crouches down slightly, both hands by his sides. Palms up. It looks as though he\'s holding shadows in the palms of his hands.\n      You unsheathe your sword, take a big gulp, and prepare for a fight. There\'s no point playing defensive against an opponent like this!\n                               What will you do?  \n  ~ Strike: Rush forward and strike him with your sword! Show him you aren\'t afraid!  \n  ~ Counter: Don\'t be a fool! wait for an opening to strike!'
                },
        'BM_Battleb': {
                'desc': 'Fear has worked for the Black Mage in the past. Not this time though. Your blow lands, but it isn\'t fatal. He teleports to the farthest side of the room to gain\n     some distance. \n                               What will you do?  \n  ~ Rush: Rush at him again! Distance is only advantageous to him!  \n  ~ Hide: Don\'t play into his hands. He\'ll be expecting the same type of attack twice.'
                },
        'BM_Battlec': {
                'desc': 'You rush towards him again. Not giving him a moment to cast. You slash at him but he teleports before your sword can connect. You look all around but can\'t find him.\n     You feel like the room is getting hotter. You look above you to see the Black Mage! His one arm raised, he throws it down immediately followed by a stream of dark\n   fire. You jump out of the way in the nick of time, but not without its costs. Your leg was hit! It\'s sustained burns and slightly hurts to stand on. \n                               What will you do?  \n  ~ Blind: If he can\'t see you, he can\'t hit you.  \n  ~ Hide: Try to take a moment to come up with a plan of attack.'
                },
        'BM_Battled': {
                'desc': 'You decide to use the fire around you to your advantage. You hang back where he just struck at you. leaving flames erupting where you once stood.\n     If you can use your sword to reflect the light back at him, you may be able to disorient him enough for a fatal blow.  He teleports nearby and you lay your sword\n   flat in front of you. He looms quickly towards you. His arms out, as if reaching for your throat. You can\' get any light to reflect! These aren\'t normal flames!\n     It\'s a dark, shadowy type of fire. \"DAMMIT! STUPID!\" you scream as you jump back in the the nick of time. You lose your balance for a moment and\n   fall on your arse, clutching your neck. He managed to claw your throat a little. You look down at your palm to see blood sticking to it. \n                               What will you do?  \n  ~ Bow: You spot a bow and quiver on the wall. Maybe you can match his distance.  \n  ~ Charge: You don\'t know if you\'ll be able to dodge many more of his attacks. Charge in and end this! '
                },
        'BM_Battlee': {
                'desc': ''
                },
        'BM_Battlef': {
                'desc': 'You rush towards him in a serpentine pattern. Midway towards him, you keep veering off and take cover behind a statue depicting the Dark Wizard.\n     You use your sword to try to see around the statue, but the Black Mage is nowhere to be found! He must\'ve teleported again! You quickly turn your head\n   around to see the Black Mage close at your side. His arm stretched out towards you, hand open palmed. Likely about to place some unholy curse upon you.\n     By instinct alone, you swing at him again. Before you even realize what happened, you catch yourself with your sword raised above your head and his hand lying\n   limply on the stone floor. He howls of pain. He teleports away from you. He\'s not dead, but he\'s weakened.\n                               What will you do?  \n  ~ Shield: Use a shield on the wall to protect yourself!  \n  ~ Hand: Maybe you can use his hand as a weapon. If it had magic imbued in it when it was severed, it should still be in there!'
                },
        'BM_Battleg': {
                'desc': 'You grab his limp hand. If it had magic imbued into it when it was severed, it may yet be in there. You hear him screaming in pain or rage.\n     You can\'t tell. Perhaps both. You come around the statue to see him in the process of setting the room on fire. Looks like he means to trap you here.\n   The wizard looks down to see you holding his severed hand. He stops casting for a moment. Whispers something to himself and you are now unable to move.\n     Well, guess that proves your theory about the magic still being embedded in it. Dark energy surges around is still attached hand and he aims it at you.\n   Whatever is coming next isn\'t good. You keep tying to force yourself to move and slowly it comes. As he casts his spell you manage to make yourself fall over,\n     but not before the magic brushes your shoulder. Sending a wave of a cold burn to the area. The pain doesn\'t seem to be subsiding for the moment.\n                               What will you do?  \n  ~ Bow: You spot a bow and quiver on the wall. Maybe you can match his distance.  \n  ~ Shield: Use a shield on the wall to protect yourself!'
                },
        'BM_Battleh': {
                'desc': 'You\'re back on your feet, ready to end this. You look around, scanning the room for anything you can use. Your eyes fixate on a bow perched on the wall.\n     That could work to counteract the distance. With the Black Mage still in a rage, firing off spells in all directions, you decide its\'s best to\n   go now before he fully composes himself again. You rush to the wall, narrowly dodging some stray flames. You grab the bow and quiver. You pull out an arrow and\n     are ready to fire. You shoot. Your aim is true but as the arrow rushes to its target it is turned to ash by a stream of fire heading in the opposite direction.\n   The fire continues its path, and strikes you. Again you narrowly dodge but, do not come out unscathed.\n     As you dive to the side it scorches your leg. The bow had also caught fire. Iti s no longer usable.\n                               What will you do?  \n  ~ Charge: You don\'t know if you\'ll be able to dodge many more of his attacks. Charge in and end this! \n  ~ Shield: Use a shield on the wall to protect yourself!'
                },
        'BM_Battlei': {
                'desc': 'You quickly but carefully get to your feet. You run behind a statue to try to get a moment to breath and get used to the pain. You use your sword to try to see\n     around the statue, but the Black Mage is nowhere to be found! He must\'ve teleported again! You quickly turn your head around to see the Black Mage close at your\n   side. His arm stretched out towards you, hand open palmed. Likely about to place some unholy curse upon you. By instinct alone, you swing at him again.\n     Before you even realize what happened, you catch yourself with your sword raised above your head and his hand lying limply on the stone floor.\n   He howls of pain. He teleports away from you. He\'s not dead, but he\'s weakened.\n                               What will you do?  \n  ~ Bow: You spot a bow and quiver on the wall. Maybe you can match his distance.  \n  ~ Hand: Maybe you can use his hand as a weapon. If it had magic imbued in it when it was severed, it should still be in there!'
                },
        'BM_Battlej': {
                'desc': 'You run to get yourself a shield while the Black Mage is weakened. He\'s angry now. He\'s not even aiming for you anymore. In his rage, he raises his arms above his\n     head and begins to set the whole room ablaze. Fire is shooting from his fingers. Lava erupting from his stump.\n   Likely his blood is catching fire as well.  You need to make your move soon, so you decide to go for the kill while he\'s unfocused.\n     As you rush towards him, you catch is focus once more as he turns his hands towards you. You raise your shield and keep rushing forward.\n   You slowly progress, shield raised like an umbrella in a storm with high winds you inch closer. Without a single wasted movement you plunge your sword into him.\n     The fire stops. The Black Mage falls backwards. Bewildered and unable to move.\n                                   Type \'continue\' to keep heading up the tower.',
                },
        'BM_Battlek': {
                'desc': 'You stand up. No point in letting the Black Mage know you\'re injured. He\'ll only exploit it. You immediately get back up and charge at him again.\n     He blasts fire at you, but the injuries you sustained slow you down and you\'re unable to fully dodge. You\'re body is about roughly 60% burned now. You\'re in trouble.\n                               What will you do?  \n  ~ Possum: Feint being dead. You may be able to get a fatal blow if he lets his guard down.  \n  ~ Bow: You see a bow and quiver on the wall. A frontal assault hasn\'t worked. Maybe a long range attack will.'
                },
        'BM_Battlel': {
                'desc': 'You wait for an opportunity to strike. You eye him down, watching his every movement. He begins to cast but you see nothing. You feel heat from behind you.\n     You spin around as a fireball hits you squarely on your left side. You go down. Your entire side covered in burns. The Black Mage laughs maniacally.\n                               What will you do?  \n  ~ Recoup: Find cover and recuperate for a moment..  \n  ~ Endure: Don\'t show weakness! Get up and show the Black Mage you won\'t go down easy!'
                },
        'BM_Battlem': {
                'desc': 'You get back on your feet. You look around, scanning the room for anything you can use. Your eyes fixate on a bow perched on the wall. That could work!\n     You rush to the wall, as the Black Mage fires off two more dark fire blasts, which you narrowly dodge. You grab the bow and quiver. There\'s only one arrow in it.\n   You pull pull it out of the quiver and prepare to fire. You let the arrow fly and... *THUNK!*  You hit!\n     While not a killing blow, you land the arrow in the Black Mage\'s shoulder. He lurches backwards, yelling in pain as he rips the arrow out. \n   Enraged, he begins to engulf the room in flames. He\'s trying to end you one way or another.\n                               What will you do?  \n  ~ Shield: Use a shield on the wall to protect yourself!  \n  ~ Reflect: Well, the fire cast IS technically magic...so perhaps reflecting his attack back at him will work!'
                },
        'BM_Battlen': {
                'desc': 'You get back on your feet. You look around, scanning the room for anything you can use. Your eyes fixate on a bow perched on the wall. That could work!\n     You rush to the wall, as the Black Mage fires off two more dark fire blasts, which you narrowly dodge. You grab the bow and quiver. There\'s only one arrow in it.\n   You pull pull it out of the quiver and prepare to fire. In one fluid motion, you turn and shoot. The pain in your leg causes you to lose balance momentarily.\n     *THUNK!*  You hit!  While not a killing blow, you land the arrow in the Black Mage\'s stomach. He lurches backwards, rips the arrow out of his stomach and\n   screams as he begins setting the entire room oh fire. Oddly enough as the room fills with the fire, it seems to get darker. He\'s getting desperate.\n                               What will you do?  \n  ~ Charge: You don\'t know if you\'ll be able to dodge many more of his attacks. Charge in and end this! \n  ~ Shield: Use a shield on the wall to protect yourself!'
                },
        'BM_Battleo': {
                'desc': 'You grab his limp hand. If it had magic imbued into it when it was severed, it may yet be in there. You hear him screaming in pain or rage.\n     You can\'t tell. Perhaps both. You come around the statue to see him in the process of setting the room on fire. Looks like he means to trap you here.\n   The wizard looks down to see you holding his severed hand. He stops casting for a moment. Whispers something to himself and you are now unable to move.\n     Well, guess that proves your theory about the magic still being embedded in it. Dark energy surges around is still attached hand and he aims it at you.\n   Whatever is coming next isn\'t good. You keep tying to force yourself to move and slowly it comes. As he casts his spell you manage to make yourself fall over,\n     but not before the magic brushes your shoulder. Sending a wave of a cold burn to the area. The pain doesn\'t seem to be subsiding for the moment.\n                               What will you do?  \n  ~ Reflect: Well, the fire cast IS technically magic...so perhaps reflecting his attack back at him will work!  \n  ~ Charge: You don\'t know if you\'ll be able to dodge many more of his attacks. Charge in and end this!'
                },
        'BM_Battlep': {
                'desc': 'You notice the mirror behind him. You sprint towards him, sword drawn in an attempt to scare him into teleporting to another part of the room. He takes the bait as\n     you draw near him. You keep charging for the wall and rip the mirror off. It\'s about half your height. You turn as a dark fire blast rushes towards you.\n   You raise the mirror as you get some pushback. You thrust the mirror forward as if pushing something off of you. You send the spell right back as the force shatters\n     the mirror. The flames hit the Black Mage, setting him ablaze. He cancels his spell, while injured, he still isn\'t down. He\'s desperate to end this. He starts\n     casting fire around the entire room, meaning to trap you.\n                               What will you do?  \n  ~ Charge: You don\'t know if you\'ll be able to dodge many more of his attacks. Charge in and end this! \n  ~ Shield: Use a shield on the wall to protect yourself!'
                },
        'BM_Battleq': {
                'desc': 'You don\'t bother getting up. You keep your sword in hand, knowing enemies like this tend to gloat when they win a battle.  Turns out you know nothing.\n     He simply shoots more fire at you until you\'re nothing but a pile of ash and armor. Your journey is at an end.'
                },
        'BM_Battler': {
                'desc': 'You look around, scanning the room for anything you can use. Your eyes fixate on a bow perched on the wall nearby. That could work!\n     You slowly get up. The Black Mage doesn\'t notice you\'re back on your feet. He doesn\'t notice you at all, not perceiving you as a threat.\n   You grab the bow and quiver. There\'s only one arrow in it. You pull pull it out of the quiver and prepare to fire. You let the arrow fly and...\n     *THUNK!*  You hit!  While not a killing blow, you land the arrow in the Black Mage\'s shoulder. He lurches backwards, yelling in pain as he rips the arrow out.\n   He seems offended you were able to hurt him. He begins setting the entire room oh fire. Seeing you still as more of an annoyance then an opponent,\n     he wants to end this quickly.\n                               What will you do?  \n  ~ Charge: You have to stop the flames from spreading! A frontal assault is your only option!\n  ~ Hide: Shield yourself from the flames. Frontal assaults haven\'t been working for you yet.'
                },
        'BM_Battles': {
                'desc': 'You don\'t have time to waste. The room is filling with fire. Escape is almost an impossibility. You get back up, prepared to launch an all or nothing attack.\n     You clutch your sword tight, whisper a prayer to yourself and rush towards the Black Mage. As you get closer, the heat intensifies.\n   You rush closer still. Sword ready to pierce him when you are paralyzed once more! You move your eves down to see the dismembered hand once again has a hold on you!\n     At such a close range there\'s no time to dodge the Black Mages incoming attack. As he screams, fire erupts around you and closes in on you. Your journey is at an end.'
                },
        'BM_Battlet': {
                'desc': 'You take cover behind a statue depicting the Dark Wizard. You use your sword to try to see around the statue, but the Black Mage is nowhere to be found!\n     He must\'ve teleported! You didn\'t take his bait and he\'s trying a different tactic. You quickly turn your head around to see the\n   Black Mage close at your side. His arm stretched out towards you, hand open palmed. Likely about to place some unholy curse upon you.\n     By instinct alone, you swing at him again. Before you even realize what happened, you catch yourself with your sword raised above your head and his hand lying\n   limply on the stone floor. He howls of pain. He teleports away from you. He\'s not dead, but he\'s weakened. He begins filling the room with fire again.\n     It doesn\'t seem to be any ploy this time. He just want you dead. \n                               What will you do?  \n  ~ Charge: You don\'t know if you\'ll be able to dodge many more of his attacks. Charge in and end this! \n  ~ Shield: Use a shield on the wall to protect yourself!'
                },
        'BM_Battleu': {
                'desc': 'You notice the mirror behind him. You sprint towards him, sword drawn in an attempt to scare him into teleporting to another part of the room. He takes the bait as\n     you draw near him. You keep charging for the wall and rip the mirror off. It\'s about half your height. You turn as a dark fire blast rushes towards you. The blast\n   is bigger than the mirror! It wraps around the mirror, scalding your hands and face. You drop the mirror and scream in pain.\n     Now is not the time to wallow in it. You have a fight on your hands!\n                               What will you do?  \n  ~ Charge: You don\'t know if you\'ll be able to dodge many more of his attacks. Charge in and end this! \n  ~ Shield: Use a shield on the wall to protect yourself!'
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
                'desc': 'The Dark Wizard is here. He turns around. He\'s looking more in your general direction then at you.\n     Up close, he just looks like a floating robe with to small white flames for eyes. He doesn\'t speak. Maybe he can\'t speak...?\n   The left side of his robe flutters for a brief moment, and once again the room is surrounded by black fire. He begins making that cold laugh again.\n     He floats up and out the balcony. Flying in the direction of the kingdom. His army will feast tonight. and you will burn.'
                },
        'Main_Tower_Final2a': {
                'inv': inventory,
                'inventory': inventory,
                'north': 'Main_Tower_Final3',
                'desc': 'Like everything else in this damnable castle, it has been set ablaze. There is still a small part the flames haven\'t gotten to yet.  Luckily a door is there.  \n  ~ North: It\'s the only exit!.'
                },
        'Main_Tower_Final3': {
                'desc': 'Ths is the Dark Wizard\'s chambers. You can only focus on the bed. There is no way out. Nowhere to go. You\'re so tired.\n     You fought the Dark Wizard and won. Nobody will know what you did. No bards will sing songs of your legendary feats.\n   You are just a man. A man that overcame adversity to protect all he holds dear. You don\'t care.',
                'envitem': 'sleep',
                'engage': 'THe bed is inviting you are ready to SLEEP.',
                'interact': ' '
                }
        }
# Players Starting Point
#CurrentRoom = 'Tent'
# Test Rom
CurrentRoom = 'Main_Tower_F2R1'

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
            if type(rooms[CurrentRoom]['invitem']) is str:
                inventory += [move[1]]
                print('You added ' + move[1] + ' to your inventory!')
                del rooms[CurrentRoom]['invitem']
            elif type(rooms[CurrentRoom]['invitem']) is list:
                inventory += [move[1]]
                print('You added ' + move[1] + ' to your inventory!')
                rooms[CurrentRoom]['invitem'].remove(move[1])
                if len(rooms[CurrentRoom]['invitem']) == 0:
                    del rooms[CurrentRoom]['invitem']
        # If there is no item to get
        else:
            print('Your mind must be playing tricks on you. There\'s no ' + move[1] + ' there!')

    # If player types 'interact' or 'int' first
    if move[0].lower() == 'interact' or move[0].lower() == 'int':
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
    if move[0].lower() == 'inventory' or move[0].lower() == 'inv':
        if 'inv' or 'inventory' in rooms[CurrentRoom]:
            print(f"Inventory: {inventory}")
            print(f"Equipment: {equipment}")

    # If player types 'quit' or 'q'
    if move[0].lower() == 'quit' or move[0].lower() == 'q':
        print('Are you sure you want to exit (y/n)?:')
        quit_query = input('> ')
        if quit_query.lower() == "yes" or quit_query.lower() == "y":
            break
        elif quit_query.lower() == "no" or quit_query.lower() == "n":
            print('Good luck!')
        else:
            print('What do you mean by that?')

# later if time
    # If player types 'status'
    #if move[0].lower() == 'status':


#═══════════════════════════════════════════════════════════════════════════════════════════════════════
#══════════════════════════════════════ ROOM SPECIFIC SCRIPTS ══════════════════════════════════════════
#═══════════════════════════════════════════════════════════════════════════════════════════════════════
    # Drawbridge ~ Special Option: Wait
    if CurrentRoom == "Drawbridge" and move[0].lower() == 'interact' and move[1].lower() == 'wait':
        print('''
        You sense a trap, as though you're being lured in. You pause for a moment to decide your next move. However, a moment was
           all it took for the bridge to give way due to the black flames. You had misjudged the intensity of the Dark Wizard's
                                 flame. You fall into the abyss below. Your journey is at an end.

                                                            |      |   
                                                            |  |   |     
                                                            |  |   |              
                                                               | _ _ 
                                                            \   / /    
                                                             0__\/
                                                            \/
              ________    _____      _____  ___________               ____________   _________________________ 
             /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
            /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
            \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
             \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                    \/         \/         \/        \/                        \/                 \/         \/ 
        ''')
        break

    if CurrentRoom == "Drawbridge" and move[0].lower() == 'int' and move[1].lower() == 'wait':
        print('''
        You sense a trap, as though you're being lured in. You pause for a moment to decide your next move. However, a moment was
            all it took for the bridge to give way due to the black flames. You misjudged the intensity of the Dark Wizard's
                                  flame. You fall into the abyss below. Your journey is at an end.

                                                            |      |   
                                                            |  |   |     
                                                            |  |   |              
                                                               | _ _ 
                                                            \   / /    
                                                             0__\/
                                                            \/
               ________    _____      _____  ___________               ____________   _________________________ 
              /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
             /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
             \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
              \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                     \/         \/         \/        \/                        \/                 \/         \/ 
         ''')
        break

    # Courtyard_Main ~ Can't leave without the sword!
    if CurrentRoom == "Courtyard_Main" and move[0].lower() == 'equip' and move[1].lower() == 'sword':
        rooms[CurrentRoom] = rooms["Courtyard_Main2"]
#    elif CurrentRoom == "Courtyard_Main" and move[0].lower() == 'go' and move[1].lower() == 'north':
#        rooms["Courtyard_Main"]["desc"] = "You\'re still standing in the main area of the castle courtyard. You were going to look around, but you forgot your sword!"
    elif CurrentRoom == "Courtyard_Main" and move[0].lower() == 'go' and move[1].lower() == 'west':
        rooms["Courtyard_Main"]["desc"] = "You\'re still standing in the main area of the castle courtyard. You were going to look around, but you forgot your sword!"
    elif CurrentRoom == "Courtyard_Main" and move[0].lower() == 'go' and move[1].lower() == 'east':
        rooms["Courtyard_Main"]["desc"] = "You\'re still standing in the main area of the castle courtyard. You were going to look around, but you forgot your sword!"
        if "sword" in equipment:
            rooms["Courtyard_Main"]["desc"] = "You\'re standing in the main area of the castle courtyard. \n  ~ North: Looks as though the entrance to the castle is up ahead. \n  ~ West: You once heard screaming coming from that direction. You can see something glistening from a nearby tree that caught fire. \n  ~ East: You see nothing but more dead foliage."

#    if CurrentRoom == "Castle_Entrance" and move[0].lower() == 'go' and move[1].lower() == 'north':
#        rooms["Courtyard_Main"]["desc"] = "You\'re still standing in the main area of the castle courtyard. You were going to look around, but you forgot your sword!"

    # Lever to open northern path to castle entrance
    if not "envitem" in rooms['Courtyard_Midwest'].keys():
        rooms["Courtyard_Main2"]["north"] = "Castle_Entrance2"

    # Hall ~ Goblin fight: Choice based
    if CurrentRoom == "Hall" and move[0].lower() == 'interact' and move[1].lower() == 'fight':
        print('''
        The goblin looks excited. Eying you up like a mountain lion noticing a deer. It pulls out an explosive from it's 
           satchel and snaps it's finger against the wick, igniting it. It throws it at you but overshot the toss as
               you rush forward for the attack. It steps back as you approach. This causes the goblin to get too 
               close to the flames, accidentally igniting one of its bombs in the satchel. Neither of you notice
                                    as the focus is primarily on the fight at hand. 
                                    
                  You here a loud explosion one moment and the next...nothingness. Your journey is at an end. 

                     ,.   (   .      )        .      "            ,.   (   .      )        .      "        
                    ("     )  )'     ,'        )  . (`     '`    ("     )  )'     ,'        )  . (`     '` 
                   .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"  .; )  ' (( (" )    ;(,     ((  (  ;)  "  )" 
                  _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '.._"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..        
                  ("     )  )'     ,'        )  . (`     '`    ("     )  )'     ,'        )  . (`     '` 
                   .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"  .; )  ' (( (" )    ;(,     ((  (  ;)  "  )" 
                  _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '.._"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..
                         
               ________    _____      _____  ___________               ____________   _________________________ 
              /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
             /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
             \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
              \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                     \/         \/         \/        \/                        \/                 \/         \/ 
                             ''')
        break

    if CurrentRoom == "Hall" and move[0].lower() == 'int' and move[1].lower() == 'fight':
        print('''
        The goblin looks excited.Eying you up like a mountain lion noticing a deer. It pulls out an explosive from it's 
           satchel and snaps it's finger against the wick, igniting it. It throws it at you but overshot the toss as
               you rush forward for the attack. It steps back as you approach. This causes the goblin to get too 
               close to the flames, accidentally igniting one of its bombs in the satchel. Neither of you notice
                                    as the focus is primarily on the fight at hand. 

                  You here a loud explosion one moment and the next...nothingness. Your journey is at an end. 

                     ,.   (   .      )        .      "            ,.   (   .      )        .      "        
                    ("     )  )'     ,'        )  . (`     '`    ("     )  )'     ,'        )  . (`     '` 
                   .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"  .; )  ' (( (" )    ;(,     ((  (  ;)  "  )" 
                  _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '.._"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..        
                  ("     )  )'     ,'        )  . (`     '`    ("     )  )'     ,'        )  . (`     '` 
                   .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"  .; )  ' (( (" )    ;(,     ((  (  ;)  "  )" 
                  _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '.._"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..

               ________    _____      _____  ___________               ____________   _________________________ 
              /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
             /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
             \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
              \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                     \/         \/         \/        \/                        \/                 \/         \/ 
                             ''')
        break

    # After goblin fight. Prelude to room description
    if CurrentRoom == "Main_Hall_South" and move[0].lower() == 'go' and move[1].lower() == 'north':
        print('\nYou decide it\'s best to run. As you turn to run you hear the goblin give off an angry screech and tosses explosives at you to halt your progress.\n  Luckily goblins have terrible aim. You run off and it dashes after you. As you both run deeper into the castle, a chandelier gives way, luckily falling onto the goblin.\nA bomb rolls out of it satchel and into the flames. Moments later, it explodes causing the hallways to collapse behind you behind you.\n  You dive into the Main Hall. Making it just in time.')

    # To use Dungeon Key (d.key) to open up Jailroom2
    if "d.key" in inventory and CurrentRoom == "Jailroom1" and move[0].lower() == 'use' and move[1].lower() == 'd.key':
        rooms[CurrentRoom] = rooms["Jailroom1a"]
        inventory.remove("d.key")
        rooms["Main_Hall_Southwest"]["down"] = "Jailroom1a"

    # Kitchen ~ Different outcomes using 'COOK' special action
    if "thigh" and "flint" and "poison" and "note" in inventory and CurrentRoom == "Kitchen" and move[0].lower() == 'int' and move[1].lower() == 'cook':
        print("\nAfter taking inspiration from the frustrated note, you get the idea to cook up a deadly treat for the beast below. You use the flint to make a small fire.\n     You douse the thigh vigorously with the poison, all the while being extra careful not let it touch you, and begin cooking. The smell of the flesh makes you slightly ill.\n   After you're done cooking, you use the remainder of the poison in case the flame may have decreased it\'s potency.\n     You place it carefully in a leather satchel you find nearby. Hopefully the beast will take the BAIT.\n\n                              BAIT was added to your inventory!")
        inventory.remove("thigh")
        inventory.remove("flint")
        inventory.remove("poison")
        inventory.remove("note")
        inventory.append("bait")
        rooms[CurrentRoom] = rooms["KitchenA"]
        rooms["Main_Hall_West"]["north"] = "KitchenA"
        rooms["Meat_Locker"]["south"] = "KitchenA"
    elif "thigh" and "flint" and "poison" and "note" in inventory and CurrentRoom == "Kitchen" and move[0].lower() == 'interact' and move[1].lower() == 'cook':
        print("\nAfter taking inspiration from the frustrated note, you get the idea to cook up a deadly treat for the beast below. You use the flint to make a small fire.\n     You douse the thigh vigorously with the poison, all the while being extra careful not let it touch you, and begin cooking. The smell of the flesh makes you slightly ill.\n   After you're done cooking, you use the remainder of the poison in case the flame may have decreased it\'s potency.\n     You place it carefully in a leather satchel you find nearby. Hopefully the beast will take the BAIT.\n\n                              BAIT was added to your inventory!")
        inventory.remove("thigh")
        inventory.remove("flint")
        inventory.remove("poison")
        inventory.remove("note")
        inventory.append("bait")
        rooms[CurrentRoom] = rooms["KitchenA"]
        rooms["Main_Hall_West"]["north"] = "KitchenA"
        rooms["Meat_Locker"]["south"] = "KitchenA"
    elif CurrentRoom == "Kitchen" and move[0].lower() == 'int' and move[1].lower() == 'cook':
        print('There\'s a spot you can cook something, but you aren\'t sure why you\'d need to.')
        rooms[CurrentRoom]['envitem'] = 'cook'
        rooms[CurrentRoom] = rooms["Kitchen"]
    elif CurrentRoom == "Kitchen" and move[0].lower() == 'interact' and move[1].lower() == 'cook':
        print('There\'s a spot you can cook something, but you aren\'t sure why you\'d need to.')
        rooms[CurrentRoom]['envitem'] = 'cook'
        rooms[CurrentRoom] = rooms["Kitchen"]

    if CurrentRoom == "Jailroom2" and move[0].lower() == 'interact' and move[1].lower() == 'sneak':
        print('''
        You attempt to sneak across To the other side.  You stick close to the wall attempting to keep distance between
           you and the beast. Unfortunately, the one thing you were never taught in all your years of training, and 
             all your battle experience was stealth. You kick a rock which begins skipping across the floor. Each
                hit echoing in the hollow chamber.  You see the beast awaken and lunge towards you with little
                       hesitation. You run for the door, but were too slow. In two bites, you're gone.  
                                                Your journey is at an end.
                                                
                                                ,
                                             ,,/( ,,,,,,,,,,___,,
                                             )b     ,,,           "`,_,
                                            /(     /                   `,
                                           L/7_/\,,|            /        \\
                                            ,`      `,  \     ,|          \\
                                             ,      /  /``````||      |\,  \__,)))
                                                   /  / |      \\\\     \  \,,,,,,/
                                                  |  /  |       \\\\   )/
                                                  \ (|  )     ,,//   /
                                                   `  _)_/     ((___/"'
                                      "`""``"````"""``````""`""```````""`"`"```""``"``"       
               ________    _____      _____  ___________               ____________   _________________________ 
              /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
             /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
             \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
              \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                     \/         \/         \/        \/                        \/                 \/         \/
               ''')

    if CurrentRoom == "Jailroom2" and move[0].lower() == 'int' and move[1].lower() == 'sneak':
        print(''' 
        You attempt to sneak across To the other side.  You stick close to the wall attempting to keep distance between
           you and the beast. Unfortunately, the one thing you were never taught in all your years of training, and 
             all your battle experience was stealth. You kick a rock which begins skipping across the floor. Each
                hit echoing in the hollow chamber.  You see the beast awaken and lunge towards you with little
                       hesitation. You run for the door, but were too slow. In two bites, you're gone.  
                                                Your journey is at an end.
                                                
                                                ,
                                             ,,/( ,,,,,,,,,,___,,
                                             )b     ,,,           "`,_,
                                            /(     /                   `,
                                           L/7_/\,,|            /        \\
                                            ,`      `,  \     ,|          \\
                                             ,      /  /``````||      |\,  \__,)))
                                                   /  / |      \\\\     \  \,,,,,,/
                                                  |  /  |       \\\\   )/
                                                  \ (|  )     ,,//   /
                                                   `  _)_/     ((___/"'
                                      "`""``"````"""``````""`""```````""`"`"```""``"``"                                                         
               ________    _____      _____  ___________               ____________   _________________________ 
              /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
             /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
             \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
              \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                     \/         \/         \/        \/                        \/                 \/         \/ 
              ''')
        break

    if CurrentRoom == "Jailroom2" and move[0].lower() == 'interact' and move[1].lower() == 'run':
        print('''   
        You decide to run.  You hesitantly start off walking, but soon enough, break into a full sprint.  You awaken the
          beast, but you were prepared. You believe that it's momentary disorientation from being woke would have given
            you time, but you were wrong. The beast lunges towards you with little hesitation. Your adrenaline kicks
                in and you sprint faster towards the door. Too bad four legs ar better than two. It catches up to 
                                and in two bites, you're gone. Your journey is at an end. ''')
                                          
        print('                                                          _|_')
        print('                                                           |')
        print('                                                       .-:\'\'\'\'\'-.')
        print('                                                    .-'    '-.')
        print('                                                 .-\'  :::::_:::::  \'-.')
        print('                                             ___/ ==:...:::-:::...:== \___')
        print('                                            /_____________________________\\')
        print('                                          \':\'-._________________________.-\'_')
        print('                                          \':::\ @-,`-[-][-^-][-]-`,-@ / _| |_')
        print('                                          \'::| .-------------------. ||_ @ _|')
        print('                                           ::|=|*    GAME OVER    *|=|\'.| |')
        print('                                           \':| |\'   ))_) )) ))_)  \'| |::.^|')
        print('                                           _:|=|\'  ((`\ (( ((     \'|=|::::::.')
        print('                                         _| || |\'        _        \'| |:::::::.')
        print('                                        |_   |=|\'15xx  _( )_  15xx\'|=|\':::::.')
        print('                                          | || |\' (   (_ ~ _)   ) \'| | \':::\'')
        print('                                          |^||=|*  )    (_)    (  *|=| \'::\'')
        print('                                             | \'-------------------\' .::::\'')
        print('                                             |_____________________.::::::\'')
        print('                                           .\'___________________.::::::''')
        print('                                           |_____________________________.::::\'\':::\'\'\'')
        print('                                         .\'_____________.::::::\'\'::::\'\'')
        print('                                                    .:::\'\'\'\' \'\'\' .\'::::\'')
        print('                                                 .:::::\'\'\':.   .:::::\'')
        print('''
               ________    _____      _____  ___________               ____________   _________________________ 
              /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
             /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
             \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
              \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                     \/         \/         \/        \/                        \/                 \/         \/ 
        ''')
        break

    if CurrentRoom == "Jailroom2" and move[0].lower() == 'int' and move[1].lower() == 'run':
        print('''   
        You decide to run.  You hesitantly start off walking, but soon enough, break into a full sprint.  You awaken the
          beast, but you were prepared. You believe that it's momentary disorientation from being woke would have given
            you time, but you were wrong. The beast lunges towards you with little hesitation. Your adrenaline kicks
                in and you sprint faster towards the door. Too bad four legs ar better than two. It catches up to 
                                and in two bites, you're gone. Your journey is at an end. ''')

        print('                                                          _|_')
        print('                                                           |')
        print('                                                       .-:\'\'\'\'\'-.')
        print('                                                    .-'    '-.')
        print('                                                 .-\'  :::::_:::::  \'-.')
        print('                                             ___/ ==:...:::-:::...:== \___')
        print('                                            /_____________________________\\')
        print('                                          \':\'-._________________________.-\'_')
        print('                                          \':::\ @-,`-[-][-^-][-]-`,-@ / _| |_')
        print('                                          \'::| .-------------------. ||_ @ _|')
        print('                                           ::|=|*    GAME OVER    *|=|\'.| |')
        print('                                           \':| |\'   ))_) )) ))_)  \'| |::.^|')
        print('                                           _:|=|\'  ((`\ (( ((     \'|=|::::::.')
        print('                                         _| || |\'        _        \'| |:::::::.')
        print('                                        |_   |=|\'15xx  _( )_  15xx\'|=|\':::::.')
        print('                                          | || |\' (   (_ ~ _)   ) \'| | \':::\'')
        print('                                          |^||=|*  )    (_)    (  *|=| \'::\'')
        print('                                             | \'-------------------\' .::::\'')
        print('                                             |_____________________.::::::\'')
        print('                                           .\'___________________.::::::''')
        print('                                           |_____________________________.::::\'\':::\'\'\'')
        print('                                         .\'_____________.::::::\'\'::::\'\'')
        print('                                                    .:::\'\'\'\' \'\'\' .\'::::\'')
        print('                                                 .:::::\'\'\':.   .:::::\'')
        print('''
               ________    _____      _____  ___________               ____________   _________________________ 
              /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
             /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
             \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
              \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                     \/         \/         \/        \/                        \/                 \/         \/ 
        ''')
        break

    if CurrentRoom == "Jailroom2" and move[0].lower() == 'interact' and move[1].lower() == 'kill':
        print('''
        You decide your best course of action would be to slay the beast while it sleeps. You are unsure if there's
        another way back, so dealing with this creature may be inevitable. You creep slowly towards it, unsheathing
          your sword as quietly as possible.  As you are about to approach, you raise your sword above your head,
           immediately ready for a downward thrust into its head once you are in striking range. As you reach a
               two pace distance from the beast, without time to react, it snaps its head forward.  In your
                surprise, you drop your sword.  The beast grabs you and raises his head. Your fate sealed,
                  you find yourself unable to move. The saliva must have a paralyzing effect. You slide
                    helplessly down its throat. Unable to move. Unable to scream. Then unable to see.
                                Finally, unable to breathe.  Your journey is at an end.           

                                                     _,.-------.,_
                                                 ,;~'             '~;,
                                               ,;                     ;,
                                              ;                         ;
                                             ,'                         ',
                                            ,;                           ;,
                                            ; ;      .           .      ; ;
                                            | ;   ______       ______   ; |
                                            |  `/~"     ~" . "~     "~\\\'  |
                                            |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
                                             |   |        }:{        |   |
                                             |   l       / | \       !   |
                                             .~  (__,.--" .^. "--.,__)  ~.
                                             |     ---;' / | \ `;---     |
                                              \__.       \/^\/       .__/
                                               V| \                 / |V
                            __                  | |T~\___!___!___/~T| |                  _____
                         .-~  ~"-.              | |`IIII_I_I_I_IIII'| |               .-~     "-.
                        /         \             |  \,III I I I III,/  |              /           Y
                       Y          ;              \   `~~~~~~~~~~'    /               i           |
                       `.   _     `._              \   .       .   /               __)         .'
                         )=~         `-.._           \.    ^    ./           _..-'~         ~"<_
                      .-~                 ~`-.._       ^~~~^~~~^       _..-'~                   ~.
                     /                          ~`-.._           _..-'~                           Y
                     {        .~"-._                  ~`-.._ .-'~                  _..-~;         ;
                      `._   _,'     ~`-.._                  ~`-.._           _..-'~     `._    _.-
                         ~~"              ~`-.._                  ~`-.._ .-'~              ~~"~
                       .----.            _..-'  ~`-.._                  ~`-.._          .-~~~~-.
                      /      `.    _..-'~             ~`-.._                  ~`-.._   (        ".
                     Y        `=--~                  _..-'  ~`-.._                  ~`-'         |
                     |                         _..-'~             ~`-.._                         ;
                     `._                 _..-'~                         ~`-.._            -._ _.'
                        "-.="      _..-'~                                     ~`-.._        ~`.
                         /        `.                                                ;          Y
                        Y           Y                                              Y           |
                        |           ;                                              `.          /
                        `.       _.'                                                 "-.____.-'
                          ~-----"
               ________    _____      _____  ___________               ____________   _________________________ 
              /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
             /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
             \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
              \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                     \/         \/         \/        \/                        \/                 \/         \/ 
               ''')
        break

    if CurrentRoom == "Jailroom2" and move[0].lower() == 'int' and move[1].lower() == 'kill':
        print('''
        You decide your best course of action would be to slay the beast while it sleeps. You are unsure if there's
        another way back, so dealing with this creature may be inevitable. You creep slowly towards it, unsheathing
          your sword as quietly as possible.  As you are about to approach, you raise your sword above your head,
           immediately ready for a downward thrust into its head once you are in striking range. As you reach a
               two pace distance from the beast, without time to react, it snaps its head forward.  In your
                surprise, you drop your sword.  The beast grabs you and raises his head. Your fate sealed,
                  you find yourself unable to move. The saliva must have a paralyzing effect. You slide
                    helplessly down its throat. Unable to move. Unable to scream. Then unable to see.
                                Finally, unable to breathe.  Your journey is at an end.           

                                                     _,.-------.,_
                                                 ,;~'             '~;,
                                               ,;                     ;,
                                              ;                         ;
                                             ,'                         ',
                                            ,;                           ;,
                                            ; ;      .           .      ; ;
                                            | ;   ______       ______   ; |
                                            |  `/~"     ~" . "~     "~\\\'  |
                                            |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
                                             |   |        }:{        |   |
                                             |   l       / | \       !   |
                                             .~  (__,.--" .^. "--.,__)  ~.
                                             |     ---;' / | \ `;---     |
                                              \__.       \/^\/       .__/
                                               V| \                 / |V
                            __                  | |T~\___!___!___/~T| |                  _____
                         .-~  ~"-.              | |`IIII_I_I_I_IIII'| |               .-~     "-.
                        /         \             |  \,III I I I III,/  |              /           Y
                       Y          ;              \   `~~~~~~~~~~'    /               i           |
                       `.   _     `._              \   .       .   /               __)         .'
                         )=~         `-.._           \.    ^    ./           _..-'~         ~"<_
                      .-~                 ~`-.._       ^~~~^~~~^       _..-'~                   ~.
                     /                          ~`-.._           _..-'~                           Y
                     {        .~"-._                  ~`-.._ .-'~                  _..-~;         ;
                      `._   _,'     ~`-.._                  ~`-.._           _..-'~     `._    _.-
                         ~~"              ~`-.._                  ~`-.._ .-'~              ~~"~
                       .----.            _..-'  ~`-.._                  ~`-.._          .-~~~~-.
                      /      `.    _..-'~             ~`-.._                  ~`-.._   (        ".
                     Y        `=--~                  _..-'  ~`-.._                  ~`-'         |
                     |                         _..-'~             ~`-.._                         ;
                     `._                 _..-'~                         ~`-.._            -._ _.'
                        "-.="      _..-'~                                     ~`-.._        ~`.
                         /        `.                                                ;          Y
                        Y           Y                                              Y           |
                        |           ;                                              `.          /
                        `.       _.'                                                 "-.____.-'
                          ~-----"
               ________    _____      _____  ___________               ____________   _________________________ 
              /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
             /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
             \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
              \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                     \/         \/         \/        \/                        \/                 \/         \/ 
               ''')
        break

    if "bait" in inventory and CurrentRoom == "Jailroom2" and move[0].lower() == 'use' and move[1].lower() == 'bait':
        print('''
        You empty the contents of the leather satchel and the poisoned bait rolls to the floor, still warm from being contained. You
         toss the warm satchel to the side and let out a loud whistle.  "By the Gods, I hope this works..." you think to yourself,
          terrified of what other outcomes may be waiting.  The beast runs towards you but stops for a moment and catches the scent
           of the cooked human flesh.  Its drools a little as it slowly walks towards the bait, as if savoring as much as it will
            savor the meal. It sniffs te bait. Once. Twice. Three times... It looks back up at you, as if knowing what you did
             but compelled to eat. It swallows it like a pill. There one moment gone the next. The same can be said about the
              beast as the poison works almost instantaneously. You can't be sure if it's dead or paralyzed. You immediately
               thrust your sword into its skull the moment it stopped moving. It's time to continue onward.''')
        rooms[CurrentRoom] = rooms["Jailroom2a"]
        inventory.remove("bait")
        rooms["Jailroom1a"]["north"] = "Jailroom2a"
        rooms["Jailroom3"]["south"] = "Jailroom2a"

# Main_Hall_Center ~ All outcomes using Multiple ORBs
    # If player has both orbs before using them
    if "p.orb" and "g.orb" in inventory and CurrentRoom == "Main_Hall_Center" and move[0].lower() == 'use' and move[1].lower() == 'p.orb':
        del rooms[CurrentRoom]['purple']
        rooms[CurrentRoom] = rooms["Main_Hall_Center1"]
        inventory.remove("p.orb")
        rooms["Main_Hall_South"]["north"] = "Main_Hall_Center1"
        rooms["Main_Hall_West"]["east"] = "Main_Hall_Center1"
        rooms["Main_Hall_East"]["west"] = "Main_Hall_Center1"
    elif not "purple" in rooms['Main_Hall_Center'].keys() and "g.orb" in inventory and CurrentRoom == "Main_Hall_Center" and move[0].lower() == 'use' and move[1].lower() == 'g.orb':
        rooms[CurrentRoom] = rooms["Main_Hall_Center5"]
        inventory.remove("g.orb")
        rooms["Main_Hall_South"]["north"] = "Main_Hall_Center5"
        rooms["Main_Hall_West"]["east"] = "Main_Hall_Center5"
        rooms["Main_Hall_East"]["west"] = "Main_Hall_Center5"
    if "p.orb" in inventory and "g.orb" in inventory and CurrentRoom == "Main_Hall_Center" and move[0].lower() == 'use' and move[1].lower() == 'g.orb':
        del rooms[CurrentRoom]['green']
        rooms[CurrentRoom] = rooms["Main_Hall_Center2"]
        inventory.remove("g.orb")
        rooms["Main_Hall_South"]["north"] = "Main_Hall_Center2"
        rooms["Main_Hall_West"]["east"] = "Main_Hall_Center2"
        rooms["Main_Hall_East"]["west"] = "Main_Hall_Center2"
    elif not "green" in rooms['Main_Hall_Center'].keys() and "p.orb" in inventory and CurrentRoom == "Main_Hall_Center" and move[0].lower() == 'use' and move[1].lower() == 'p.orb':
        rooms[CurrentRoom] = rooms["Main_Hall_Center5"]
        inventory.remove("p.orb")
        rooms["Main_Hall_South"]["north"] = "Main_Hall_Center5"
        rooms["Main_Hall_West"]["east"] = "Main_Hall_Center5"
        rooms["Main_Hall_East"]["west"] = "Main_Hall_Center5"

    # If Grab single ORB and use them individually
    if "p.orb" in inventory and CurrentRoom == "Main_Hall_Center" and move[0].lower() == 'use' and move[1].lower() == 'p.orb':
        del rooms[CurrentRoom]['purple']
        rooms[CurrentRoom] = rooms["Main_Hall_Center3"]
        inventory.remove("p.orb")
        rooms["Main_Hall_South"]["north"] = "Main_Hall_Center3"
        rooms["Main_Hall_West"]["east"] = "Main_Hall_Center3"
        rooms["Main_Hall_East"]["west"] = "Main_Hall_Center3"
    elif not "purple" in rooms['Main_Hall_Center'].keys() and "g.orb" in inventory and CurrentRoom == "Main_Hall_Center3" and move[0].lower() == 'use' and move[1].lower() == 'g.orb':
        rooms[CurrentRoom] = rooms["Main_Hall_Center5"]
        inventory.remove("g.orb")
        rooms["Main_Hall_South"]["north"] = "Main_Hall_Center5"
        rooms["Main_Hall_West"]["east"] = "Main_Hall_Center5"
        rooms["Main_Hall_East"]["west"] = "Main_Hall_Center5"
    if "g.orb" in inventory and CurrentRoom == "Main_Hall_Center" and move[0].lower() == 'use' and move[1].lower() == 'g.orb':
        del rooms[CurrentRoom]['green']
        rooms[CurrentRoom] = rooms["Main_Hall_Center4"]
        inventory.remove("g.orb")
        rooms["Main_Hall_South"]["north"] = "Main_Hall_Center4"
        rooms["Main_Hall_West"]["east"] = "Main_Hall_Center4"
        rooms["Main_Hall_East"]["west"] = "Main_Hall_Center4"
    elif not "green" in rooms['Main_Hall_Center'].keys() and "p.orb" in inventory and CurrentRoom == "Main_Hall_Center4" and move[0].lower() == 'use' and move[1].lower() == 'p.orb':
        rooms[CurrentRoom] = rooms["Main_Hall_Center5"]
        inventory.remove("p.orb")
        rooms["Main_Hall_South"]["north"] = "Main_Hall_Center5"
        rooms["Main_Hall_West"]["east"] = "Main_Hall_Center5"
        rooms["Main_Hall_East"]["west"] = "Main_Hall_Center5"

    # Use Lockpick to get to Jailroom5
    if "lockpick" in inventory and CurrentRoom == "Jailroom4" and move[0].lower() == 'use' and move[1].lower() == 'lockpick':
        rooms[CurrentRoom] = rooms["Jailroom4a"]
        inventory.remove("lockpick")
        rooms["Jailroom3"]["north"] = "Jailroom4a"

    # Jailroom4 - Remove duplicate Old Whip item
    if CurrentRoom == "Jailroom4" and move[0].lower() == 'get' and move[1].lower() == 'oldwhip':
        del rooms['Jailroom4a']['invitem']
        del rooms['Jailroom4b']['invitem']
        del rooms['Jailroom4c']['invitem']
        del rooms['Jailroom4d']['invitem']
    elif CurrentRoom == "Jailroom4a" and move[0].lower() == 'get' and move[1].lower() == 'oldwhip':
        del rooms['Jailroom4']['invitem']
        del rooms['Jailroom4b']['invitem']
        del rooms['Jailroom4c']['invitem']
        del rooms['Jailroom4d']['invitem']
    elif CurrentRoom == "Jailroom4b" and move[0].lower() == 'get' and move[1].lower() == 'oldwhip':
        del rooms['Jailroom4']['invitem']
        del rooms['Jailroom4a']['invitem']
        del rooms['Jailroom4c']['invitem']
        del rooms['Jailroom4d']['invitem']
    elif CurrentRoom == "Jailroom4c" and move[0].lower() == 'get' and move[1].lower() == 'oldwhip':
        del rooms['Jailroom4']['invitem']
        del rooms['Jailroom4a']['invitem']
        del rooms['Jailroom4b']['invitem']
        del rooms['Jailroom4d']['invitem']
    elif CurrentRoom == "Jailroom4d" and move[0].lower() == 'get' and move[1].lower() == 'oldwhip':
        del rooms['Jailroom4']['invitem']
        del rooms['Jailroom4a']['invitem']
        del rooms['Jailroom4b']['invitem']
        del rooms['Jailroom4c']['invitem']

    # Jailroom5 - The poor bastard options: Story
    if CurrentRoom == "Jailroom5" and move[0].lower() == 'mercy':
        print('''
        Although you feel no satisfaction from this, you believe mercy is the best option given the situation. You line up your sword, close your eyes, and whisper an
         inaudible prayer as you thrust your sword into the poor bastard's chest.''')
        rooms[CurrentRoom] = rooms["Jailroom5a"]

    if CurrentRoom == "Jailroom5b" and move[0].lower() == 'mercy':
        print('''
        Although you feel no satisfaction from this, you believe mercy is the best option given the situation. You line up your sword, close your eyes, and whisper an
         inaudible prayer as you thrust your sword into the poor bastard's chest.''')
        rooms[CurrentRoom] = rooms["Jailroom4b"]

    if CurrentRoom == "Jailroom5" and move[0].lower() == 'get' and move[1].lower() == 'blizzard':
        del rooms['Jailroom5a']['invitem']
        del rooms['Jailroom5b']['invitem']
    elif CurrentRoom == "Jailroom5a" and move[0].lower() == 'get' and move[1].lower() == 'blizzard':
        del rooms['Jailroom5']['invitem']
        del rooms['Jailroom5b']['invitem']
    elif CurrentRoom == "Jailroom5b" and move[0].lower() == 'get' and move[1].lower() == 'blizzard':
        del rooms['Jailroom5']['invitem']
        del rooms['Jailroom5a']['invitem']
    if CurrentRoom == "Jailroom5" and move[0].lower() == 'equip' and move[1].lower() == 'breastplate':
        del rooms['Jailroom5a']['eqitem']
        del rooms['Jailroom5b']['eqitem']
    elif CurrentRoom == "Jailroom5a" and move[0].lower() == 'equip' and move[1].lower() == 'breastplate':
        del rooms['Jailroom5']['eqitem']
        del rooms['Jailroom5b']['eqitem']
    elif CurrentRoom == "Jailroom5b" and move[0].lower() == 'equip' and move[1].lower() == 'breastplate':
        del rooms['Jailroom5']['eqitem']
        del rooms['Jailroom5a']['eqitem']

    # Balcony in western Tower if monster goes unchecked
    if "envitem" in rooms['West1_Main'].keys() and CurrentRoom == "West1_South":
        print('''
        While you stood on the balcony, taking in the view and having a moment of solace, the monster clad in armor found
            an opening to attack! The monster shoulder charged you! It crashed into you, hitting you in the back and
                        knocking you over the balcony. Your wish to escape the castle had come true! 
                                           Your journey has come to an end.

                                                                                              
                                                                                              
                                    ║                                         ║                   
                                    ║             ║             ║             ║                   
                                    ║             ║             ║             ║                   
                                    ║             ║             ║             ║                   
                                    ║             ║             ║             ║                       
                                    ║             ║             ║             ║                   
                                    ║             ║             ║  M          ║  
                        *SPLAT*                 M ║               MMM   M
                                                M              MMMMM   MM           M
                               M       M       MMMM         MMMMMM    MMMMM       MMM
                                MMM   MMM     MMMMMMM  WMMMMMMMMM    MMMMMM   MMMMMM
                                 MMM MMMMMM  MMMMMMMM MMMMMMMMMMM  MWMMMMMM MMMMMM
                             MM  MMMMMMMWWM MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   MM
                             MMMM MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM MMMM
                           M   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                           MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                             MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                               MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
             
               ________    _____      _____  ___________               ____________   _________________________ 
              /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
             /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
             \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
              \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                     \/         \/         \/        \/                        \/                 \/         \/              
        ''')
        break

    # West Tower Treasure Room
    if CurrentRoom == "West2_Treasure" and "blizzard" in inventory and move[0].lower() == 'get' and move[1].lower() == 'p.orb':
        CurrentRoom = 'West2_Treasure3'
        rooms["West2_Main"]["north"] = "West2_Treasure4"
    elif CurrentRoom == "West2_Treasure" and move[0].lower() == 'get' and move[1].lower() == 'p.orb':
        CurrentRoom = 'West2_Treasure2'

    if CurrentRoom == 'West2_Treasure2' and move[0].lower() == 'interact' and move[1].lower() == 'run':
        print('''
        You attempt to make a run for it. There is no discernible way you're able to kill a creature made
         of fire with a sword! You bolt out the room. However, the purple orb you're carrying is getting
           hotter and hotter until it ignites. The flame quickly you. The last thing you do is let out
             one agonizing scream before falling to the ground. You continue to burn until only bone
                                      remains. Your journey has come to an end.
                                           .            )        )
                                                    (  (|              .
                                                )   )\/ ( ( (
                                        *  (   ((  /     ))\))  (  )    )
                                      (     \   )\(          |  ))( )  (|
                                      >)     ))/   |          )/  \((  ) \\
                                      (     (      .        -.     V )/   )(    (
                                       \   /     .   \            .       \))   ))
                                         )(      (  | |   )            .    (  /
                                        )(    ,'))     \ /          \( `.    )
                                        (\>  ,'/__      ))            __`.  /
                                       ( \   | /  ___   ( \/     ___   \ | ( (
                                        \.)  |/  /   \__      __/   \   \|  ))
                                       .  \. |>  \      | __ |      /   <|  /
                                            )/    \____/ :..: \____/     \ <
                                     )   \ (|__  .      / ;: \          __| )  (
                                    ((    )\)  ~--_     --  --      _--~    /  ))
                                     \    (    |  ||               ||  |   (  /
                                           \.  |  ||_             _||  |  /
                                             > :  |  ~V+-I_I_I-+V~  |  : (.
                                            (  \:  T\   _     _   /T  : ./
                                             \  :    T^T T-+-T T^T    ;<
                                              \..`_       -+-       _'  )
                                                 . `--=.._____..=--'. ./    
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/          
        ''')
        break

    if CurrentRoom == 'West2_Treasure2' and move[0].lower() == 'int' and move[1].lower() == 'run':
        print('''
        You attempt to make a run for it. There is no discernible way you're able to kill a creature made
         of fire with a sword! You bolt out the room. However, the purple orb you're carrying is getting
           hotter and hotter until it ignites. The flame quickly you. The last thing you do is let out
             one agonizing scream before falling to the ground. You continue to burn until only bone
                                      remains. Your journey has come to an end.
                                           .            )        )
                                                    (  (|              .
                                                )   )\/ ( ( (
                                        *  (   ((  /     ))\))  (  )    )
                                      (     \   )\(          |  ))( )  (|
                                      >)     ))/   |          )/  \((  ) \\
                                      (     (      .        -.     V )/   )(    (
                                       \   /     .   \            .       \))   ))
                                         )(      (  | |   )            .    (  /
                                        )(    ,'))     \ /          \( `.    )
                                        (\>  ,'/__      ))            __`.  /
                                       ( \   | /  ___   ( \/     ___   \ | ( (
                                        \.)  |/  /   \__      __/   \   \|  ))
                                       .  \. |>  \      | __ |      /   <|  /
                                            )/    \____/ :..: \____/     \ <
                                     )   \ (|__  .      / ;: \          __| )  (
                                    ((    )\)  ~--_     --  --      _--~    /  ))
                                     \    (    |  ||               ||  |   (  /
                                           \.  |  ||_             _||  |  /
                                             > :  |  ~V+-I_I_I-+V~  |  : (.
                                            (  \:  T\   _     _   /T  : ./
                                             \  :    T^T T-+-T T^T    ;<
                                              \..`_       -+-       _'  )
                                                 . `--=.._____..=--'. ./    
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/          
        ''')
        break

    if CurrentRoom == 'West2_Treasure2' and move[0].lower() == 'interact' and move[1].lower() == 'fight':
        print('''
        Real knights don't run! You charge straight at it, sword drawn. It still gives you that same puzzled "look", making no attempt to defend itself.
         "HYYAAAGHH!!" You shout as you slash at what would be a stomach on any normal man. You don't even have to turn around to know that your attack
           was infective. You still feel the heat emanating off the beast. You wait for a counterattack, but nothing comes. You turn around to to see
            it curiously "looking" back at you. It raises one of its arms as the creature begins to shine brighter. You were enthralled at the sight
              for a moment and that moment was all it took. It set you ablaze and there's nothing you can do. Your final moments are spent staring
                at the flame creature before it snuffs itself out and disappears as the room fades to darkness. Your journey has come to an end.  

              .7
            .'/
           / /
          / /
         / /
        / /
       / /
      / /                                                       
     / /                                                        
    / /                                                                     ________   ____ ____________   ___ ___ 
  __|/                                                                      \_____  \ |    |   \_   ___ \ /   |   \      
,-\__\\                                                                       /   |   \|    |   /    \  \//    ~    \    
|f-"Y\|                                                                     /    |    \    |  /\     \___\    Y    / 
\()7L/                                                           /\  /\  /\ \_______  /______/  \______  /\___|_  / /\  /\  /\ 
 cgD                            __ _                             \/  \/  \/         \/                 \/       \/  \/  \/  \/
 |\(                          .'  Y '>,
  \ \                        / _   _   \\
   \\\\\                       )(_) (_)(|}
    \\\\\                      {  4A   } /
     \\\\\                      \\uLuJJ/\l
      \\\\\                     |3    p)/
       \\\\\___ __________      /nnm_n//
       c7___-__,__-)\,__)(".  \_>-<_/D
                  //V     \_"-._.__G G_c__.-__<"/ ( \\
                         <"-._>__-,G_.___)\   \\7\\
                        ("-.__.| \\"<.__.-" )   \ \\
                        |"-.__"\  |"-.__.-".\   \ \\
                        ("-.__"". \\"-.__.-".|    \_\\
                        \\"-.__""|!|"-.__.-".)     \ \\
                          "-.__""\_|"-.__.-"./      \ l
                          ".__""">G>-.__.-">       .--,_

          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/          
        ''')
        break

    if CurrentRoom == 'West2_Treasure2' and move[0].lower() == 'int' and move[1].lower() == 'fight':
        print('''
        Real knights don't run! You charge straight at it, sword drawn. It still gives you that same puzzled "look", making no attempt to defend itself.
         "HYYAAAGHH!!" You shout as you slash at what would be a stomach on any normal man. You don't even have to turn around to know that your attack
           was infective. You still feel the heat emanating off the beast. You wait for a counterattack, but nothing comes. You turn around to to see
            it curiously "looking" back at you. It raises one of its arms as the creature begins to shine brighter. You were enthralled at the sight
              for a moment and that moment was all it took. It set you ablaze and there's nothing you can do. Your final moments are spent staring
                at the flame creature before it snuffs itself out and disappears as the room fades to darkness. Your journey has come to an end.  

              .7
            .'/
           / /
          / /
         / /
        / /
       / /
      / /                                                       
     / /                                                        
    / /                                                                     ________   ____ ____________   ___ ___ 
  __|/                                                                      \_____  \ |    |   \_   ___ \ /   |   \      
,-\__\\                                                                       /   |   \|    |   /    \  \//    ~    \    
|f-"Y\|                                                                     /    |    \    |  /\     \___\    Y    / 
\()7L/                                                           /\  /\  /\ \_______  /______/  \______  /\___|_  / /\  /\  /\ 
 cgD                            __ _                             \/  \/  \/         \/                 \/       \/  \/  \/  \/
 |\(                          .'  Y '>,
  \ \                        / _   _   \\
   \\\\\                       )(_) (_)(|}
    \\\\\                      {  4A   } /
     \\\\\                      \\uLuJJ/\l
      \\\\\                     |3    p)/
       \\\\\___ __________      /nnm_n//
       c7___-__,__-)\,__)(".  \_>-<_/D
                  //V     \_"-._.__G G_c__.-__<"/ ( \\
                         <"-._>__-,G_.___)\   \\7\\
                        ("-.__.| \\"<.__.-" )   \ \\
                        |"-.__"\  |"-.__.-".\   \ \\
                        ("-.__"". \\"-.__.-".|    \_\\
                        \\"-.__""|!|"-.__.-".)     \ \\
                         "-.__""\_|"-.__.-"./      \ l
                          ".__""">G>-.__.-">       .--,_
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/          
                    ''')
        break

    if CurrentRoom == 'West2_Treasure3' and move[0].lower() == 'interact' and move[1].lower() == 'run':
        print('''
        You attempt to make a run for it. There is no discernible way you're able to kill a creature made
         of fire with a sword! You bolt out the room. However, the purple orb you're carrying is getting
           hotter and hotter until it ignites. The flame quickly you. The last thing you do is let out
             one agonizing scream before falling to the ground. You continue to burn until only bone
                                      remains. Your journey has come to an end.
                                           .            )        )
                                                    (  (|              .
                                                )   )\/ ( ( (
                                        *  (   ((  /     ))\))  (  )    )
                                      (     \   )\(          |  ))( )  (|
                                      >)     ))/   |          )/  \((  ) \\
                                      (     (      .        -.     V )/   )(    (
                                       \   /     .   \            .       \))   ))
                                         )(      (  | |   )            .    (  /
                                        )(    ,'))     \ /          \( `.    )
                                        (\>  ,'/__      ))            __`.  /
                                       ( \   | /  ___   ( \/     ___   \ | ( (
                                        \.)  |/  /   \__      __/   \   \|  ))
                                       .  \. |>  \      | __ |      /   <|  /
                                            )/    \____/ :..: \____/     \ <
                                     )   \ (|__  .      / ;: \          __| )  (
                                    ((    )\)  ~--_     --  --      _--~    /  ))
                                     \    (    |  ||               ||  |   (  /
                                           \.  |  ||_             _||  |  /
                                             > :  |  ~V+-I_I_I-+V~  |  : (.
                                            (  \:  T\   _     _   /T  : ./
                                             \  :    T^T T-+-T T^T    ;<
                                              \..`_       -+-       _'  )
                                                 . `--=.._____..=--'. ./    
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/          
        ''')
        break

    if CurrentRoom == 'West2_Treasure3' and move[0].lower() == 'int' and move[1].lower() == 'run':
        print('''
        You attempt to make a run for it. There is no discernible way you're able to kill a creature made
         of fire with a sword! You bolt out the room. However, the purple orb you're carrying is getting
           hotter and hotter until it ignites. The flame quickly you. The last thing you do is let out
             one agonizing scream before falling to the ground. You continue to burn until only bone
                                      remains. Your journey has come to an end.
                                           .            )        )
                                                    (  (|              .
                                                )   )\/ ( ( (
                                        *  (   ((  /     ))\))  (  )    )
                                      (     \   )\(          |  ))( )  (|
                                      >)     ))/   |          )/  \((  ) \\
                                      (     (      .        -.     V )/   )(    (
                                       \   /     .   \            .       \))   ))
                                         )(      (  | |   )            .    (  /
                                        )(    ,'))     \ /          \( `.    )
                                        (\>  ,'/__      ))            __`.  /
                                       ( \   | /  ___   ( \/     ___   \ | ( (
                                        \.)  |/  /   \__      __/   \   \|  ))
                                       .  \. |>  \      | __ |      /   <|  /
                                            )/    \____/ :..: \____/     \ <
                                     )   \ (|__  .      / ;: \          __| )  (
                                    ((    )\)  ~--_     --  --      _--~    /  ))
                                     \    (    |  ||               ||  |   (  /
                                           \.  |  ||_             _||  |  /
                                             > :  |  ~V+-I_I_I-+V~  |  : (.
                                            (  \:  T\   _     _   /T  : ./
                                             \  :    T^T T-+-T T^T    ;<
                                              \..`_       -+-       _'  )
                                                 . `--=.._____..=--'. ./    
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/          
        ''')
        break

    if CurrentRoom == 'West2_Treasure3' and move[0].lower() == 'interact' and move[1].lower() == 'fight':
        print('''
        Real knights don't run! You charge straight at it, sword drawn. It still gives you that same puzzled "look", making no attempt to defend itself.
         "HYYAAAGHH!!" You shout as you slash at what would be a stomach on any normal man. You don't even have to turn around to know that your attack
           was infective. You still feel the heat emanating off the beast. You wait for a counterattack, but nothing comes. You turn around to to see
            it curiously "looking" back at you. It raises one of its arms as the creature begins to shine brighter. You were enthralled at the sight
              for a moment and that moment was all it took. It set you ablaze and there's nothing you can do. Your final moments are spent staring
                at the flame creature before it snuffs itself out and disappears as the room fades to darkness. Your journey has come to an end.  

              .7
            .'/
           / /
          / /
         / /
        / /
       / /
      / /                                                       
     / /                                                        
    / /                                                                     ________   ____ ____________   ___ ___ 
  __|/                                                                      \_____  \ |    |   \_   ___ \ /   |   \      
,-\__\\                                                                       /   |   \|    |   /    \  \//    ~    \    
|f-"Y\|                                                                     /    |    \    |  /\     \___\    Y    / 
\()7L/                                                           /\  /\  /\ \_______  /______/  \______  /\___|_  / /\  /\  /\ 
 cgD                            __ _                             \/  \/  \/         \/                 \/       \/  \/  \/  \/
 |\(                          .'  Y '>,
  \ \                        / _   _   \\
   \\\\\                       )(_) (_)(|}
    \\\\\                      {  4A   } /
     \\\\\                      \\uLuJJ/\l
      \\\\\                     |3    p)/
       \\\\\___ __________      /nnm_n//
       c7___-__,__-)\,__)(".  \_>-<_/D
                  //V     \_"-._.__G G_c__.-__<"/ ( \\
                         <"-._>__-,G_.___)\   \\7\\
                        ("-.__.| \\"<.__.-" )   \ \\
                        |"-.__"\  |"-.__.-".\   \ \\
                        ("-.__"". \\"-.__.-".|    \_\\
                        \\"-.__""|!|"-.__.-".)     \ \\
                          "-.__""\_|"-.__.-"./      \ l
                          ".__""">G>-.__.-">       .--,_

          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/          
        ''')
        break

    if CurrentRoom == 'West2_Treasure3' and move[0].lower() == 'int' and move[1].lower() == 'fight':
        print('''
        Real knights don't run! You charge straight at it, sword drawn. It still gives you that same puzzled "look", making no attempt to defend itself.
         "HYYAAAGHH!!" You shout as you slash at what would be a stomach on any normal man. You don't even have to turn around to know that your attack
           was infective. You still feel the heat emanating off the beast. You wait for a counterattack, but nothing comes. You turn around to to see
            it curiously "looking" back at you. It raises one of its arms as the creature begins to shine brighter. You were enthralled at the sight
              for a moment and that moment was all it took. It set you ablaze and there's nothing you can do. Your final moments are spent staring
                at the flame creature before it snuffs itself out and disappears as the room fades to darkness. Your journey has come to an end.  

              .7
            .'/
           / /
          / /
         / /
        / /
       / /
      / /                                                       
     / /                                                        
    / /                                                                     ________   ____ ____________   ___ ___ 
  __|/                                                                      \_____  \ |    |   \_   ___ \ /   |   \      
,-\__\\                                                                       /   |   \|    |   /    \  \//    ~    \    
|f-"Y\|                                                                     /    |    \    |  /\     \___\    Y    / 
\()7L/                                                           /\  /\  /\ \_______  /______/  \______  /\___|_  / /\  /\  /\ 
 cgD                            __ _                             \/  \/  \/         \/                 \/       \/  \/  \/  \/
 |\(                          .'  Y '>,
  \ \                        / _   _   \\
   \\\\\                       )(_) (_)(|}
    \\\\\                      {  4A   } /
     \\\\\                      \\uLuJJ/\l
      \\\\\                     |3    p)/
       \\\\\___ __________      /nnm_n//
       c7___-__,__-)\,__)(".  \_>-<_/D
                  //V     \_"-._.__G G_c__.-__<"/ ( \\
                         <"-._>__-,G_.___)\   \\7\\
                        ("-.__.| \\"<.__.-" )   \ \\
                        |"-.__"\  |"-.__.-".\   \ \\
                        ("-.__"". \\"-.__.-".|    \_\\
                        \\"-.__""|!|"-.__.-".)     \ \\
                         "-.__""\_|"-.__.-"./      \ l
                          ".__""">G>-.__.-">       .--,_
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/          
                    ''')
        break

    if CurrentRoom == 'West2_Treasure3' and move[0].lower() == 'use' and move[1].lower() == 'blizzard':
        CurrentRoom = 'West2_Treasure4'
        inventory.remove("blizzard")
        print('''
        You grab the blizzard scroll, remembering the icy chill in the room where the poor bastard is. You read from the scroll, trying your
          best to say the incantation correctly. The flame creature still stares at you, unmoving. You finish the incantation and you feel
             the room getting colder. The familiar chill from earlier returning. Unable to maintain its form, the flame creature begins 
                 to shrink until all that remained was a momentary puff of smoke. THe purple or in your pocket also begins to cool.
        ''')

    # East Tower mirror puzzle
    if CurrentRoom == 'East2_Duality' and move[0].lower() == 'use' and move[1].lower() == 'crystal':
        CurrentRoom = 'East2_Duality2'
        inventory.remove("crystal")
        print('''
        You hold the CRYSTAL against the northern wall. The reflections seemingly merging into one. The CRYSTAL sinks into the wall as it begins
         to waver. You poke the wall in confusion. Your finger sinks in, leaving a rippling effect that spreads to all ends of the wall.        
        ''')

    # Mirror room outcomes
    if CurrentRoom == 'East2_Treasure' and "fire" not in inventory and move[0].lower() == 'go' and move[1].lower() == 'north':
        print('''
        You walk through the mirror and are now standing in a mirror room almost completely similar to the one you were just in. There is no visible door.
          Instead, another mirror wall is adjacent to your position.  You walk to the wall and you see your reflection seems as though it is walking to
              you too....Wait! It IS walking towards you! You stop. So does it. You raise your left hand and it simultaneously raises its right. You
               aren't sure what this means, but you know it can't be good. You take out your sword, which was sheathed on your left hip, holding it
                in your right hand.  You're ready for a fight. It unsheathes it's sword from it's right hip and grasps its sword in its left hand.
                It's eyes are different colors. One a dark red, the other illuminating a dark green light. After a long fight neither of you have
                 a mark on you. You think to just escape but theres no way out. You panic looking for a door and your doppelganger does the same.
                            You both try kicking the walls, slashing them, punching them. Nothing. You're trapped. There is no way out. 
                                                              Your journey has come to an end. 
                            ________    _____      _____  ___________               ____________   _________________________ 
                           /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
                          /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
                          \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
                           \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                                  \/         \/         \/        \/                        \/                 \/         \/                                                                      
                                                            ''')
        break

    if CurrentRoom == 'East2_Treasure' and move[0].lower() == 'use' and move[1].lower() == 'fire':
        CurrentRoom = 'East2_Treasure2'
        inventory.remove("fire")
        print('''
        You pull out the fire scroll and begin reading the incantation written on it. Your doppelganger does the same but only mouths the spell. You can feel
        sweat start rolling down your forehead, but this is no time to stop now. If this doesn't work, He could burn you too! As you finish reciting the last
         word, the scroll transforms into a ball of fire you are able to hold.  You launch the ball at your mirror self while he in turn pathetically tosses
          a sheet of parchment at you. Direct hit! Your doppelganger begins to burn. But it doesn't seem to notice. It simply stands there, mirroring 
            whatever action you're doing. You wonder if it even feels pain.  If it's even real... As the last of the flames go out, a light emerges
              from the wall as if was at the exit of a dark tunnel. It must be the way out. Nothing remains of the doppelganger except for a pile
                                                            of ash and a green orb. WAIT! A what?!      
                ''')

    # Main_Hall_North for easter egg
    if CurrentRoom == 'Main_Hall_North' and "oldwhip" in inventory and move[0].lower() == 'use' and move[1].lower() == 'oldwhip':
        CurrentRoom = 'Main_Hall_North2'
        inventory.remove("oldwhip")
        print('You decide to use the whip on the wall for some reason. Your old school instincts of exploring a castle of monsters kicks in.')

    # All scenarios for the Tepes/Tepes2 rooms
    if not "invitem" in rooms['Tepes'].keys():
        rooms["Tepes"] = rooms["Tepes2"]
        rooms["Main_Hall_North"]["north"] = "Tepes2"
        rooms["Main_Hall_Center5"]["north"] = "Main_Hall_North3"
        rooms["Main_Tower1"]["down"] = "Main_Hall_North3"
    elif CurrentRoom == "Tepes" and "belmont" in rooms["Tepes"]["invitem"] and "rope" in rooms["Tepes"]["invitem"] and "p.chop" not in rooms["Tepes"]["invitem"]:
        rooms["Tepes"]["item"] = "You grabbed the pork chop! Don\'t forget the BELMONT scroll and your ROPE!"
    elif CurrentRoom == "Tepes" and "rope" in rooms["Tepes"]["invitem"] and "belmont" not in rooms["Tepes"]["invitem"] and "p.chop" not in rooms["Tepes"]["invitem"]:
        rooms["Tepes"]["item"] = "The ROPE remains."
    elif CurrentRoom == "Tepes" and "belmont" in rooms["Tepes"]["invitem"] and "rope" not in rooms["Tepes"]["invitem"] and "p.chop" not in rooms["Tepes"]["invitem"]:
        rooms["Tepes"]["item"] = "All that\'s left is the BELMONT scroll."
    elif CurrentRoom == "Tepes" and "p.chop" in rooms["Tepes"]["invitem"] and "rope" in rooms["Tepes"]["invitem"] and "belmont" not in rooms["Tepes"]["invitem"]:
        rooms["Tepes"]["item"] = "You grabbed the scroll first! Don\'t forget the P.CHOP! and your ROPE!"
    elif CurrentRoom == "Tepes" and "rope" in rooms["Tepes"]["invitem"] and "p.chop" not in rooms["Tepes"]["invitem"] and "belmont" not in rooms["Tepes"]["invitem"]:
        rooms["Tepes"]["item"] = "All that\'s left is the ROPE."
    elif CurrentRoom == "Tepes" and "p.chop" in rooms["Tepes"]["invitem"] and "rope" not in rooms["Tepes"]["invitem"] and "belmont" not in rooms["Tepes"]["invitem"]:
        rooms["Tepes"]["item"] = "All that\'s left is the P.CHOP."
    elif CurrentRoom == "Tepes" and "p.chop" in rooms["Tepes"]["invitem"] and "belmont" in rooms["Tepes"]["invitem"] and "rope" not in rooms["Tepes"]["invitem"]:
        rooms["Tepes"]["item"] = "You took the rope! Don\'t forget the BELMONT scroll and P.CHOP!"
    elif CurrentRoom == "Tepes" and "belmont" in rooms["Tepes"]["invitem"] and "p.chop" not in rooms["Tepes"]["invitem"] and "rope" not in rooms["Tepes"]["invitem"]:
        rooms["Tepes"]["item"] = "All that\'s left is the BELMONT scroll."
    elif CurrentRoom == "Tepes" and "p.chop" in rooms["Tepes"]["invitem"] and "belmont" not in rooms["Tepes"]["invitem"] and "rope" not in rooms["Tepes"]["invitem"]:
        rooms["Tepes"]["item"] = "All that\'s left is the P.CHOP."



    if CurrentRoom == "Tepes2" and "sword" in equipment:
        print('''
                                                       ###                                  
                                                      #@@@#                                 
                                                     ###  #                                 
                                                  ######@ #                                 
                                                 #@#  #@######         THANK YOU         ##     
                                                #@ @###  #@   ##      FOR PLAYING       #  #    
                                                # @###@@ ###@@  #@ #@ #@#@ #@ #@# #@ #@ #@ #    
                                                #  @ #@@######@ ############################      
                                                #@ @ #@##     ##                            
                                                 ####@##                                    
                                                 ######                                     
                                                #@   #                                      
                                                #   ##                                      
                                               #@  # @#                                     
                                               #@##@@ #                                     
                                                ####@@ #                                    
                                                #@#### #                                    
                                               ##@# #@ #                                    
                                             ##@@#  ## #                                    
                                            ##@##   #@##                                    
                                            #@#     #@@#                                    
                                            ##@#    #@ ##                                   
                                              ##@#  #@@   #                                 
                              ##############################################################
                              ##          ##          ##          ##          ##          ##
                              ##@@@@@@@@@@##@@@@@@@@@@##@@@@@@@@@@##@@@@@@@@@@##@@@@@@@@@@##
        ''')

    # Black Mage "Fight"
    if CurrentRoom == "Main_Tower_F2R2" and move[0].lower() == 'commence':
        CurrentRoom = 'BM_Battlea'
        print('''
        
                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |  "Oh? Another one? How many more of you rats are            \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |   scurrying about? Oh... no matter....                       \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |   You did well to make it this far. I do commend you,        /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |   but you will go no further!!!"                            /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
             ____          ║          ____                                    ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
            |___ \         ║         |___ \\                                  ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
              __) |        ║           __) |                                  ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
             |__ <         ║          |__ <                                 ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
             ___) |        ║          ___) |                                ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
            |____/         ║         |____/                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlea" and move[0].lower() == 'counter':
        CurrentRoom = 'BM_Battlel'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |   "Your luck's run out."                                     \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║          ____                                    ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             |__ \         ║         |___ \\                                  ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
                ) |        ║           __) |                                  ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               / /         ║          |__ <                                 ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
              / /_         ║          ___) |                                ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             |____|        ║         |____/                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlel" and move[0].lower() == 'endure':
        CurrentRoom = 'BM_Battlek'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |   "Ha ha ha ha... Is this what passes for a knight           \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |     these days?  Pathetic.                                    >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║          ____                                    ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║         |___ \\                                  ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           __) |                                  ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║          |__ <                                 ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║          ___) |                                ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║         |____/                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlek" and move[0].lower() == 'possum':
        CurrentRoom = 'BM_Battleq'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |   "There are things floating in the latrine more            \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |     terrifying than you.                                     \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |    My master does not entertain the likes of filth."         /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║          ____                                    ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             / _ \         ║         |___ \\                                  ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║           __) |                                  ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║          |__ <                                 ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
            | |_| |        ║          ___) |                                ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             \___/         ║         |____/                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓
          
      You don't bother getting up. You keep your sword in hand, knowing enemies like this tend to gloat when they win a
       battle. Turns out you know nothing. He simply shoots more fire at you until you're nothing except a pile of ash
                                          and armor. Your journey is at an end.          
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/  ''')
        break

    if CurrentRoom == "BM_Battlea" and move[0].lower() == 'strike':
        CurrentRoom = 'BM_Battleb'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |    "You won't get lucky twice."                              \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
             ____          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
            |___ \         ║         |__ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
              __) |        ║            ) |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
             |__ <         ║           / /                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
             ___) |        ║          / /_                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
            |____/         ║         |____|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battleb" and move[0].lower() == 'rush':
        CurrentRoom = 'BM_Battlec'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |   "Oh? I see you have some skills..."                        \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             |__ \         ║         |__ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
                ) |        ║            ) |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               / /         ║           / /                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
              / /_         ║          / /_                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             |____|        ║         |____|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlel" and move[0].lower() == 'recoup':
        CurrentRoom = 'BM_Battlei'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |   "Oh? I see you have some skills..."                        \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             |__ \         ║         |__ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
                ) |        ║            ) |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               / /         ║           / /                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
              / /_         ║          / /_                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             |____|        ║         |____|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlei" and move[0].lower() == 'hand':
        CurrentRoom = 'BM_Battleo'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |   "Ha ha ha.  Any last words?"                               \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║         |__ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║            ) |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           / /                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║          / /_                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║         |____|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlek" and move[0].lower() == 'bow':
        CurrentRoom = 'BM_Battler'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |   "Ha ha ha.  Any last words?"                               \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║         |__ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║            ) |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           / /                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║          / /_                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║         |____|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlec" and move[0].lower() == 'blind':
        CurrentRoom = 'BM_Battled'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |   "Ha ha ha.  Any last words?"                               \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║         |__ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║            ) |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           / /                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║          / /_                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║         |____|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battler" and move[0].lower() == 'charge':
        CurrentRoom = 'BM_Battles'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |  "Your screams are like a symphony to me."                   \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             / _ \         ║         |__ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║            ) |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║           / /                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
            | |_| |        ║          / /_                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             \___/         ║         |____|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓

         You don't have time to waste. The room is filling with fire. Escape is almost an impossibility. You get back up,
            prepared to launch an all or nothing attack. You clutch your sword tight, whisper a prayer to yourself and
             rush towards the Black Mage. As you get closer, the heat intensifies. You rush closer still. Sword ready
               to pierce him when you are paralyzed once more! You move your eves down to see the dismembered hand
                  once again has a hold on you! At such a close range there's no time to dodge the Black Mages
                          incoming attack. As he screams, fire erupts around you and closes in on you. 
                                                    Your journey is at an end.
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/  ''')
        break

    if CurrentRoom == "BM_Battleo" and move[0].lower() == 'charge':
        CurrentRoom = 'BM_Battlee'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |  "Your screams are like a symphony to me."                   \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             / _ \         ║         |__ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║            ) |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║           / /                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
            | |_| |        ║          / /_                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             \___/         ║         |____|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓

      You don't have time to waste. The room is filling with fire. Escape is almost an impossibility. You get back up, prepared
       to launch an all or nothing attack. You clutch your sword tight, whisper a prayer to yourself and rush towards the
        Black Mage. As you get closer, the heat intensifies. You rush closer still. Sword ready to pierce him when you
         are paralyzed once more! You move your eves down to see the dismembered hand once again has a hold on you! At
          such a close range there's no time to dodge the Black Mages incoming attack. As he screams, fire erupts
                              around you and closes in on you. Your journey is at an end.
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/  ''')
        break

    if CurrentRoom == "BM_Battled" and move[0].lower() == 'charge':
        CurrentRoom = 'BM_Battlee'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |  "Your screams are like a symphony to me."                   \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             / _ \         ║         |__ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║            ) |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║           / /                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
            | |_| |        ║          / /_                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             \___/         ║         |____|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓

      You don't have time to waste. The room is filling with fire. Escape is almost an impossibility. You get back up, prepared
       to launch an all or nothing attack. You clutch your sword tight, whisper a prayer to yourself and rush towards the
        Black Mage. As you get closer, the heat intensifies. You rush closer still. Sword ready to pierce him when you
         are paralyzed once more! You move your eves down to see the dismembered hand once again has a hold on you! At
          such a close range there's no time to dodge the Black Mages incoming attack. As he screams, fire erupts
                              around you and closes in on you. Your journey is at an end.
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/  ''')
        break

    if CurrentRoom == "BM_Battleb" and move[0].lower() == 'hide':
        CurrentRoom = 'BM_Battlef'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |  "DAMN YOU!  I WON'T LET YOU PASS!                           \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
             ____          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
            |___ \         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
              __) |        ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
             |__ <         ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
             ___) |        ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
            |____/         ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlec" and move[0].lower() == 'hide':
        CurrentRoom = 'BM_Battlef'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |  "Why fight it? Your death is inevitable..."                 \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             |__ \         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
                ) |        ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               / /         ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
              / /_         ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             |____|        ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlei" and move[0].lower() == 'bow':
        CurrentRoom = 'BM_Battlem'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |  "Why fight it? Your death is inevitable..."                 \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             |__ \         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
                ) |        ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               / /         ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
              / /_         ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             |____|        ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlef" and move[0].lower() == 'hand':
        CurrentRoom = 'BM_Battleg'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |  "Why fight it? Your death is inevitable..."                 \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             |__ \         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
                ) |        ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               / /         ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
              / /_         ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             |____|        ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battleo" and move[0].lower() == 'reflect':
        CurrentRoom = 'BM_Battlep'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |  ""You're tougher than you look..."                         \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |                                                              \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlem" and move[0].lower() == 'reflect':
        CurrentRoom = 'BM_Battleu'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |  ""You're tougher than you look..."                         \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |                                                              \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battler" and move[0].lower() == 'hide':
        CurrentRoom = 'BM_Battlet'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |  ""You're tougher than you look..."                         \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |                                                              \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battled" and move[0].lower() == 'bow':
        CurrentRoom = 'BM_Battlen'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |  ""You're tougher than you look..."                         \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |                                                              \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battled" and move[0].lower() == 'bow':
        CurrentRoom = 'BM_Battlen'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |  ""You're tougher than you look..."                         \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |                                                              \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battleg" and move[0].lower() == 'bow':
        CurrentRoom = 'BM_Battleh'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |  ""You're tougher than you look..."                         \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |                                                              \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlep" and move[0].lower() == 'charge':
        CurrentRoom = 'BM_Battlee'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |   "No matter the path, the destination                       \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |        is inevitable..."                                      >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             / _ \         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
            | | | |        ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             \___/         ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓
      
      You don't have time to waste. The room is filling with fire. Escape is almost an impossibility. You get back up, prepared
       to launch an all or nothing attack. You clutch your sword tight, whisper a prayer to yourself and rush towards the
        Black Mage. As you get closer, the heat intensifies. You rush closer still. Sword ready to pierce him when you
         are paralyzed once more! You move your eves down to see the dismembered hand once again has a hold on you! At
          such a close range there's no time to dodge the Black Mages incoming attack. As he screams, fire erupts
                              around you and closes in on you. Your journey is at an end.
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/  ''')
        break

    if CurrentRoom == "BM_Battleu" and move[0].lower() == 'charge':
        CurrentRoom = 'BM_Battlee'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |   "No matter the path, the destination                       \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |        is inevitable..."                                      >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             / _ \         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
            | | | |        ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             \___/         ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓

      You don't have time to waste. The room is filling with fire. Escape is almost an impossibility. You get back up, prepared
       to launch an all or nothing attack. You clutch your sword tight, whisper a prayer to yourself and rush towards the
        Black Mage. As you get closer, the heat intensifies. You rush closer still. Sword ready to pierce him when you
         are paralyzed once more! You move your eves down to see the dismembered hand once again has a hold on you! At
          such a close range there's no time to dodge the Black Mages incoming attack. As he screams, fire erupts
                              around you and closes in on you. Your journey is at an end.
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/  ''')
        break

    if CurrentRoom == "BM_Battlen" and move[0].lower() == 'charge':
        CurrentRoom = 'BM_Battlee'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |   "No matter the path, the destination                       \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |        is inevitable..."                                      >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             / _ \         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
            | | | |        ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             \___/         ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓

      You don't have time to waste. The room is filling with fire. Escape is almost an impossibility. You get back up, prepared
       to launch an all or nothing attack. You clutch your sword tight, whisper a prayer to yourself and rush towards the
        Black Mage. As you get closer, the heat intensifies. You rush closer still. Sword ready to pierce him when you
         are paralyzed once more! You move your eves down to see the dismembered hand once again has a hold on you! At
          such a close range there's no time to dodge the Black Mages incoming attack. As he screams, fire erupts
                              around you and closes in on you. Your journey is at an end.
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/  ''')
        break

    if CurrentRoom == "BM_Battlet" and move[0].lower() == 'charge':
        CurrentRoom = 'BM_Battlee'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |   "No matter the path, the destination                       \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |        is inevitable..."                                      >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             / _ \         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
            | | | |        ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             \___/         ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓

      You don't have time to waste. The room is filling with fire. Escape is almost an impossibility. You get back up, prepared
       to launch an all or nothing attack. You clutch your sword tight, whisper a prayer to yourself and rush towards the
        Black Mage. As you get closer, the heat intensifies. You rush closer still. Sword ready to pierce him when you
         are paralyzed once more! You move your eves down to see the dismembered hand once again has a hold on you! At
          such a close range there's no time to dodge the Black Mages incoming attack. As he screams, fire erupts
                              around you and closes in on you. Your journey is at an end.
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/  ''')
        break

    if CurrentRoom == "BM_Battleh" and move[0].lower() == 'charge':
        CurrentRoom = 'BM_Battlee'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |   "No matter the path, the destination                       \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |        is inevitable..."                                      >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║           __                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             / _ \         ║          /_ |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║           | |                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
            | | | |        ║           | |                                  ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
            | | | |        ║           | |                                  ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             \___/         ║          |___|                                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓

      You don't have time to waste. The room is filling with fire. Escape is almost an impossibility. You get back up, prepared
       to launch an all or nothing attack. You clutch your sword tight, whisper a prayer to yourself and rush towards the
        Black Mage. As you get closer, the heat intensifies. You rush closer still. Sword ready to pierce him when you
         are paralyzed once more! You move your eves down to see the dismembered hand once again has a hold on you! At
          such a close range there's no time to dodge the Black Mages incoming attack. As he screams, fire erupts
                              around you and closes in on you. Your journey is at an end.
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/  ''')
        break

    if CurrentRoom == "BM_Battlef" and move[0].lower() == 'shield':
        CurrentRoom = 'BM_Battlej'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |                                                             \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |   "Hells...                                                  \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |       ...am I...really that weak...?"                        /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
             ____          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
            |___ \         ║         / _ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
              __) |        ║        | | | |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
             |__  <        ║        | | | |                                 ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
             ___) |        ║        | | | |                                 ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
            |____/         ║         \___/                                   ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlem" and move[0].lower() == 'shield':
        CurrentRoom = 'BM_Battlej'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |  "Master....                                                \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |                                                              \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |           I'm sorry...."                                      >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             |__ \         ║         / _ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
                ) |        ║        | | | |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               / /         ║        | | | |                                 ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
              / /_         ║        | | | |                                 ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             |____|        ║         \___/                                   ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battleg" and move[0].lower() == 'shield':
        CurrentRoom = 'BM_Battlej'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |  "Master....                                                \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |                                                              \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |           I'm sorry...."                                      >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |                                                              /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
              ___          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
             |__ \         ║         / _ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
                ) |        ║        | | | |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               / /         ║        | | | |                                 ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
              / /_         ║        | | | |                                 ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
             |____|        ║         \___/                                   ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlep" and move[0].lower() == 'shield':
        CurrentRoom = 'BM_Battlej'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |  "Why is it...                                              \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |                                                              \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |            .....so cold...?                                  /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║         / _ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║        | | | |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║        | | | |                                 ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║        | | | |                                 ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║         \___/                                   ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')


    if CurrentRoom == "BM_Battleu" and move[0].lower() == 'shield':
        CurrentRoom = 'BM_Battlej'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |  "Why is it...                                              \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |                                                              \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |            .....so cold...?                                  /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║         / _ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║        | | | |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║        | | | |                                 ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║        | | | |                                 ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║         \___/                                   ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlet" and move[0].lower() == 'shield':
        CurrentRoom = 'BM_Battlej'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |  "Why is it...                                              \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |                                                              \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |            .....so cold...?                                  /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║         / _ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║        | | | |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║        | | | |                                 ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║        | | | |                                 ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║         \___/                                   ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlen" and move[0].lower() == 'shield':
        CurrentRoom = 'BM_Battlej'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |  "Why is it...                                              \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |                                                              \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |            .....so cold...?                                  /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║         / _ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║        | | | |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║        | | | |                                 ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║        | | | |                                 ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║         \___/                                   ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battleh" and move[0].lower() == 'shield':
        CurrentRoom = 'BM_Battlej'
        print('''

                                                                                                             ▓▓▓▓▓▓▓
                                                                                                             ▓░░░░░▓
                                                                                                        ▓▓▓▓▓▓░░░░░▓▓▓▓
                                                                                                     ▓▓▓▓░░░░░▓▓▓▓▓░░░▓
                                                                                                     ▓░░░▓▓▓░▓▓▓▓▓▓░░░▓
                                                                                                ▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░▓░░░▓
                                                                                           ▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                                           ▓░░░░░░▓░▓░▓▓▓▓▓▓▓▓▓▓▓░░░▓
                                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░░░▓▓
                                                                        ▓▓▓▓░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
                                                                        ▓░░░░▓░▓░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓░▓▓▓░▓░▓░▓░▓░░░▓
                                                                        ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓░▓░▓▓░░░▓
                                                                        ▓▓▓▓░░░▓▓▓▓▓▓▓░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░▓░▓░▓▓▓░░░▓
                                                                           ▓▓░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░░▓▓▓▓
                                                                            ▓▓░░░░░░░░░▓░▓░▓░▓░▓░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓
                                                                             ▓▓▓▓▓▓▓▓▓▓░░░░░░░▓▓▓▓▓▓▓▓▓░▓░▓░▓▓░░░▓▓▓
        +-----------------------------------------------------------+              ▓░▓░░░░░░░░░░░░░░░░░▓░▓▓▓▓▓░░░▓░▓▓
        |                                                            \          ▓▓▓▓░░▓▓▓░░░░░░░░░░░░░▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓
        |  "Why is it...                                              \        ▓▓▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓▓▓▓▓▓░░░▓
        |                                                              \      ▓▓░▓░░░░░░▓▓░░░░░▓▓▓░░░░░░░░░░░▓▓░░░▓▓░░░▓▓▓
        |                                                               >   ▓▓▓░░░▓▓▓░░░░░░░░░░▓▓▓░░░░░░░░░░▓▓▓░░░▓▓▓▓▓░░▓
        |            .....so cold...?                                  /    ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓▓▓
        |                                                             /     ▓░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░▓
        +------------------------------------------------------------+      ▓░░░▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
                                                                           ▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                        **      ** *******                                 ▓▓▓▓░░░░░░▓░▓▓▓▓▓▓▓▓▓▓▓░▓░░░░░░░░▓▓▓▓▓░░░▓▓▓
                       /**     /**/**////**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**   /**                                ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**********/*******                                 ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**//////**/**////                                  ▓░░░▓▓▓▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓ 
                       /**     /**/**                                      ▓▓▓▓░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       /**     /**/**                                         ▓░░░▓░░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
                       //      // //                                          ▓░░░▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              YOU          ║       BLACK MAGE                                 ▓░░░▓▓░▓░░░▓▓▓░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
      ══════════════════════════════════════════════                          ▓░░░▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓
               __          ║          ___                                     ▓░░░▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░▓▓▓
              /_ |         ║         / _ \                                    ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║        | | | |                                   ▓░░░▓▓▓▓▓▓▓░░░░░░░░░▓▓░░░░░▓▓▓▓▓▓░░░░░░░▓▓
               | |         ║        | | | |                                 ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓░░░▓▓▓▓▓░░░▓▓▓░░░▓▓▓
               | |         ║        | | | |                                 ▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓░░░▓
              |___|        ║         \___/                                   ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
      ══════════════════════════════════════════════                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░▓▓▓▓
                                                                                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓''')

    if CurrentRoom == "BM_Battlej" and move[0].lower() == 'continue':
        CurrentRoom = 'Main_Tower_F2R2a'

    if CurrentRoom == "Main_Tower_F2R2a" and move[0].lower() == 'go' and move[1].lower() == 'west':
        print('''
        You rushed out of the room to look for something to get across. Unfortunately the fire had brought down the ceiling.
         Supports have crumbled and your only exit is now nothing but a pile of burning wood and stone. It is impossible 
        to pass. Your only options are to wait to burn or fall to your doom through the hole at the other end of the room.
                                             Your journey has come to an end.
          ________    _____      _____  ___________               ____________   _________________________ 
         /  _____/   /  _  \    /     \ \_   _____/               \_____  \   \ /   /\_   _____/\______   \\
        /   \  ___  /  /_\  \  /  \ /  \ |    __)_      ______     /   |   \   Y   /  |    __)_  |       _/
        \    \_\  \/    |    \/    Y    \|        \    /_____/    /    |    \     /   |        \ |    |   \\
         \______  /\____|__  /\____|__  /_______  /               \_______  /\___/   /_______  / |____|_  /
                \/         \/         \/        \/                        \/                 \/         \/                                             
                                             ''')
        break

    if CurrentRoom == "Main_Tower_F2R2a" and move[0].lower() == 'use' and move[1].lower() == 'oldwhip':
        CurrentRoom = 'Main_Tower_F2R3'
        inventory.remove("oldwhip")
        print('''
        You wrap the old whip around and swing across. You barely make it before the fire burns the whip. You're safe, but
            there's no going back!''')

    if CurrentRoom == "Main_Tower_F2R2a" and move[0].lower() == 'use' and move[1].lower() == 'rope':
        CurrentRoom = 'Main_Tower_F2R3'
        inventory.remove("rope")
        print('''
        You wrap the rope around and swing across. You barely make it before the fire burns the whip. You're safe, but
            there's no going back!''')

    if CurrentRoom == "Main_Tower_Final2" and "scroll" in inventory:
        CurrentRoom = 'Main_Tower_Final2a'
        inventory.remove("scroll")
        print('''  
        The Dark Wizard is here. He turns around. He's looking more in your general direction then at you. Up close, he just looks
         like a floating robe with to small white flames for eyes. He doesn't speak. Maybe he can't speak...? The left side of his
          robe flutters for a brief moment, and once again the room is surrounded by black fire. He begins making that cold laugh
           again. He begins to float towards the balcony, but amidst your panic, a moment of clarity arrives. The scroll! You
            take in out and unravel it as fast as you can and shout at the top of your lungs:
                                                
                                                "KLAATU VERATA NIKTO!!!"
                                                
         The Dark Wizard stops hovering and falls to the ground in pain. Arms and legs manifest from the robe, but barely. You
          can still see through them, but it looks as thought he has a physical form. You only have one shot at this. you better
            make it count. After an awesome battle wilder than anything you can imagine (there were probably ninjas and a 
             programmer who ran out of time to make a proper ending) You won!
             
        You won! The Dark Wizard is vanquished as the world around you is devoured flames. Theres only one area of the room that
                                           has yet to be ravaged by fire.''')

    if CurrentRoom == "Main_Tower_Final3" and move[0].lower() == 'int' and move[1].lower() == 'sleep':
        print('''
        You just want to sleep. You earned that much at least. You fall face first onto the bed and close your eyes.
                                It was the best sleep You've had in your entire life.
                           ___________.__                       ___________           .___
                           \__    ___/|  |__   ____             \_   _____/ ____    __| _/
                             |    |   |  |  \_/ __ \    ______   |    __)_ /    \  / __ | 
                             |    |   |   Y  \  ___/   /_____/   |        \   |  \/ /_/ | 
                             |____|   |___|  /\___  >           /_______  /___|  /\____ | 
                                           \/     \/                    \/     \/      \/ 
                             ______   ______   ______   ______   ______   ______   ______ 
                            /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/
        ''')
        break
