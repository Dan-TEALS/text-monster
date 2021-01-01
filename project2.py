''' Text Monster (Simple)
      A Zork clone in which the player moves around a three level dungeon.
    * The dungeon has five rooms in each level laid out in a line.
    * The possible moves are left, right, up, and down, but not every move is
    possible in every room.
    * Each room can contain a sword, a monster, magic stones, up-stairs, 
    down-stairs, or nothing.
    * Players can grab a sword or magic stones if they are present in a room.
    * The player wins if they retrieve the prize.

Dan Stormont
December 2020
'''

# GAME INITIALIZATION
# The game has three floors.
# Each floor is made up of five rooms, arranged in a line from left to right.
# A room can contain: a sword, a monster, magic stones, up-stairs, down-stairs, or nothing.
# There should be three regular monsters placed throughout the game. (These require a sword to defeat.)
# There should be a boss monster in the room just before the room that contains the prize.
# (This monster requires magic stones and a sword to defeat.)
# The gameboard can be implemented using three lists, one for each floor.
floor_1 = ['nothing', 'sword', 'sword', 'sword', 'stairs down']
floor_2 = ['stairs down', 'monster', 'magic stones', 'sword', 'stairs up']
floor_3 = ['stairs up', 'monster', 'monster', 'boss', 'prize']

# At the start of the game, the user is placed in one of the rooms.
# The player's position should be tracked using one or more variables.
player_room = 0
player_floor = floor_1

# Need an additional variable to track where the player came from to check for walking past a monster.
player_previous_room = 0

# On each move, the user has seven possible commands: left, right, up, down, grab, fight, and help.
valid_inputs = ['l', 'r', 'u', 'd', 'g', 'f', 'h']

# Use a list to keep track of the player's items.
# At the beginning of the game, it should be empty.
inventory = []


# GAME LOGIC

# Display a greeting to the player when the game starts.
print('Welcome to the dungeon!')

# Instruction string that can be printed when the help command is entered.
instruction_string = '''Your goal is to defeat all the monsters and collect the prize.
The dungeon has three floors. You start on the ground floor and descend into the dungeon.
You can move [l]eft or [r]ight, as long as there is a room in that direction.
You can go [d]own to the next level if there are "stairs down" in the room or [u]p if there are "stairs up."
If you find an item in a room (sword or magic stones), you can [g]rab them, but you can only hold three items at a time.
If there is a monster in the room, you can [f]ight it.
You will need a sword to fight a monster and a sword and the magic stones to fight the boss monster.
If you try to fight without the needed items, you will be defeated and the game will end. 
You can leave a room with a monster in the same direction you came in.
If you try to walk past the monster, you will be defeated and the game will end.''' 

print(instruction_string)
print('Good luck, intrepid adventurer!')

# Set up the game loop.
player_active = True
while player_active:
  # If the input is invalid, the game will let the user know.
  valid_input = False
  while not valid_input:
    # Prompt the player for a command.
    input_prompt = 'Please enter a command ([l]eft, [r]ight, [u]p, [d]own, [g]rab, [f]ight, [h]elp): '
    player_input = input(input_prompt)

    # Simplify the input.
    simplified_input = player_input.lower()[0]

    # If the input is invalid, the game will let the user know.
    if simplified_input not in valid_inputs:
      print(player_input, 'is not valid.')
    else:
      valid_input = True

  # If the input is valid, the game will execute the user's command.
  # The user can move left, right, up, or down.
  # The game should not allow a player to move if there is no room in that direction.
  # If the player tries to walk past a monster, they will be defeated and the game will end.
  if simplified_input == 'l':
    if player_room == 0:
      print("There is a wall to your left. You can't go that way!")
    elif (player_floor[player_room] == 'monster' or player_floor[player_room] == 'boss') and player_previous_room > player_room:
      print('The monster has defeated you. The game is over!')
      player_active = False
    else:
      player_previous_room = player_room
      player_room -= 1
  if simplified_input == 'r':
    if player_room == len(player_floor) - 1:
      print("There is a wall to your right. You can't go that way!")
    elif (player_floor[player_room] == 'monster' or player_floor[player_room] == 'boss') and player_previous_room < player_room:
      print('The monster has defeated you. The game is over!')
      player_active = False
    else:
      player_previous_room = player_room
      player_room += 1
  # The user can only go up if there is an up-staircase.
  if simplified_input == 'u':
    if player_floor[player_room] != 'stairs up':
      print("There are no stairs going up here. You can't go that way!")
    else:
      player_previous_room = player_room
      if player_floor == floor_3:
        player_floor = floor_2
      else:
        player_floor = floor_1
  # The user can only go down if there is a down-staircase.
  if simplified_input == 'd':
    if player_floor[player_room] != 'stairs down':
      print("There are no stairs going down here. You can't go that way!")
    else:
      player_previous_room = player_room
      if player_floor == floor_2:
        player_floor = floor_3
      else:
        player_floor = floor_2
  # The user can grab swords or magic stones if they walk into a room with them.
  # The sword or stones are no longer in the room once grabbed.
  if simplified_input == 'g':
    if player_floor[player_room] == 'sword' or player_floor[player_room] == 'magic stones':
      # Use a list to keep track of the player's items.
      # A maximum of three items can be held at once.
      if len(inventory) == 3:
        print("You are already holding three items, you can't grab any more.")
      else:
        inventory.append(player_floor[player_room])
        player_floor[player_room] = 'nothing'
    # This is not covered in the Project Description, but it makes sense that trying to grab a 
    # monster would be a BAD IDEA.
    elif player_floor[player_room] == 'monster' or player_floor[player_room] == 'boss':
      print('You tried to grab a monster...not a good idea. The monster defeated you!')
      player_active = False
    else:
      print('There is nothing here to grab.')
  # Monsters guard some rooms.
  # The user can use a sword to defeat a monster using the fight command.
  if simplified_input == 'f':
    if player_floor[player_room] != 'monster' and player_floor[player_room] != 'boss':
      print('There is nothing to fight here.')
    # If the player fights without a sword, they will be defeated and the game will end.
    elif (player_floor[player_room] == 'monster' or player_floor[player_room] == 'boss') and 'sword' not in inventory:
      print("You don't have a sword. You have been defeated!")
      player_active = False
    # If the player fights the boss monster without a sword and the magic stones, they will
    # be defeated and the game will end.
    elif player_floor[player_room] == 'boss' and 'magic stones' not in inventory:
      print("You don't have the magic stones. The boss monster defeats you!")
      player_active = False
    # The sword and monster disappear after fighting.
    elif player_floor[player_room] == 'monster':
      print('You defeated the monster!')
      player_floor[player_room] = 'nothing'
      inventory.remove('sword')
    else: # the player must be fighting the boss monster
      print('You defeated the boss monster!')
      player_floor[player_room] = 'nothing'
      inventory.remove('sword')
      inventory.remove('magic stones')
  # The Project Description doesn't say what should happen if a player requests help.
  # I decided to print the instruction string and the player's inventory.
  if simplified_input == 'h':
    print(instruction_string)
    if len(inventory) == 0:
      print("You aren't carrying any items.")
    else:
      print('You are carrying the following items:')
      for item in inventory:
        print(item)

  # The game prints out the contents of the current room after every (successful) command.
  # If the player is not active, they have been defeated or won the game and there is no reason
  # to print the contents of the room.
  if player_active:
    if player_floor[player_room] == 'sword' or player_floor[player_room] == 'monster':
      print('You see a', player_floor[player_room], 'in the room.')
    elif player_floor[player_room] == 'magic stones' or player_floor[player_room] == 'prize':
      print('You see the', player_floor[player_room], 'in the room.')
    elif player_floor[player_room] == 'boss':
      print('You see the boss monster in the room.')
    else:
      print('You see', player_floor[player_room], 'in the room.')

  # Check for the victory condition.
  if player_floor[player_room] == 'prize':
    print("You've retrieved the prize. Congratulations...You win!")
    player_active = False

