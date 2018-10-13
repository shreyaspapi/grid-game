
import random


CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]



def get_locations():
    return random.sample(CELLS, 3)


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


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    return moves


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

def game_loop():
    monster, door, player = get_locations()
    playing = True
    
    while playing:
        draw_map(player, monster, door)
        valid_moves = get_moves(player)
        
        print("You're currently in room {}".format(player))
        print("You can move {}".format(", ".join(valid_moves)))
        print("Enter QUIT to quit")
        
        move = input("> ")
        move = move.upper()
        
        if move == 'QUIT':
            print("\n ** See you next time! **\n")
            break
        if move in valid_moves:
            player = move_player(player, move)
            
            if player == monster:
                print("\n ** Oh no! The monster got you! Better luck next time! **\n")
                playing = False
            if player == door:
                print("\n ** You escaped! Congratulations! **\n")
                playing = False
        else:
            input("\n ** Walls are hard! Don't run into them! **\n")
    else:
        if input("Play again? [Y/n] ").lower() != "n":
            game_loop()



print("Welcome to the dungeon!")
print("You have 1 life with you Try your luck!!")
input("Press Enter to start!")

game_loop()

