player_names = []

while input("Would you like to add a player to the list? Y/N     ").lower() == "y":
    player_names.append(input("Please enter the player's name:     "))

print("There are {} players on your team.".format(len(player_names)))

player_number = 1
for player in player_names:
    print("Player {}: {}".format(player_number, player))
    player_number += 1


goal_keeper = int(input("Please enter the player NUMBER of your goalkeeper (1 - {}):     ".format(len(player_names))))
#TODO: enter value error resolution
goal_keeper = player_names[goal_keeper - 1]
print("{} is your goalkeeper.".format(goal_keeper))
