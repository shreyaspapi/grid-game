
import random


CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]


# Samples 3 random tuples from the CELLS which become the location of monster door and player
def get_locations():
    return random.sample(CELLS, 3)

'''
Receives the current location of the player and the move chosen by the player and returns the position
of the player after making the move.
'''
def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    return x, y

'''
Receives the players current location and return what are the valid moves that the player can make
in the given position.
'''
def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if x == 0:
        moves.remove("LEFT") # removes "LEFT" from the list
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    return moves

'''
Function displays the positions of player,Door and moster in the form of a gird.
eg:
 _ _ _ _ _
|_|_|_|_|_|
|_|_|_|X|_|
|_|_|_|_|_|
|_|_|_|_|D|
|_|_|_|_|_|

Here X is the player abd D is the door to be reached.
'''
def draw_map(player, monster, door):
    print(" _"*5)
    tile = "|{}"
    
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            elif cell == door:
                output = tile.format("D")
            #elif cell == monster:
                #output = tile.format("M")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            elif cell == monster:
                output = tile.format("M|")
                            
            elif cell == door:
                output = tile.format("D|")           
            else:
                output = tile.format("_|")
        print(output, end=line_end)

'''
The main function which manages the entire game
'''
def game_loop():
    monster, door, player = get_locations()
    playing = True
    
    while playing:
        draw_map(player, monster, door) # draws the grid with player, monster and door
        valid_moves = get_moves(player) # gets the valid moves for the given position
        
        print("You're currently in room {}".format(player))
        print("You can move {}".format(", ".join(valid_moves)))
        print("Enter QUIT to quit")
        
        move = input("> ")
        move = move.upper()
        
        if move == 'QUIT':   # break the loop if the player enters QUIT
            print("\n ** See you next time! **\n")
            break
        if move in valid_moves:
            player = move_player(player, move) #gives the new position of the player as per the move which was input by the player
            
            if player == monster:
                print("\n ** Oh no! The monster got you! Better luck next time! **\n")
                playing = False
            if player == door:
                print("\n ** You escaped! Congratulations! **\n")
                playing = False
        else:
            input("\n ** Walls are hard! Don't run into them! **\n") # in case the move is not valid
    else:
        if input("Play again? [Y/n] ").lower() != "n":
            game_loop()  #Restarts the game 



print("Welcome to the dungeon!")
print("You have 1 life with you Try your luck!!")
input("Press Enter to start!")

game_loop()

