# text-monster
My implementation of the TEALS Program Text Monster game.

## Planning required by the rubric
For the initial version of the project, I plan to follow the data structures suggested in the Project Description.

### Gameboard
The gameboard for this game is very simplistic and doesn't require a lot of exploration. 
- The description requires three linear arrangements of five rooms each. 
- Each room can only contain one item or monster each.
- There are a total of four monsters (three "normal" monsters and one boss).
- Each monster needs a sword to kill it (since the swords disappear after killing a monster).
- The boss also needs magic stones to kill it.
- The boss guards the room on the other side of it that contains the "prize" that will win the game.
- You can only change floors at an up-staircase or a down-staircase. Assuming no "magical" staircases that only go one direction and disappear after you've passed through them, this means there will be two up-staircases and two down-staircases.
- Adding these all up means there are objects in 14 of the 15 rooms in the gameboard.
Creating the gameboard using three lists, as suggested in the description, I plan to implement the following gameboard. (It's a dungeon, so the floors go down from 1-3, rather than up.)

```python
floor_1 = ['nothing', 'sword', 'sword', 'sword', 'stairs down']
floor_2 = ['stairs down', 'monster', 'magic stones', 'sword', 'stairs up']
floor_3 = ['stairs up', 'monster', 'monster', 'boss', 'prize']
```
Note that I "front-loaded" the items in order to test the three item limit in the user inventory. It makes for a very artificial and not-at-all fun gameboard.

### Player position
As suggested in the Project Description, I plan to use two vairables to track the player's position: one for the floor the player is on and one for the room the player is in.
```python
player_room = 0
player_floor = floor_1
```
The __player_floor__ variable keeps track of which list the player is in and the __player_room__ variable keeps track of the index in the list.

The starting position is the "nothing" cell in __floor_1[0]__.

### Inventory
The Program description requires using a list to track the items the player is carrying. The player can hold no more than three items. Also, the Project Description doesn't have an "inventory" command or a "drop" command, so the player would have to remember everything they've picked up and expended and, if the player does pick up too many items, thus preventing them from picking up an item they need (like the magic stones), the player needs to fight a monster to open a position in their inventory. I set up the gameboard with all of the needed items in adjacent rooms to test the inventory limit, which means the player has to backtrack to pick up the magic stones and sword needed to defeat the boss. The inventory starts as an empty list and the program logic ensures it can only have length <= 3.
```python
inventory = []
```

### Player commands
The Project Description lists the following seven commands as allowable input from the player.
- left
- right
- up
- down
- grab
- fight
- help

The Project Description does not specify what the __help__ command should do. I've decided it should print out a list of possible commands and the player inventory (since there's no __inventory__ command).

I also noticed that the allowable commands all start with a unique letter. To make life easier for the player, I plan to convert the player input string to lowercase and only check the first letter of the input. To enable printing the valid commands and validating player input, I plan to use two lists: one with the full commands for printing and one with only the first letters for player input validation. There are also two variables to get the player input and for the cleaned-up input.
```python
valid_commands = ['[l]eft', '[r]ight', '[u]p', '[d]own', '[g]rab', '[f]ight', '[h]elp']
valid_inputs = ['l', 'r', 'u', 'd', 'g', 'f', 'h']
player_input = input(input_prompt)
simplified_input = player_input.lower()[0]
```

*There are more implementation details that need to be considered to create the game, but these are all of the variables that need to be planned for, according to the lesson plan and rubric. Also, when implementing the game, I realized I didn't need the valid commands list.* 