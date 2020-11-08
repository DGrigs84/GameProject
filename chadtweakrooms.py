#!/usr/bin/env python3

def ShowStatus():
    # Displays the player's current location
    print('\n╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗')
    print(' ● ',end="")
    print(rooms[CurrentRoom]['desc'])
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

## As of now, this is used to try to "build" the map try to see if movent is programmable by tonight.
# The dictionary used to link the rooms together
rooms = {
        'Tent': {
                'north': 'Camp',
                'desc': 'There is a pile of old blankets infused with your sweat and blood. There is some light shining into the tent through the opening in the \'North\'.',
                'invitem': 'breakfast',
                'item': 'You notice your BREAKFAST lying on the ground next to the sheets. It\'s probably a good idea to eat it now.\n      ~ [Use the \'get BREAKFAST\' command to add the item to your inventory, followed by \'use BREAKFAST\' to eat it]'
                },
        'Camp': {
                'north': 'Drawbridge',
                'desc': 'You muster with the rest of the knights. After an uninspiring speech by your commander, you\'re told to move out.\n     You prepare to march further \'North\' to the Dark Wizard\'s castle.\n       ...All hopes rest on this last attack. There\'s no turning back now.'
                },
        'Drawbridge': {
                'north': 'Courtyard_Main',
                'desc': 'As you and your comerades approach the castle, you notice the drawbridge has already been lowered. \n     \"Good fortunes men!\" the Commander shouts. \"Our previous raids must have destroyed the counterbalance! These demons are wide open for a frontal assault!\"\n                                                     \"CCCHHHAAAAAAAAARRRGGGEEE!!!\"\n   You feel something is amiss, but orders are orders. You rush forward across the bridge, laid out over a chasm which looks as though it leads down to Hell itself.\n     Just as your battalion reaches halfway across the bridge, your greeted by the sound of laughter so cold you can see your breath.\n   Screams of agony errupt behind you. Looking back, you see some of your comerades engulfed in what appears to be black flames.\n     You also take note the drawbridge had caught fire as well, blocking your only escape.\n    Your comerades rush into the the castle, swords drawn, ready to use skills they trained so hard to master.\n Your only option is to follow suit and rush \'North\' to the inner walls of the castle.\n  ' 
                },
        'Courtyard_Main': {
                'north': 'Castle_Entrance',
                'east': 'Courtyard_East',
                'west': 'Courtyard_West',
                'desc': 'There\'s no going back, your only escape is now nothing but ash. You\'re standing in the main area of the castle courtyard.\n    Dead trees. Dead grass. A premonition of things to come? \n  ~ North: Looks as though the entrance to the castle is up ahead. \n  ~ West: You once heard screaming coming from that direction. You can see something glistening from a nearby tree that caught fire. \n  ~ East: You see nothing but more dead foliage.',
                'eqitem': 'sword',
                'gear': 'You dropped your SWORD. Mind still racing. Heart beating so hard it seems as though it will burst out of your chest.\n   Just being in the Dark Wizard\'s presence instilled you with a fear unlike any you\'ve felt before.\n      But this is no time to be weak! Pick up your SWORD and fight! For everlasting peace!'
                },
        'Courtyard_West': {
                'north': 'Courtyard_Midwest',
                'east': 'Courtyard_Main',
                'desc': 'Body parts are scattered everywhere. Human and monster alike. Blood-soaked armor glistens off the fire like a dragon\'s eye. \n  ~ North: Looks like more evidence a battle took place.  You don\'t notice any movement. \n  ~ East: The main area of the courtyard.  Feels more like the entrance to a nightmare.'
                },
        'Courtyard_Midwest': {
                'north': 'Courtyard_Northwest',
                'south': 'Courtyard_West',
                'desc': 'Signs of another battle. What else would there be? It looks as though it ended in a draw.  Both man and monster lay dead near a lever.\n       ....The monster appears to be missing a hand.... \n  ~ North: There appears to be nothing but rotting trees. Evidence of an old orchard. Was this castle once overtaken? \n  ~ South: You once heard screaming coming from that direction. You can see something glistening from a nearby tree that caught fire.',
                'envitem': 'lever',
                'engage': 'You notice a LEVER slightly hidden behind a pile of rocks. A demon\'s hand maintaining a death grip on it. It was separated at the wrist.'
#  Interact portion incomplete. Unsure how to code. needs research. lever will open gate in Castle_Entrance room
#                'interact': 'You take the hand off the lever and throw it to the ground with a heavy thud.\n     You pull the lever and hear gears grinding in the distance.' 
                },
        'Courtyard_Northwest': {
                'south': 'Courtyard_Midwest',
                'desc': 'Just as you suspected. A dead orchard. You are surrounded by dead trees, symbolizing dead titans reaching down to grab you. \n  ~ South: Looks like more evidence a battle took place.  You don\'t notice any movement.',
                'invitem': 'apple',
                'item': 'You notice one shiny red APPLE hanging from a branch. A sign of like in amidst all this death.  It\'s somehow...hopeful.'
                },
        'Courtyard_East': {
                'north': 'Courtyard_Mideast',
                'west': 'Courtyard_Main',
                'desc': 'No signs of life here either. The vegitation looks ready to crumble to dust if you touch it. \n  ~ North: You see evidence of one of our previous attacks. Stone tumbling into the courtyard, proof of an outside attack. \n  ~ West: The main area of the courtyard.  Feels more like the entrance to a nightmare.'
                },
        'Courtyard_Mideast': {
                'south': 'Courtyard_East',
                'desc': 'Large stone pours into the courtyard. A failed attack from one of our previous raids. \n  ~ South: You see nothing but more dead foliage.',
                'eqitem': 'helmet',
                'gear': 'You see a perfectly good HELMET about your size. The previous owner\'s head is mere meters away.'
                },
        'Castle_Entrance': {
# Make a door that interacts with the lever in Courtyard_Midwest, leading to the Cooridor.
        ##See about 2 different descriptions based on door open or closed.
                'north': 'Corridor',
                'south': 'Courtyard_Main',
                'desc': 'You stand before a large door at least three times your height. There are spikes jutting out, some adorning human skulls. Intimidating? Yes.\n      You don\'t notice a way to open it from here. \n  ~ South:  The main area of the courtyard.  Feels more like the entrance to a nightmare.'
#                'desc2': 'You stand at the entrance to the castle. The opening to the main hall resembling a mouth ready to swallow you, never to see the light again.  \n  ~ North: The corridor th the castle\'s main hall lies before you.  \n  ~ South:  The main area of the courtyard.  Feels more like the entrance to a nightmare.'
                },
        'Corridor': {
                'north': 'Hall',
                'desc': 'The door slams behind you! There\'s no way to open it from here. The only way to go is forward. Great.  \n  ~ North: There is a hallway leading to the main hall of the castle.' 
                },
        'Hall': {
# Would like to trigger an "into" battle/tutorial. Need a "scene" triggering before and after fight.
        ## May need to use other description if that isn't doable. 
                'north': 'Main_Hall_South',
                'desc': 'You walk slowly into the hall, guard up. Again, you hear that cold laughter.  You instinctly look behind you to notice the black flames again.\n      You get out of the range of the fire as a goblin jumps down from the ceiling behind you. Trying for a sneak attack!'
# After tut. >   'descafter': 'You weaken the goblin as it staggers backwards. One of the wicks of its explosives catch fire.\n      You need to get out before the explosives go off!  \n  ~ North: The castle\'s main hall is dead ahead!'
# 2nd scenario > 'desc2': 'You walk slowly into the hall, guard up. Again, you hear that cold laughter.  You instinctly look behind you to notice the black flames again.\n      It begin to creep forward, you know you need to get out of here before the flames surround you!  \n  ~ North: The castle\'s main hall is dead ahead!'
                },
        'Main_Hall_South': {
                'north': 'Main_Hall_Center',
                'east': 'Main_Hall_Southeast',
                'west': 'Main_Hall_Southwest',
                'desc': """
The hallway had collapsed from the explosion. Every move you seem to make, you find yourself further ensnared in some sort of trap.  
~ North: The center of the main hall. You notice a dark but beautiful light in the distance.  
~ West: A corner of the main hall. Wait...is that a... hole there?
~ East: A corner of the main hall. you notice some furniture and candles flickering in the distance."""
#                'desc2': 'The hallway had collapsed from the explosion. Every move you seem to make, you find yourself further ensnared in some sort of trap.  \n  ~ North: The center of the main hall.  \n  ~ West: A corner of the main hall.  Wait...is that a. ..hole there?  \n  ~ East: A corner of the main hall. you notice some furniture and candles flickering in the distance.'
# 2nd scenario > 'descalt': 'You make it out of the hallway as it fully engulfs in flames.  For some reason, it refulses to spread into the main hall.\n      You aren\'t sure why, but you know you\'re safe from the flames.\  \n  ~ North: The center of the main hall. You noticed a dark but beautiful light in the distance.  \n  ~ West: A corner of the main hall.  Wait...is that a. ..hole there?  \n  ~ East: A corner of the main hall. you notice some furniture and candles flickering in the distance.' 
                },
        'Main_Hall_Southwest': {
                'north': 'Main_Hall_West',
                'east': 'Main_Hall_South',
                'down': 'Jailroom1',
                'desc': 'This corner of the main hall seems \'extra\' dark. You barely make out a hole that contains stairs leading down.  \n  ~ North: A pool of bood blood leading from the stairs to a door on the other end of the main hall.  \n  ~ East: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ Down: A set of stairs decending into an unknown horror. Nothing bad ever happens in a cellar, right?'
                },
        'Main_Hall_West': {
                'north': 'Kitchen',
                'south': 'Main_Hall_Southwest',
                'east': 'Main_Hall_Center',
                'west': 'West_Wing',
                'desc': 'The trail of blood is thicker here. Looks to be a small pool under the edge of the door.  \n  ~ North: There\'s a door with a pool of blood under it.  \n  ~ South: A corner of the main hall.  Wait...is that a. ..hole there?  \n  ~ West: There is a pathway leading to the western tower.  \n  ~ East: The center of the castle\'s main hall. You notice a dark but beautiful light in the distance.',
#                'desc2': 'The trail of blood is thicker here. Looks to be a small pool under the edge of the door.  \n  ~ North: There\'s a door with a pool of blood under it.  \n  ~ South: A corner of the main hall.  Wait...is that a. ..hole there?  \n  ~ West: There is a pathway leading to the western tower.  \n  ~ East: The center of the castle\'s main hall.',
                'invitem': 'flint',
                'item': 'You see a piece of FLINT rock under one of the torches by the door.'
                },
        'Kitchen': {
                'north': 'Meat_Locker',
                'south': 'Main_Hall_West',
                'desc': 'You\'re in the castle\'s kitchen. Who would\'ve guessed that monsters cook their food?  \n  ~ North: There\'s a door. Maybe the castle\'s pantry?  \n  ~ South: A door back to the castle\'s main hall.',
                'invitem': 'fire',
                'item': 'You notice a scroll to learn the FIRE spell. Maybe they use it to cook with?'
# Scenario >     'scenario': Needs THIGH and FLINT to make MEAT; MEAT + POISON = BAIT
                },
        'Meat_Locker': {
                'south': 'Kitchen',
                'desc': 'You notice a bunch of people hanging from meat hooks, some of them have limbs hacked off.\n    You now understand why you were all led here.  \n  ~ South: Back to the Kitchen',
                'invitem': 'thigh',
                'item': 'You notice a person\'s THIGH in a bin. Probably set aside to be eaten. The thought of being food for these..things.. makes you sick.\n      You know there\'s no chance to give these people a proper burial, but this is one piece these bastards won\'t get.' 
                },
        'Main_Hall_Southeast': {
                'north': 'Main_Hall_East',
                'west': 'Main_Hall_South',
                'desc': 'There\'s a painting of the Dark Wizard on the wall. You feel like you\'re being watched.  \n  ~ North: The other end of the main hall. You can make out a door from here.   \n  ~ West: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.'
#                'invitem': 'map',
#                'item': 'There\'s a table under the painting. There\'s a MAP sitting on the table between two lit candlesticks.' 
                },
        'Main_Hall_East': {
                'north': 'Barracks',
                'south': 'Main_Hall_Southeast',
                'east': 'East_Wing',
                'west': 'Main_Hall_Center',
                'desc': 'You\'re standing in the eastern portion of the main hall.  \n  ~ North: You see a door. You don\'t understand monster language, but you think you see a picture of a bed?  \n  ~ South: A corner of the main hall. you notice some furniture and candles flickering in the distance.  \n  ~ West: The center of the main hall. You notice a dark but beautiful light in the distance.  \n  ~ East: There is a pathway leading to the eastern tower.'
#                'desc2': 'You\'re standing in the eastern portion of the main hall.  \n  ~ North: You see a door. You don\'t understand monster language, but you think you see a picture of a bed?  \n  ~ South: A corner of the main hall. you notice some furniture and candles flickering in the distance.  \n  ~ West: The center of the main hall.  \n  ~ East: There is a pathway leading to the eastern tower.
                },
        'Barracks': {
                'north': 'Armory',
                'south': 'Main_Hall_East',
                'desc': 'This must be the monster\'s barracks.  \"They\'re more like us than I realized.\" You think to yourself.  \n  ~ North: You see a door with a picture of two swords crossed over a shield.  \n  ~ South: This way leads you back to the main hall.',
                'invitem': 'dkey',
                'item': 'You notice a key hanging on one of the beds. It has a picture of a jailcell etched into it. Maybe it\'s the dungeon key? Or DKEY for short.'
                },
        'Armory': {
                'south': 'Barracks',
                'desc': 'You found the castle\s armory! There are no weapons but plenty of armor. These do seem like the typ of creatures to focus more on attack than defense...  \n  ~ South: This will take you back to the barracks.',
                'eqitem': 'boots',
                'gear': 'Your eyes glance all across the armory. SO many different shapes and sizes! Your eyes catch a pair of BOOTS that are probably your size...'
                },
        'Main_Hall_Center': {
                'north': 'Main_Hall_North',
                'south': 'Main_Hall_South',
                'east': 'Main_Hall_East',
                'west': 'Main_Hall_West',
                'desc': 'There\'s a wall of green and purple flames that prevent you from going towards the main tower.\n      You notice two pillars, one on each side of the wall, corresponding with the colors of the flames. It looks as though you could place an ORB on the top of each one.  \n  ~ South: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ West: This way will lead you to the western part of the main hall.  \n  ~ East: This way will lead you to the eastern part of the main hall.'
#  Green ORB     'descA': 'The GREEN ORB sits atop its rightful place.\n    There\'s a wall of purple flames that prevent you from going towards the main tower, meaning only the PURPLE ORB remains.  \n  ~ South: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ West: This way will lead you to the western part of the main hall.  \n  ~ East: This way will lead you to the eastern part of the main hall.'
#  Purple ORB    'descB': 'The PURPLE ORB sits atop its rightful place.\n    There\'s a wall of green flames that prevent you from going towards the main tower, meaning only the GREEN ORB remains.  \n  ~ South: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ West: This way will lead you to the western part of the main hall.  \n  ~ East: This way will lead you to the eastern part of the main hall.'
#  BOTH          'desc2': 'Both ORBS sit atop their respective pillars. witht he flames gone, you are now able to make it up the main tower and take on the Dark Wizard.  \n  ~ North: This leads you to the bottom of the main tower.  \n  ~ South: The entrance to the main hall...but you can\'t really call it that now that there\'s no way to enter.  \n  ~ West: This way will lead you to the western part of the main hall.  \n  ~ East: This way will lead you to the eastern part of the main hall.'                
                },
        'Main_Hall_North': {
                'north': 'Belmont',
                'south': 'Main_Hall_Center',
                'up': 'Main_Tower1',
                'desc': 'You made it. You\'re at the base of the main tower. The Dark Wizard must be somewhere up top.\n  You notice the state of the room and realize that you must have missed one hell of a fight before the flame wall was cast.\n      There\'s monster parts, fallen brothers in arms, bomb residue, broken gear, eviscerated flesh, teeth... Memories you won\'t soon forget\n      You notice claw marks and sword slashes on the walls. The northern wall is has a huge crack in it.  \n  ~ South: This will put you back into the main hall.  \n  ~ Up: Begin ascending the spiral staircase of the final tower!'
#   Somehow see if its possible to USE the OLDWHIP in room and have a script to "open" the wall to get in                
                },
        'Belmont': {
                'south': 'Main_Hall_North',
                'desc': 'What is a man?! A miserable little pile of secrets! But enough talk! Have at you!\n     You notice a lone treasure chest in this hidden room. You kick it open as hard as you can and spilled whatever contents it contained onto the cold, stone floor.   \n  ~ South: With your new super secret items and skills, you\'re ready to get up that tower!',
                'invitem': 'pchop',
# Other items   'invitemAB': 'btears', 'rope',
                'item': 'Who cooks a pork chop and hides it in a wall?!\n    Before you can even begin to ponder the answer, you notice a ROPE and the BELMONT scroll with the words \"Bloody Tears\" enscribed on the top.\n      You look over this weird haul of a PCHOP, ROPE and BELMONT scroll, debating on whether or not to take them.\n             I mean, really? Who\'s idea was it to put a pork chop in a wall?'
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
                'east': 'Main_Hall_West',
                'up': 'West1_Main',
                'desc': 'You\'re standing at the base of the western tower.  \n  ~ East: This direction will lead you back into the main hall.  \n  ~ Up: A set of stairs leading up into the west tower.'
                },
        'East_Wing': {
                'west': 'Main_Hall_East',
                'up': 'East1_Main',
                'desc': 'You\'re standing at the base of the eastern tower.  \n  ~ West: This direction will lead you back into the main hall.  \n  ~ Up: A set of stairs leading up into the east tower.'
                },
        'Jailroom1': {
                'north': 'Jailroom2',
                'up': 'Main_Hall_Southwest',
                'desc': 'You\'re standin in the enterance to the castle\'s dungeon. Who would have guessed that they actually keep prisoners? There is a door to the \'North\' that requires a key to enter.  \n  ~ Up: A set of stairs leading back up into the main hall.'
#                 'desc2': 'desc': 'You\'re standin in the enterance to the castle\'s dungeon. Who would have guessed that they actually keep prisoners?  \n  ~ North: A door that leads you further into the dungeon.  \n  ~ Up: A set of stairs leading back up into the main hall.'
## north needs DKEY
                },
        'Jailroom2': {
                'north': 'Jailroom3',
                'south': 'Jailroom1',
                'desc': 'You arrive in a wide open room resembling a small colosseum. The Guardian Beast lies sleeping. A pile of bines lat before it. Some meat chunks still attachecd. You don\'t believe it heard you enter, but you noticed it\'s ear twitch.'
#                'desc2': 'You arrive in a wide open room resembling a small colosseum. The beasts corpse lies dead from poison. You swear you saw it move, but it must have just been your nerves.'
#                'desc3': 'You arrive in a wide open room resembling a small colosseum. The beast is back on it\'s feet?! The poison didn't seem to have the deired effect on it after all. It stands between you and the exit, but luckilly it does appear to be weakened. You have no choice but to fight!'
#                'desc4': 'You arrive in a wide open room resembling a small colosseum. The Gurdian Beast's corpse lies in a pile near the center of the room.\n    Proof of a hard faught victory.'
#                'interact' 'The beast awakens, smelling the cooked thigh. It charges at you, excited for its treat.  Before it gets to close you throw th BAIT at the creature.  It swallows it without even chewing.  THe poison takes affect almost instantly.  The beast dry heaves and you can see it struggles to breathe. In mere moments its body becomes upright and stiff before falling onto its side like a broom falling to the floor.' 
                },
        'Jailroom3': {
                'north': 'Jailroom4',
                'south': 'Jailroom2',
                'east': 'Jailcell2',
                'west': 'Jailcell1',
                'desc': 'You\'re in the middle of a crossway. There\'s two jailcells here and another door which leads you further in.  \n  ~ North: A door similar to the others. It must lead further into the dungeon.  \n  ~ South: It will lead you back to the room where the beast was dwelling.  \n  ~ West: There\'s a jail cell here.  \n  ~ East: There\'s a jail cell here.'
                },
        'Jailcell1': {
                'east': 'Jailroom3',
                'desc': 'A small jail cell. Not even enough room for a normal sized person to lay down.  \n  ~ East: Leads you back to the dungeons crossway.',
                'invitem': 'lockpick',
                'item': 'You notice a LOCKPICK on the ground near the entrance. You wonder if this person had ecaped, or if that pile of bones by the beast belonged to them.'
                },
        'Jailcell2': {
                'west': 'Jailroom3',
                'desc': 'A small jail cell. Not even enough room for a normal sized person to lay down.  \n  ~ West: Leads you back to the dungeons crossway.',
                'invitem': 'lastmeal',
                'item': 'You see a tray lying on the floor with something that barely resembles food for human consumption.\n    Looks as though the person was focefully dragged out.  Must of been thier LASTMEAL...'
                },
        'Jailroom4': {
# Need to use lockpick to go north. make it so it unlocks the door but breaks after being used.              
                'north': 'Jailroom5',
                'south': 'Jailroom3',
                'desc': 'This looks like an office of some sort. You hear moaning coming from the room to the north. Sounds like someone\'s hurt.\n    The door appears to be locked.',
# Scripted fight 'desc': 'This looks like an office of some sort. You hear moaning coming from the room to the north. Sounds like someone\'s hurt.\n    You approach the door slowly, not knowing what awaits you on the other side.\n  Just as you begin your approach towards the door, a pig-like creature emerges from it. It notices you and gives off an inhuman shriek all the while matching your gaze.\n    It quickly locks the door it emerged from and throws the key into a gutter that you believe is supposed to be a latrine.\n  It gives of a noise that sounds like a confident laugh. It unravels a whip and prepares to give you a proper greeting.'
# After fight    'desc2': 'The warden gives a death squeal so ear piercingly high, you check to make sure your ears aren\'t bleeding. It drops the OLDWHIP before dropping to the ground.  \n  ~ North: That\'s the door the warden came out from! The air feels colder the closer you are to it.  \n  ~ South: Takes you back to the dungeons crossway.'
# Using lockpick 'desc3': 'You decide to try the LOCKPICK you found to open the door. You aren\t the most experieneced when it comes to this.  After much trial an error, you finally get it! Unfortunately you broke the LOCKPICK in the process!'
# Nrml room fite 'desc4': 'You\'re in the office belong to the warden of the castle\'s dungeon. That pig bastard lying dead on the floor. You picture somehow finding a way to stuff his corpse into the latrine to be witht he rest of his kind.  A dry grin washes across your face.  \n  ~ North: That\'s the door the warden came out from! The air feels colder the closer you are to it.  \n  ~ South: Takes you back to the dungeons crossway.'
# Nrml room -fite'desc5': 'You\'re in what appears to be an office like space. Is someone in charge of this dungeon? The room is pretty well lit compared to the other rooms.  \n  ~ There is an arched wooden door. While picking the lock, you noticed the air coming from it was significantly colder.  \n  ~ South: Takes you back to the dungeons crossway.'
                'invitem': 'oldwhip',
                'item': 'The warden\'s favorite weapon, an OLDWHIP sits next to its coprse. It looks very beat up. It must of used it a lot in it\'s lifetime.'
# If can't fite  'item2': 'There is an OLDWHIP hanging on the wall. It looks incredibly worn. Must have been used a lot. Something tells you you shoudl take it.'                
                },
        'Jailroom5': {
                'south': 'Jailroom4',
                'desc': 'The room is freezing. Through your breath, you see a knight chained up -no. HANGING on the wall. He\'s still alive!\n    He\'s missing both of his legs and one of his arms from the elbow down. His body is a light blue hue. You hear gentle sobbing. You don\'t believe he even notices you\'re there.\n  \"How long has he been here?\" you wonder. He\'s not from your battalion. You walk closer, not knowing what to say, or how to react.\n  The gentle sobbing you hear slowly turns into words you can start making out: \"Kill me...Kill..me..\" he says.\n  \"What?!\" "Kill Me!!Kill Me Kill MeKillMeKillMeKillMeKIlLMEkIlLMeKILLMEKILLMEKILLMEKI-\"\n You grant his wish.  Slowly pulling your sword out of this chest, you try to come up with a means of justifying you actions.\n   If he hadn\'t shut up, he may have brought attention down here. You would of been trapped, possibly having the same fate as him.\n You keep telling youself it was the right thing to do...It was the right thing to do...It was the right thing to do...',
# after 1st desc/"cutscene"                'desc2': 'You look af the poor bastard hanging there and pay your respects.  \n  ~ South: The beginning of the way out of the dungeon. You don\'t like being in this room longer than necessary.'
                'invitem': 'breasplate',
# item 2, how?               'invitem': 'blizzard',
                'item': 'The poor bastards armor lies in a pile in the corner. It\'s all dented or cracked. No longer fit for use.\n   But wait! you notice the BREASTPLATE is relatively untouched.  It is freezing, but will warm up with you body heat. \n You also notice a spell scroll. The scroll reads BLIZZARD on it. Must be why the room is so cold.'
# scroll first   'item2': 'The poor bastards armor lies in a pile in the corner. It\'s all dented or cracked. No longer fit for use.\n   But wait! you notice the BREASTPLATE is relatively untouched.  It is freezing, but will warm up with you body heat.'
# Armor first    'item3': 'There\'s a BLIZZARD scroll lying by the remaning pieces of the poor bastards busted armor.'
                },
        'West1_Main': {
                'north': 'West1_North',
                'south': 'West1_South',
                'east': 'West1_East',
                'west': 'West1_West',
                'up': 'West2_Main',
                'down': 'West_Wing',
                'desc': 'After using the stairs, you\'re standing in the main room of the western tower. There\'s multiple areas to check.\n   Maybe you\'ll get lucky and catch the Dark Wizard off-guard.  \n  ~ North: There is a door lying on the floor. It was kicked open. There is a room wide open. You can see a body in there wearing your kingdom\'s colors.  \n  ~ South: There is a walkway that looks to lead outside.  \n  ~ West: There is a doorway.  \n  ~ East: There is a doorway. There is a dead monster neraby. Possibly a guard?  \n  ~ Up: There\'s a set of stairs leading further up the tower.  \n  ~ Down: There\'s a set of stairs leading back dowwn to the main floor of the castle.'
                },
        'West1_North': {
                'south': 'West1_Main',
                'desc': 'There is a knight impaled into the wall with a spear. The power behind that thrust must\'ve been incredible.  \n  ~ South: Go back into the main room.',
                'eqitem': 'gloves',
                'gear': 'The knight is grasping tightly to the spear. Was he trying to pull the spear out, or pull himself all the way through? \n  You\'ll never know.  The GLOVES look about your size though...'
                },
        'West1_South': {
                'north': 'West1_Main',
                'desc': 'You step out to the balcony. You take int he sights. You feel heat on your face and the smell of iron is thick in the air. It\'s a drepressingly meloncholy view.  \n  ~ North: Go back into the main room.'
                },
        'West1_East': {
                'west': 'West1_Main',
                'desc': 'You walk into the room, stepping over the guard in the process. You\'re standing in a bedchamber. It looks exquite.\n  More than a typical soldier would sleep in. Is this the bedchamber of Dark Mage?  \n  ~ West: Go back into the main room.'
                },
        'West1_West': {
                'east': 'West1_Main',
                'desc': 'A room full of potions and vials. Alchemy was perfomed here.  \n  ~ East: Go back to the main room',
                'invitem': 'poison',
                'item': 'You take note of..well a note. It reads"\n    \"That damn guardian beast! It\'s too damn picky! It won\'t even eat its meat raw.\n        It\'s below me to take care of that creature! I\'ll take care of it once and for all!!\"\n   A vial of POISON sits closeby the note. It\'s been knocked over, but is still intact and sealed tightly.'
                },
        'West2_Main': {
                'north': 'West2_Treasure',
                'down': 'West1_Main',
                'desc': ''
                },
        'West2_Treasure': {
                'south': 'West2_Main',
                'desc': ''
                },
        'East1_Main': {
                'north': 'East1_North',
                'south': 'East1_South',
                'west': 'East1_West',
                'up': 'East2_Main',
                'down': 'East_Wing',
                'desc': ''
                },
        'East1_North': {
                'south': 'East1_Main',
                'desc': ''
                },
        'East1_South': {
                'north': 'East1_Main',
                'desc': ''
                },
        'East1_West': {
                'east': 'East1_Main',
                'desc': ''
                },
        'East2_Main': {
                'north': 'East2_Duality',
                'down': 'East1_Main',
                'desc': ''
                },
        'East2_Duality': {
                'north': 'East2_Treasure',
                'south': 'East2_Main',
                'desc': ''
                },
        'East2_Treasure': {
                'south': 'East2_Duality',
                'desc': ''
                },
        'Main_Tower1': {
                'south': 'Main_Tower2',
                'down': 'Main_Hall_North',
                'desc': ''
                },
        'Main_Tower2': {
                'north': 'Main_Tower1',
                'east': 'Main_Tower3',
                'desc': ''
                },
        'Main_Tower3': {
                'north': 'Main_Tower4',
                'west': 'Main_Tower2',
                'desc': ''
                },
        'Main_Tower4': {
                'north': 'Main_Tower5',
                'south': 'Main_Tower3',
                'desc': ''
                },
        'Main_Tower5': {
                'south': 'Main_Tower4',
                'west': 'Main_Tower6',
                'desc': ''
                },
        'Main_Tower6': {
                'east': 'Main_Tower5',
                'west': 'Main_Tower7',
                'desc': ''
                },
        'Main_Tower7': {
                'north': 'Library',
                'south': 'Main_Tower8',
                'east': 'Main_Tower6',
                'desc': ''
                },
        'Library': {
                'south': 'Main_Tower7',
                'desc': ''
                },
        'Main_Tower8': {
                'north': 'Main_Tower7',
                'south': 'Main_Tower9',
                'desc': ''
                },
        'Main_Tower9': {
                'north': 'Main_Tower8',
                'up': 'Main_Tower_F2R1',
                'desc': ''
                },
        'Main_Tower_F2R1': {
                'east': 'Main_Tower_F2R2',
                'down': 'Main_Tower9',
                'desc': ''
                },
        'Main_Tower_F2R2': {
                'east': 'Main_Tower_F2R3',
                'west': 'Main_Tower_F2R1',
                'desc': ''
                },
        'Main_Tower_F2R3': {
                'west': 'Main_Tower_F2R2',
                'up': 'Main_Tower_Final1',
                'desc': ''
                },
        'Main_Tower_Final1': {
                'north': 'Main_Tower_Final2',
                'down': 'Main_Tower_F2R2',
                'desc': ''
                },
        'Main_Tower_Final2': {
                'north': 'Main_Tower_Final3',
                'desc': ''
                },
        'Main_Tower_Final3': {
                'south': 'Main_Tower_Final2',
                'desc': ''
                }
        }

# Players Starting Point
CurrentRoom = 'Tent'

#showInstructions()

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
    if move[0] == 'go':
        # Check to see if player is allowed to go wherever they want
        if move[1] in rooms[CurrentRoom]:
            # Sets current room to the new room
            CurrentRoom = rooms[CurrentRoom][move[1]]
        # Displays if no exit (link) in a direction
        else:
            print('Amidst your panic and exhastion, you were lost for a moment. Please input a valid move.')
    
    # If player types 'get' first
    if move[0] == 'get':
        # If the room contains an item, and they want to add it to their inventory
##        if 'item' in rooms[CurrentRoom] and move[1] in rooms[CurrentRoom]['item']:
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
