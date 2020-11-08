#!/usr/bin/env python3

def showInstructions():
    print("""
Welcome to Doug's Kickass RPG Game
==================================
Instructions:
get
go
Doug's gotta fix this
""")


def ShowStatus():
    # Displays the player's current location
    print('╔════════════════════════════════════════════╗')
    print(' ● ' + rooms[CurrentRoom]['desc'])
#    print('╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣')
    # Also display any items in the room 
    if "invitem" in rooms[CurrentRoom]:
        print('╠═══════════════════════════════════════════════╣')
        print(' ‣ ' + rooms[CurrentRoom]['item'])
    if "eqitem" in rooms[CurrentRoom]:
        print('╠══════════════════════════════════════════════╣')
        print(' ⁍ ' + rooms[CurrentRoom]['gear'])
    print('╚══════════════════════════════════════════════════╝')
# Player's Inventory
inventory = []

## As of now, this is used to try to "build" the map try to see if movent is programmable by tonight.
# The dictionary used to link the rooms together
rooms = {
        'Tent': {
                'north': 'Camp',
                'desc': 'There is a pile of sweat-smelling blankets you\'ve had with you since you and your comerades set forth in this journey. There is some light shining into the tent though the opening in the \'North\'.',
                'invitem': 'BREAKFAST',
                'item': 'You notice your BREAKFAST lying on the ground next to the sheets. It\'s probably a good idea to eat it now. [Use the \'get BREAKFAST\' command to add the item to your inventory, followed by \'use BREAKFAST\' to eat it]',
                'eqitem': 'test',
                'gear': 'testing'
                },
        'Camp': {
                'north': 'Bridge',
                'desc': "test",
                'eqitem': 'test2',
                'gear': 'teest'
                },
        'Bridge': {
                'north': 'Courtyard_Main'
                },
        'Courtyard_Main': {
                'north': 'Castle_Entrance',
                'east': 'Courtyard_East',
                'west': 'Courtyard_West'
                },
        'Courtyard_West': {
                'north': 'Courtyard_Midwest',
                'east': 'Courtyard_Main'
                },
        'Courtyard_Midwest': {
                'north': 'Courtyard_Northwest',
                'south': 'Courtyard_West'
                },
        'Courtyard_Northwest': {
                'south': 'Courtyard_Midwest'
                },
        'Courtyard_East': {
                'north': 'Courtyard_Mideast',
                'west': 'Courtyard_Main'
                },
        'Courtyard_Mideast': {
                'south': 'Courtyard_East'
                },
        'Castle_Entrance': {
                'north': 'Corridor',
                'south': 'Courtyard_Main'
                },
        'Corridor': {
                'north': 'Hall'
                },
        'Hall': {
                'north': 'Main_Hall_South'
                },
        'Main_Hall_South': {
                'north': 'Main_Hall_Center',
                'east': 'Main_Hall_Southeast',
                'west': 'Main_Hall_Southwest'
                },
        'Main_Hall_Southwest': {
                'north': 'Main_Hall_West',
                'east': 'Main_Hall_South',
                'down': 'Jailroom1'
                },
        'Main_Hall_West': {
                'north': 'Kitchen',
                'south': 'Main_Hall_Southwest',
                'east': 'Main_Hall_Center',
                'west': 'West_Wing'
                },
        'Kitchen': {
                'north': 'Meat_Locker',
                'south': 'Main_Hall_West'
                },
        'Meat_Locker': {
                'south': 'Kitchen'
                },
        'Main_Hall_Southeast': {
                'north': 'Main_Hall_East',
                'west': 'Main_Hall_South'
                },
        'Main_Hall_East': {
                'north': 'Barracks',
                'south': 'Main_Hall_Southeast',
                'east': 'East_Wing',
                'west': 'Main_Hall_Center'
                },
        'Barracks': {
                'north': 'Armory',
                'south': 'Main_Hall_East'
                },
        'Armory': {
                'south': 'Barracks'
                },
        'Main_Hall_Center': {
                'north': 'Main_Hall_North',
                'south': 'Main_Hall_South',
                'east': 'Main_Hall_East',
                'west': 'Main_Hall_West'
                },
        'Main_Hall_North': {
                'north': 'Castlevania',
                'south': 'Main_Hall_Center',
                'up': 'Main_Tower1'
                },
        'Castlevania': {
                'south': 'Main_Hall_North'
                },
        'West_Wing': {
                'east': 'Main_Hall_West',
                'up': 'West1_Main'
                },
        'East_Wing': {
                'west': 'Main_Hall_East',
                'up': 'East1_Main'
                },
        'Jailroom1': {
                'north': 'Jailroom2',
                'up': 'Main_Hall_Southwest'
                },
        'Jailroom2': {
                'north': 'Jailroom3',
                'south': 'Jailroom1'
                },
        'Jailroom3': {
                'north': 'Jailroom4',
                'south': 'Jailroom2',
                'east': 'Jailcell2',
                'west': 'Jailcell1'
                },
        'Jailcell1': {
                'east': 'Jailroom3'
                },
        'Jailcell2': {
                'west': 'Jailroom3'
                },
        'Jailroom4': {
                'north': 'Jailroom5',
                'south': 'Jailroom3'
                },
        'Jailroom5': {
                'south': 'Jailroom4'
                },
        'West1_Main': {
                'north': 'West1_North',
                'south': 'West1_South',
                'east': 'West1_East',
                'west': 'West1_West',
                'up': 'West2_Main',
                'down': 'West_Wing'
                },
        'West1_North': {
                'south': 'West1_Main'
                },
        'West1_South': {
                'north': 'West1_Main'
                },
        'West1_East': {
                'west': 'West1_Main'
                },
        'West1_West': {
                'east': 'West1_Main'
                },
        'West2_Main': {
                'north': 'West2_Treasure',
                'down': 'West1_Main'
                },
        'West2_Treasure': {
                'south': 'West2_Main'
                },
        'East1_Main': {
                'north': 'East1_North',
                'south': 'East1_South',
                'west': 'East1_West',
                'up': 'East2_Main',
                'down': 'East_Wing'
                },
        'East1_North': {
                'south': 'East1_Main'
                },
        'East1_South': {
                'north': 'East1_Main'
                },
        'East1_West': {
                'east': 'East1_Main'
                },
        'East2_Main': {
                'north': 'East2_Duality',
                'down': 'East1_Main'
                },
        'East2_Duality': {
                'north': 'East2_Treasure',
                'south': 'East2_Main'
                },
        'East2_Treasure': {
                'south': 'East2_Duality'
                },
        'Main_Tower1': {
                'south': 'Main_Tower2',
                'down': 'Main_Hall_North'
                },
        'Main_Tower2': {
                'north': 'Main_Tower1',
                'east': 'Main_Tower3'
                },
        'Main_Tower3': {
                'north': 'Main_Tower4',
                'west': 'Main_Tower2'
                },
        'Main_Tower4': {
                'north': 'Main_Tower5',
                'south': 'Main_Tower3'
                },
        'Main_Tower5': {
                'south': 'Main_Tower4',
                'west': 'Main_Tower6'
                },
        'Main_Tower6': {
                'east': 'Main_Tower5',
                'west': 'Main_Tower7'
                },
        'Main_Tower7': {
                'north': 'Library',
                'south': 'Main_Tower8',
                'east': 'Main_Tower6'
                },
        'Library': {
                'south': 'Main_Tower7'
                },
        'Main_Tower8': {
                'north': 'Main_Tower7',
                'south': 'Main_Tower9'
                },
        'Main_Tower9': {
                'north': 'Main_Tower8',
                'up': 'Main_Tower_F2R1'
                },
        'Main_Tower_F2R1': {
                'east': 'Main_Tower_F2R2',
                'down': 'Main_Tower9'
                },
        'Main_Tower_F2R2': {
                'east': 'Main_Tower_F2R3',
                'west': 'Main_Tower_F2R1'
                },
        'Main_Tower_F2R3': {
                'west': 'Main_Tower_F2R2',
                'up': 'Main_Tower_Final1'
                },
        'Main_Tower_Final1': {
                'north': 'Main_Tower_Final2',
                'down': 'Main_Tower_F2R2'
                },
        'Main_Tower_Final2': {
                'north': 'Main_Tower_Final3'
                },
        'Main_Tower_Final3': {
                'south': 'Main_Tower_Final2'
                }
        }

# Players Starting Point
CurrentRoom = 'Tent'
showInstructions()

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
            print(move[1] + ' acquired!')
            # Removes item from the room itself
            del rooms[CurrentRoom]['invitem']
        # If there is no item to get
        else:
            print('Your mind must be playing tricks on you. There\'s no ' + move[1] + ' there!')
