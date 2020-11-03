#!usr/bin/env python3

## As of now, this is used to try to "build" the map
# The dictionary used to link the rooms together
rooms = {
        'Tent':{
                'north': 'Camp'
                },
        'Camp':{
                'north': 'Bridge'
                },
        'Bridge':{
                'north': 'Courtyard_Main'
                },
        'Courtyard_Main':{
                'north': 'Castle_Entrance',
                'east': 'Courtyard_East',
                'west': 'Courtyard_West'
                },
        'Courtyard_West':{
                'north': 'Courtyard_Midwest',
                'east': 'Courtyard_Main'
                },
        'Courtyard_Midwest':{
                'north': 'Courtyard_Northwest',
                'south': 'Courtyard_West'
                },
        'Courtyard_Northwest':{
                'south': 'Courtyard_Midwest'
                },
        'Courtyard_East':{
                'north': 'Courtyard_Mideast',
                'west': 'Courtyard_Main'
                },
        'Courtyard_Mideast':{
                'south': 'Courtyard_East'
                },
        'Castle_Entrance':{
                'north': 'Corridor',
                'south': 'Courtyard_Main'
                },
        'Corridor':{
                'north': 'Hall'
                },
        'Hall':{
                'north': 'Main_Hall_South'
                },
        'Main_Hall_South':{
                'north': 'Main_Hall_Center',
                'east': 'Main_Hall_Southeast',
                'west': 'Main_Hall_Southwest'
                },
        'Main_Hall_Southwest':{
                'north': 'Main_Hall_West',
                'east': 'Main_Hall_South',
                'down': 'Jailroom1'
                },
        'Main_Hall_West':{
                'north': 'Kitchen',
                'south': 'Main_Hall_Southwest',
                'east': 'Main_Hall_Center',
                'west': 'West_Wing'
                },
        'Kitchen':{
                'north': 'Meat_Locker',
                'south': 'Main_Hall_West'
                },
        'Meat_Locker':{
                'south': 'Kitchen'
                },
        'Main_Hall_Southeast':{
                'north': 'Main_Hall_East',
                'west': 'Main_Hall_South'
                },
        'Main_Hall_East':{
                'north': 'Barracks',
                'south': 'Main_Hall_Southeast',
                'east': 'East_wing',
                'west': 'Main_Hall_Center'
                },
        'Barracks':{
                'north': 'Armory',
                'south': 'Main_Hall_East'
                },
        'Armory':{
                'south': 'Barracks'
                },
        'Main_Hall_Center':{
                'north': 'Main_Hall_North',
                'south': 'Main_Hall_South',
                'east': 'Main_Hall_East',
                'west': 'Main_Hall_West'
                },
        'Main_Hall_North':{
                'north': 'Castlevania',
                'south': 'Main_Hall_Center',
                'up': 'Main_Tower1'
                },
        'Castlevania':{
                'south': 'Main_Hall_North'
                },
        'West_Wing':{
                'east': 'Main_Hall_West',
                'up': 'West_Main1'
                },
        'East_Wing':{
                'west': 'Main_Hall_East',
                'up': 'East_Main1'
                },
        'Jailroom1':{
                'north': 'Jailroom2',
                'up': 'Main_Hall_Southwest'
                },
        'Jailroom2':{
                'north': 'Jailroom3',
                'south': 'Jailroom1'
                },
        'Jailroom3':{
                'north': 'Jailroom4',
                'south': 'Jailroom2',
                'east': 'Jailcell2',
                'west': 'Jailcell1'
                },
        'Jailcell1':{
                'east': 'Jailroom3'
                },
        'Jailcell2':{
                'west': 'Jailroom3'
                },
        'Jailroom4':{
                'north': 'Jailroom5',
                'south': 'Jailroom3'
                },
        'Jailroom5':{
                'south': 'Jailroom4'
                },
        }

