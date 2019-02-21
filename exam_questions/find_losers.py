'''
You are a part of a game development team. You have two lists round 1 and round 2.
Each list contains the player names.
Write a code to print the player who lost in the first round.
'''

round1 = ['Scott', 'Eric', 'Kelly', 'Emma', 'Smith']
round2 = ['Scott', 'Eric', 'Kelly']

for player in round1:
    if player not in round2:
        print(player)